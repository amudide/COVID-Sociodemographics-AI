# adds vet-pop to data.csv

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

df['vetpop'] = round(df['totpop'] * ((df['vetshare_18_64'] * (df['age_18_24'] + df['age_25_34'] + df['age_35_44'] + df['age_45_54'] + df['age_55_64'])) + (df['vetshare_65pl'] * (df['age_65_74'] + df['age_75_84'] + df['age_85pl']))))

df.to_csv('data.csv', index=False)