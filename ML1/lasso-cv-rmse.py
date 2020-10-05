# Ridge regression. Performs cross-validaio

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel

df = pd.read_csv("data-agg.csv")

X = (df[["totpop-log","medhhincome-log","medhvalue-log","male","age_under18","age_18_24","age_25_34","age_35_44","age_45_54","age_55_64","age_65_74","age_75_84","age_85pl","race_white","race_black","race_nativeam","race_asian","married","divorced","educ_lesshs","educ_somecoll","educ_college","educ_collpl","urate_all","urate_male","urate_female","HSdropout_male","HSdropout_female","ind_agmining","ind_const","ind_manuf","ind_wholesale","ind_retail","ind_transport","ind_info","ind_FIRE","ind_pro","ind_educhealth","ind_artentertain","ind_otherserve","ind_public","occ_mgmtbiz","occ_pro","occ_healthsupp","occ_protective","occ_food","occ_building","occ_personalcare","occ_sales","occ_officeadmin","occ_farming","occ_constextract","occ_production","occ_transport","income_less10k","income_10k15","income_15k20","income_20k25","income_25k30","income_30k35","income_35k40","income_40k45","income_45k50","income_50k60","income_60k75","income_75k100","income_100k125","income_125k150","income_150kpl","rent_share_income","poverty_under18","poverty_18_64","poverty_65pl","poverty_white","poverty_black","poverty_nativeA","vetshare_18_64","vetshare_65pl","Num-Services","Avg-Satisfaction"]]).values.tolist()
y1 = (df[['Log-Cases']]).values.tolist()
y2 = (df[['Log-Deaths']]).values.tolist()

print("Initial dimensions:")
dim1X = len(X)
dim2X = len(X[0])
print("rows:",dim1X,". columns:",dim2X,"\n")

lasso1 = linear_model.Lasso(alpha=0.001).fit(X, y1)
model1 = SelectFromModel(lasso1, prefit=True)
X_new = model1.transform(X)

dim1X = len(X_new)
dim2X = len(X_new[0])
print("\nNew dimensions for cases:")
print("rows:",dim1X,". columns:",dim2X)

print("New Data")
print(X_new[0])

reg1 = linear_model.RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1, 1e1, 1e2, 1e3], cv=5, scoring="neg_mean_absolute_error")
reg1.fit(X_new, y1)

print("\n\n LOG CASES \n\n")
print("R^2 Score:", reg1.score(X_new, y1))
print("Parameters:", reg1.coef_)
print("Intercept:", reg1.intercept_)
print("Best Alpha:", reg1.alpha_)
print("CV Score:", reg1.best_score_)


lasso2 = linear_model.Lasso(alpha=0.001).fit(X, y2)
model2 = SelectFromModel(lasso2, prefit=True)
X_new = model2.transform(X)

dim1X = len(X_new)
dim2X = len(X_new[0])
print("\n\nNew dimensions for deaths:")
print("rows:",dim1X,". columns:",dim2X)

print("New Data")
print(X_new[0])


reg2 = linear_model.RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1, 1e1, 1e2, 1e3], cv=5, scoring="neg_mean_absolute_error")
reg2.fit(X_new, y2)

print("\n\n LOG DEATHS \n\n")
print("R^2 Score:", reg2.score(X_new, y2))
print("Parameters:", reg2.coef_)
print("Intercept:", reg2.intercept_)
print("Best Alpha:", reg2.alpha_)
print("CV Score:", reg2.best_score_)