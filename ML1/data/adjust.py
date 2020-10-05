# imputes data

import pandas as pd
import numpy as np

df = pd.read_csv("data-imputed.csv")

fipscodes = df['County FIPS'].values.tolist()
mp = {}
for code in fipscodes:
    if code in mp:
        mp[code] += 1
    else:
        mp[code] = 1

#print(mp)

vetpops = df['vetpop'].values.tolist()

#print(len(vetpops))
#print(len(fipscodes))

for i in range(len(fipscodes)):
    vetpops[i] = round(vetpops[i] / mp[fipscodes[i]])

#print(vetpops)

df['vetpop-adj'] = vetpops
#print(df)

df.to_csv('data-imp-adj.csv', index=False)