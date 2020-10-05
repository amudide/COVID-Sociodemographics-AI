# logs non-share data

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

df['totpop'] = np.log2(df["totpop"] + 1)
df['medhhincome'] = np.log2(df["medhhincome"] + 1)
df['medhvalue'] = np.log2(df["medhvalue"] + 1)

df.to_csv('data.csv', index=False)