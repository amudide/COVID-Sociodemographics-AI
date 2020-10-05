# cleans data-full.csv; extracts useful information from the VA API data
import pandas as pd
import numpy as np 
import json
import ast
import math

df = pd.read_csv("data-full.csv")

data = df.values.tolist()


countbad = 0
ndata = []
for entry in data:
    cur = entry[:]

    #services = json.loads(cur[88]) 
    services = ast.literal_eval(cur[88])
    #print(services)
    #print(type(services))

    cur.append(len(services)) # appends a new feature with the number of services
    #print(len(services))

    cur[89] = cur[89].replace("'", "\"")
    scores = json.loads(cur[89])
    #print(type(scores))

    scoreS = 0
    scoreN = 0

    for p in scores:
        scoreN += 1
        scoreS += scores[p]
    
    if scoreN == 0:
        countbad += 1
        cur.append(math.nan)
    else:
        cur.append(scoreS / scoreN)
    
    # appended average score to cur data list

    ndata.append(cur)


print('bad:', countbad)
final_data = pd.DataFrame(ndata, columns=["VA Station Number","HCS","Address","City","State","County FIPS","Cases","Active","Convalescent","Deaths","totpop","medhhincome","medhvalue","male","age_under18","age_18_24","age_25_34","age_35_44","age_45_54","age_55_64","age_65_74","age_75_84","age_85pl","race_white","race_black","race_nativeam","race_asian","married","divorced","educ_lesshs","educ_somecoll","educ_college","educ_collpl","urate_all","urate_male","urate_female","HSdropout_male","HSdropout_female","ind_agmining","ind_const","ind_manuf","ind_wholesale","ind_retail","ind_transport","ind_info","ind_FIRE","ind_pro","ind_educhealth","ind_artentertain","ind_otherserve","ind_public","occ_mgmtbiz","occ_pro","occ_healthsupp","occ_protective","occ_food","occ_building","occ_personalcare","occ_sales","occ_officeadmin","occ_farming","occ_constextract","occ_production","occ_transport","income_less10k","income_10k15","income_15k20","income_20k25","income_25k30","income_30k35","income_35k40","income_40k45","income_45k50","income_50k60","income_60k75","income_75k100","income_100k125","income_125k150","income_150kpl","rent_share_income","poverty_under18","poverty_18_64","poverty_65pl","poverty_white","poverty_black","poverty_nativeA","vetshare_18_64","vetshare_65pl","Services","Satisfaction","Wait Times","Num-Services","Avg-Satisfaction"])

final_data["Log-Cases"] = np.log2(df["Cases"] + 1) 
final_data["Log-Deaths"] = np.log2(df["Deaths"] + 1) 

final_data.to_csv('data-full-cleaned.csv', index=False)