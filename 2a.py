import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

address = '/Users/escamsam000/Desktop/Exercise Files/Ch02/02_01/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars['mpg']

df = cars[['cyl', 'wt', 'mpg']]

xx = [1, 2, 3, 4, 0.5]
plt.pie(xx)
plt.show()
