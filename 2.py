import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

address = '/Users/escamsam000/Desktop/Exercise Files/Ch03/03_06/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg

mpg_matrix = mpg.reshape(-1, 1)
scaled = preprocessing.MinMaxScaler(feature_range=(0, 10))
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
plt.show()
