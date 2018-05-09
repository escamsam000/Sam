import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

address = '/Users/escamsam000/Desktop/Exercise Files/Ch02/02_06/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names
mpg = cars['mpg']

mpg.plot(kind='hist')
plt.show()

plt.hist(mpg)
plt.plot()
plt.show()

sb.distplot(mpg)
plt.show()

cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgrey'], s=150)
plt.show()

sb.regplot(x='hp', y='mpg', data=cars, scatter=True)
plt.show()

# cars_df = pd.DataFrame(cars.ix[:, (1, 3, 4, 6)].values, columns=['mpg', 'disp', 'hp', 'wt'])
# cars_target = cars.ix[:, 9].values
# target_names = [0, 1]

# cars_df['group'] = pd.Series(cars_target, dtype="category")
# sb.pairplot(cars_df, hue='group', palette='hls')
# plt.show()

cars.boxplot(column='mpg', by='am')
plt.show()
cars.boxplot(column='wt', by='am')
plt.show()

sb.boxplot(x='am', y='mpg', data=cars, palette='hls')
plt.show()
