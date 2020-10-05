# imputes data

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

numserv = df['Num-Services'].values.tolist()
sum1 = 0
count1 = 0
for num in numserv:
    if num != 0:
        count1 += 1
    sum1 += num
avg1 = sum1 / count1
#print(avg1)
for i in range(len(numserv)):
    if (numserv[i] == 0):
        numserv[i] = avg1

#print(numserv)

df['Num-Services'] = numserv
#print(df['Num-Services'])



satis = df['Avg-Satisfaction'].values.tolist()
sum2 = 0
count2 = 0
for num in satis:
    if not np.isnan(num):
        count2 += 1
        sum2 += num
avg2 = sum2 / count2
#print(avg2)
#print(satis)
for i in range(len(satis)):
    if (np.isnan(satis[i])):
        satis[i] = avg2

#print(satis)

df['Avg-Satisfaction'] = satis
#print(df['Avg-Satisfaction'])


df.to_csv('data-imputed.csv', index=False)