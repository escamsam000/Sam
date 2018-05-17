import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 5, 4

df = pd.read_csv(
    filepath_or_buffer='/Users/escamsam000/Desktop/Exercise Files/Ch05/05_01/iris.data.csv',
    header=None, sep=',')
df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length',
              'Petal Width', 'Species']
x = df.ix[:, 0:4].values
y = df.ix[:, 4].values
# print(df[:5])

df.boxplot(return_type='dict')
plt.plot()
# plt.show()

Sepal_Width = x[:, 1]
iris_outliers = (Sepal_Width > 4)
print(df[iris_outliers])
print("")
iris_outliers = (Sepal_Width < 2.05)
print(df[iris_outliers])
print("")
pd.options.display.float_format = '{:.1f}'.format
x_df = pd.DataFrame(x)
print(x_df.describe())
