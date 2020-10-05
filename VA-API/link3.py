import pandas as pd
import numpy as np

df = pd.read_csv("fips-vanilla-cases-link2.csv")
data = df.values.tolist()

mp = {}

counter = 0
ndata = []
for entry in data:
    cur = entry[:]

    if not np.isnan(cur[6]):
        mp[cur[1]] = cur[6:]

print(mp)
print("size: ", len(mp))

ndata = []
for entry in data:
    cur = entry[:]

    if cur[1] in mp:
        cur[6:] = mp[cur[1]]
    #print(cur)
    ndata.append(cur)

# counter stores number of successful queries in the vacovidsummary-new.csv file
#print("counter", counter)
final_data = pd.DataFrame(ndata, columns=["VA Station Number","HCS","Address","City","State","County FIPS","Cases","Active","Convalescent","Deaths"])
final_data.to_csv('fips-cases-final.csv', index=False)