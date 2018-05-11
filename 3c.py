import numpy
import pandas as pd

address = '/Users/escamsam000/Desktop/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names

carb = cars.carb

cars_cat = cars[['cyl', 'vs', 'am', 'gear', 'carb']]

gears_group = cars_cat.groupby('gear')

cars['group'] = pd.Series(cars.gear, dtype='category')

print(pd.crosstab(cars['am'], cars['gear']))
