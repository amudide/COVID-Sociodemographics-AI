import pandas as pd

df = pd.read_csv("fips.csv")

df2 = pd.read_csv("vacovid19summary.csv")

data = df.values.tolist()

print(data[0][2:4])

counter = 0
ndata = []
for entry in data:
    cur = entry
    city = entry[2]
    state = entry[3]
    searchstring = city + ", " + state + " HCS"
    print(searchstring)
    df3 = (df2.loc[df2['Facility'] == searchstring])
    dflist = df3.values.tolist()
    print(dflist)
    print(len(dflist))
    if (len(dflist) != 0 and len(dflist) != 1):
        print("Error!")
        break

    if (len(dflist) == 1):
        cur.append(dflist[0][1])
        cur.append(dflist[0][2])
        cur.append(dflist[0][3])
        cur.append(dflist[0][4])
        print(cur)
        counter += 1

    ndata.append(cur)

print(counter)
final_data = pd.DataFrame(ndata, columns=["VA Station Number","Address","City","State","Zip","Latitude","Longitude","Accuracy Score","Accuracy Type","Number","Street","Unit Type","Unit Number","City","State","County","Zip","Country","Source","Census Year","State FIPS","County FIPS","Place Name","Place FIPS","Census Tract Code","Census Block Code","Census Block Group","Full FIPS","Metro/Micro Statistical Area Name","Metro/Micro Statistical Area Code","Metro/Micro Statistical Area Type","Combined Statistical Area Name","Combined Statistical Area Code","Metropolitan Division Area Name","Metropolitan Division Area Code", "VA Confirmed Total_Display","Active","Convalescent","Known Deaths"])
final_data.to_csv('fips_and_cases_deaths.csv', index=False)

