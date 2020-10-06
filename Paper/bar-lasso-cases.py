import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_tmp = [(14.79958071, 'age_55_64', '-'), (10.12717474, 'ind_pro', '+'), (9.56676634, 'occ_sales', '+'), (9.46650696, 'poverty_65pl', '+'), (8.24240185, 'urate_male', '-'), (7.68787764, 'ind_const', '+'), (7.30433173, 'ind_agmining', '-'), (6.25936549, 'ind_educhealth', '-'), (4.74678917, 'educ_collpl', '-'), (4.6610742, 'race_black', '+')]
data = [(14.79958071, 'Population Ages 55-64', '-'), (10.12717474, 'Population Industry Prof-Services', '+'), (9.56676634, 'Population Occupation Sales', '+'), (9.46650696, 'Population Poverty Age 65+', '+'), (8.24240185, 'Population Male Unemployment', '-'), (7.68787764, 'Population Industry Construction', '+'), (7.30433173, 'Population Industry Agric./Mining', '-'), (6.25936549, 'Population Industry Educ./Health', '-'), (4.74678917, 'Population Education College+', '-'), (4.6610742, 'Population Race Black', '+')]


# height = [3, 12, 5, 18, 45]
# bars = ('A', 'B', 'C', 'D', 'E')

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16
FIG_SIZE = 18


plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=16)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=20)  # fontsize of the figure title
plt.rc('axes', titlesize=20)     # fontsize of the axes title


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
