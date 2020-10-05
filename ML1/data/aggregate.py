# imputes data

import pandas as pd
import numpy as np

centers = set()

data = pd.read_csv("data-imp2-adj.csv")
badc = 0

ndata = []

with open('centers.txt') as fp:
    content = fp.readlines()
    for line in content:
        #print(line[0:-1])
        line = int(line[0:3])
        #print(line)
        centers.add(line)

for center in centers:
    df = (data.loc[data['HCS'] == center])
    #print(df)


    # CHECK FOR LENGTH 0; jk?

    if np.isnan((df['Cases'].values.tolist())[0]):
        badc += 1
        continue

    curdata = df.values.tolist()
    
    #print(curdata)
    #print(len(curdata[0]))

    # 6 : 87 inclusive

    cur = [0] * 82
    #print(cur)
    totvets = 0
    for rowdata in curdata:
        adder = [item * rowdata[-1] for item in rowdata[6:88]]
        #print("adder:", adder)
        for i in range(len(cur)):
            cur[i] += adder[i]
        totvets += rowdata[-1]
    cur = [i/totvets for i in cur]
    #print(totvets)
    #print("cur:",cur)

    finald = []
    finald.append(center)
    finald.extend(cur)
    #print(finald)
    #print(len(finald))
    ndata.append(finald)
    
print(badc)

final_data = pd.DataFrame(ndata, columns=["HCS","totpop-log","medhhincome-log","medhvalue-log","male","age_under18","age_18_24","age_25_34","age_35_44","age_45_54","age_55_64","age_65_74","age_75_84","age_85pl","race_white","race_black","race_nativeam","race_asian","married","divorced","educ_lesshs","educ_somecoll","educ_college","educ_collpl","urate_all","urate_male","urate_female","HSdropout_male","HSdropout_female","ind_agmining","ind_const","ind_manuf","ind_wholesale","ind_retail","ind_transport","ind_info","ind_FIRE","ind_pro","ind_educhealth","ind_artentertain","ind_otherserve","ind_public","occ_mgmtbiz","occ_pro","occ_healthsupp","occ_protective","occ_food","occ_building","occ_personalcare","occ_sales","occ_officeadmin","occ_farming","occ_constextract","occ_production","occ_transport","income_less10k","income_10k15","income_15k20","income_20k25","income_25k30","income_30k35","income_35k40","income_40k45","income_45k50","income_50k60","income_60k75","income_75k100","income_100k125","income_125k150","income_150kpl","rent_share_income","poverty_under18","poverty_18_64","poverty_65pl","poverty_white","poverty_black","poverty_nativeA","vetshare_18_64","vetshare_65pl","Num-Services","Avg-Satisfaction","Log-Cases","Log-Deaths"])
final_data.sort_values(by = 'HCS', inplace = True)
final_data.to_csv('data-agg.csv', index=False)