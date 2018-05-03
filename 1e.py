import numpy as np
import pandas as pd

from pandas import Series, DataFrame

address = '/Users/escamsam000/Desktop/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)

cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

cars_groups = cars.groupby(cars['cyl'])
print(cars_groups.mean())
