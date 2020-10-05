import numpy as np
import pandas as pd

params = [ 6.43876881e-01,1.99863506e-01, -4.20179566e-01, -2.47760331e-01
, 1.35979241e-01, -3.99118532e-02,1.13993150e-01,1.28232053e-02
, 4.23777740e-02, -1.91022170e-01, -6.83391369e-02,1.53491284e-03
 , -7.43512057e-03, -7.38832812e-01,2.24677642e+00, -1.45745910e-02
 , -7.30838836e-01, -3.28260338e-01, -1.78202037e-01,4.52461661e-02
 , -7.80240063e-01,4.13277586e-01,3.21716238e-01, -1.04944139e-01
 , -1.66901434e-01, -3.44855383e-02,1.77997429e-01, -5.16539728e-02
 , -3.31949026e-01,1.39569829e-01, -1.76375800e-01,3.15822475e-02
, 1.65546426e-02, -1.85802488e-01,8.10649612e-02,2.27329710e-01
, 5.17709633e-01,5.83864514e-02, -2.22060012e-01,3.31596809e-02
 , -1.89169962e-01,2.42664075e-01,3.07409205e-01, -1.72251989e-02
, 1.62540589e-02, -1.07163760e-01, -2.07987904e-02,2.69434677e-02
, 1.39714639e-01, -1.47795343e-01, -4.99570272e-02, -9.11559498e-02
 , -6.30929106e-02, -2.35796474e-01,8.13760382e-02,1.00356555e-01
 , -3.61362184e-02,1.65552534e-02,1.48080910e-02,1.44910396e-02
, 9.12779645e-04,1.38491138e-02, -3.15594356e-03, -4.35775015e-02
 , -1.39160677e-01, -1.79279264e-01, -1.34066860e-01, -5.20789214e-02
, 3.45106605e-01,1.90647244e-01,3.53414086e-01, -1.00081963e-01
, 3.58687231e-01, -2.18869462e-01, -4.31314337e-01,3.84660583e-01
 , -2.00063941e-01, -1.28405690e-01, -1.39264809e-02,2.05764984e-01]

features = ["totpop-log","medhhincome-log","medhvalue-log","male","age_under18","age_18_24","age_25_34","age_35_44","age_45_54","age_55_64","age_65_74","age_75_84","age_85pl","race_white","race_black","race_nativeam","race_asian","married","divorced","educ_lesshs","educ_somecoll","educ_college","educ_collpl","urate_all","urate_male","urate_female","HSdropout_male","HSdropout_female","ind_agmining","ind_const","ind_manuf","ind_wholesale","ind_retail","ind_transport","ind_info","ind_FIRE","ind_pro","ind_educhealth","ind_artentertain","ind_otherserve","ind_public","occ_mgmtbiz","occ_pro","occ_healthsupp","occ_protective","occ_food","occ_building","occ_personalcare","occ_sales","occ_officeadmin","occ_farming","occ_constextract","occ_production","occ_transport","income_less10k","income_10k15","income_15k20","income_20k25","income_25k30","income_30k35","income_35k40","income_40k45","income_45k50","income_50k60","income_60k75","income_75k100","income_100k125","income_125k150","income_150kpl","rent_share_income","poverty_under18","poverty_18_64","poverty_65pl","poverty_white","poverty_black","poverty_nativeA","vetshare_18_64","vetshare_65pl","Num-Services","Avg-Satisfaction"]

print(params)
print(len(params))
print(features)
print(len(features))

data = []
for i in range(len(features)):
    if params[i] < 0:
        cur = (-params[i], features[i], '-')
    else:
        cur = (params[i], features[i], '+')
    data.append(cur)


data.sort(key= lambda x: x[0], reverse=True)
print(data)