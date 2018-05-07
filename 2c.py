import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams

import seaborn as sb

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, 0.5, 4, 3, 2, 1]
plt.bar(x, y)
plt.show()

wide = [0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.5, 0.5, 0.5]
color = ['salmon']
plt.bar(x, y, width=wide, color=color, align='center')
plt.show()

address = '/Users/escamsam000/Desktop/Exercise Files/Ch02/02_03/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'mpg', 'wt']]
color_theme = ['darkgrey', 'lightsalmon', 'powderblue']
df.plot(color=color_theme)
plt.show()

z = [1, 2, 3, 4, 0.5]
ct = ['#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
plt.pie(z, colors=ct)
plt.show()

x1 = range(0, 10)
y1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.plot(x, y)
plt.plot(x1, y1)
plt.show()

plt.plot(x, y, ls='steps', lw=5)
plt.plot(x1, y1, ls='--', lw=10)
plt.show()

plt.plot(x, y, marker='1', mew=20)
plt.plot(x1, y1, marker='+', mew=15)
plt.show()
