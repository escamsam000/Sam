import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr

rcParams['figure.figsize'] = 8, 4
plt.style.use('seaborn-whitegrid')

address = '/Users/escamsam000/Desktop/Exercise Files/Ch03/03_04/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
# sb.pairplot(cars)
# plt.show()

X = cars[['mpg', 'hp', 'qsec', 'wt']]
# sb.pairplot(X)
# plt.show()

mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']

pearsonr_coefficient, p_value = pearsonr(mpg, hp)
print('PearsonR Correlation Coefficient %0.3f' % pearsonr_coefficient)

pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print('PearsonR Correlation Coefficient %0.3f' % pearsonr_coefficient)

pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print('PearsonR Correlation Coefficient %0.3f' % pearsonr_coefficient)

corr = X.corr()
print(corr)

sb.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
