# removes columns that I don't need from fips_and_cases_deaths.csv

import pandas as pd

df = pd.read_csv("fips_and_cases_deaths.csv")

df1 = df[['VA Station Number', 'Address', 'City', 'State', 'County FIPS', 'VA Confirmed Total_Display', 'Active', 'Convalescent', 'Known Deaths']]
df1.to_csv("countyfips_cases.csv", index=False)