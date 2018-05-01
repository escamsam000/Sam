import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

df = pd.read_csv(filepath_or_buffer='/Users/escamsam000/Desktop/Exercise Files/Ch05/05_03/iris.data.csv',
                 header=None, sep=',')

df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Species']
data = df.ix[:, 0:4].values
target = df.ix[:, 4].values
# print(df[:5])

model = DBSCAN(eps=0.8, min_samples=19).fit(data)
# print(model)

outliers_df = pd.DataFrame(data)

# print(Counter(model.labels_))

# print(outliers_df[model.labels_ == -1])

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])

colors = model.labels_

ax.scatter(data[:, 2], data[:, 1], c=colors, s=120)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBScan for Outlier Detection')
plt.show()
