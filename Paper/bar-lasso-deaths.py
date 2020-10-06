import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_tmp = [(11.7287401, 'ind_pro', '+'), (9.5115487, 'age_55_64', '-'), (8.98145081, 'ind_transport', '-'), (8.47715207, 'HSdropout_male', '+'), (8.2323321, 'ind-public', '-'), (7.80469752, 'occ_transport', '-'), (7.43555758, 'ind_agmining', '-'), (6.92523098, 'urate_male', '-'), (5.63181471, 'race_nativeA', '+'), (5.35600979, 'poverty_65pl', '+')]
data = [(11.7287401, 'Population Industry Prof-Services', '+'), (9.5115487, 'Population Ages 55-64', '-'), (8.98145081, 'Population Industry Transport', '-'), (8.47715207, 'Population Male HS Dropout', '+'), (8.2323321, 'Population Industry Public Adm.', '-'), (7.80469752, 'Population Occupation Transport', '-'), (7.43555758, 'Population Industry Agric./Mining', '-'), (6.92523098, 'Population Male Unemployment', '-'), (5.63181471, 'Population Race Native Amer.', '+'), (5.35600979, 'Population Poverty Age 65+', '+')]

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

plt.title('Predicting log deaths with Lasso + Ridge Regression: Top 10 Features')
plt.xlabel('Parameter Weight Magnitude')
plt.ylabel('Feature')
 
# Show graphic
plt.show()