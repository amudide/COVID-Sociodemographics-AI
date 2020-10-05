# counts the number of distinct case 4-tuples in the countyfips_cases.csv file

import pandas as pd
import numpy

df = pd.read_csv("countyfips_cases.csv")

df1 = df[['Total','Active','Convalescent','Deaths']]
df_list = df1.values.tolist()

unique_centers = set()

n = len(df_list)
for i in range(n):
    if not numpy.isnan(df_list[i][0]):
        print(df_list[i])
        unique_centers.add(tuple(df_list[i]))
        if (df_list[i] == [1046,3,927,11]):
            print('hoorah')

print(len(unique_centers))
