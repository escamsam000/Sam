import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

url = 'https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/mtcars.csv'
cars = pd.read_csv(url)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg

gear = cars.gear

print(cars.describe())
