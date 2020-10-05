import pandas as pd

df = pd.read_csv("fips-vanilla.csv")
df2 = pd.read_csv("vacovidsummary-new.csv")
data = df.values.tolist()

counter = 0
ndata = []
for entry in data:
    cur = entry[:]
    station_va = entry[0][4:7]
    cur.insert(1, station_va)

    city = entry[2]
    state = entry[3]
    searchstring = city + ", " + state + " HCS"
    #print(searchstring)

    df3 = (df2.loc[df2['Facility'] == searchstring])
    dflist = df3.values.tolist()
    #print(dflist)

    if (len(dflist) != 0 and len(dflist) != 1):
        print("Error!")
        break

    if (len(dflist) == 1):
        cur.append(dflist[0][1])
        cur.append(dflist[0][2])
        cur.append(dflist[0][3])
        cur.append(dflist[0][4])
        counter += 1

    #print(cur)
    ndata.append(cur)

# counter stores number of successful queries in the vacovidsummary-new.csv file
print("counter", counter)
final_data = pd.DataFrame(ndata, columns=["VA Station Number","HCS","Address","City","State","County FIPS","Cases","Active","Convalescent","Deaths"])
final_data.to_csv('fips-vanilla-cases-link2.csv', index=False)