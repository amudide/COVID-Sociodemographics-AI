import pandas as pd
import numpy as np

params = [4.16638082e-01,-5.67132366e-02,4.86070028e+00,-9.51154870e+00,4.92164245e+00,5.63181471e+00,-3.99187630e+00,4.79713214e+00,-6.63974599e-01,-6.92523098e+00,8.47715207e+00,-7.43555758e+00,-8.98145081e+00,1.17287401e+01,-8.23233210e+00,-7.80469752e+00,2.82578495e+00,-4.38657375e+00,5.35600979e+00,-9.91335683e-03,1.73307100e+00,-1.42877285e-02,6.49035849e-01]

features = ["totpop-log", "medhvalue-log", "age_under18", "age_55_64", "race_black", "race_nativeA", "race_asian", "educ_lesshs", "educ_somecoll", "urate_male", "HSdropout_male", "ind_agmining", "ind_transport", "ind_pro", "ind-public", "occ_transport", "income_150kpl", "poverty_18_64", "poverty_65pl", "poverty_black", "poverty_nativeA", "Num-Services", "Avg-Satisfaction"]

print(len(params))
print(len(features))

data = []
for i in range(len(params)):
    if params[i] < 0:
        cur = (-params[i], features[i], '-')
    else:
        cur = (params[i], features[i], '+')
    data.append(cur)

data.sort(key= lambda x: x[0], reverse=True)
print(data)