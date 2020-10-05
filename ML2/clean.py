# delete hcs with empty cases

import pandas as pd
import numpy as np

df = pd.read_csv("data-imp2-adj.csv")

df = (df.loc[(np.isnan(df['Cases']) == False)])

df.to_csv("data-cleaned.csv", index=False)