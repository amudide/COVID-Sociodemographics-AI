import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_tmp = [(14.79958071, 'age_55_64', '-'), (10.12717474, 'ind_pro', '+'), (9.56676634, 'occ_sales', '+'), (9.46650696, 'poverty_65pl', '+'), (8.24240185, 'urate_male', '-'), (7.68787764, 'ind_const', '+'), (7.30433173, 'ind_agmining', '-'), (6.25936549, 'ind_educhealth', '-'), (4.74678917, 'educ_collpl', '-'), (4.6610742, 'race_black', '+')]
data = [(14.79958071, 'Population Ages 55-64', '-'), (10.12717474, 'Population Industry Prof-Services', '+'), (9.56676634, 'Population Occupation Sales', '+'), (9.46650696, 'Population Poverty Age 65+', '+'), (8.24240185, 'Population Male Unemployment', '-'), (7.68787764, 'Population Industry Construction', '+'), (7.30433173, 'Population Industry Agric./Mining', '-'), (6.25936549, 'Population Industry Educ./Health', '-'), (4.74678917, 'Population Education College+', '-'), (4.6610742, 'Population Race Black', '+')]


# height = [3, 12, 5, 18, 45]
# bars = ('A', 'B', 'C', 'D', 'E')

height = [item[0] for item in data]
height.reverse()
bars = [item[1] for item in data]
bars.reverse()

y_pos = np.arange(len(bars))

# print(y_pos)

# Create horizontal bars
plt.barh(y_pos, height)
 
# Create names on the y-axis
plt.yticks(y_pos, bars)

plt.title('Predicting log cases with Lasso + Ridge Regression: Top 10 Features')
plt.xlabel('Parameter Weight Magnitude')
plt.ylabel('Feature')
 
# Show graphic
plt.show()
