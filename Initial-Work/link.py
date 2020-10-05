import pandas as pd
import numpy as np

df = pd.read_csv("fips-cases-final.csv")
data = df.values.tolist()

countydf = pd.read_csv("county2014_2018.csv")

mp = {}

counter = 0
ndata = []
for entry in data:
    current = entry[:]

    fips_code = entry[5]
    # print(fips_code)
    if not np.isnan(fips_code):
        df1 = (countydf.loc[countydf['county'] == fips_code])
        dflist = df1.values.tolist()

        if len(dflist) > 0:
            good_data = dflist[0][1:-1]
            current.extend(good_data)

    # if counter < 20:
    #     print(current)
    # counter += 1

    ndata.append(current)

# counter stores number of successful queries in the vacovidsummary-new.csv file
#print("counter", counter)

final_data = pd.DataFrame(ndata, columns=["VA Station Number","HCS","Address","City","State","County FIPS","Cases","Active","Convalescent","Deaths","totpop","medhhincome","medhvalue","male","age_under18","age_18_24","age_25_34","age_35_44","age_45_54","age_55_64","age_65_74","age_75_84","age_85pl","race_white","race_black","race_nativeam","race_asian","married","divorced","educ_lesshs","educ_somecoll","educ_college","educ_collpl","urate_all","urate_male","urate_female","HSdropout_male","HSdropout_female","ind_agmining","ind_const","ind_manuf","ind_wholesale","ind_retail","ind_transport","ind_info","ind_FIRE","ind_pro","ind_educhealth","ind_artentertain","ind_otherserve","ind_public","occ_mgmtbiz","occ_pro","occ_healthsupp","occ_protective","occ_food","occ_building","occ_personalcare","occ_sales","occ_officeadmin","occ_farming","occ_constextract","occ_production","occ_transport","income_less10k","income_10k15","income_15k20","income_20k25","income_25k30","income_30k35","income_35k40","income_40k45","income_45k50","income_50k60","income_60k75","income_75k100","income_100k125","income_125k150","income_150kpl","rent_share_income","poverty_under18","poverty_18_64","poverty_65pl","poverty_white","poverty_black","poverty_nativeA","vetshare_18_64","vetshare_65pl"])
final_data.to_csv('data.csv', index=False)