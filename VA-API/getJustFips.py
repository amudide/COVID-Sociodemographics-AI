# removes columns that I don't need from fips.csv

import pandas as pd

df = pd.read_csv("fips.csv")

df1 = df[['VA Station Number', 'Address', 'City', 'State', 'County FIPS']]
df1.to_csv("fips-vanilla.csv", index=False)