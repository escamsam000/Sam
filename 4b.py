import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams

import pandas as pd
import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

iris = datasets.load_iris()
X = iris.data
variable_names = iris.feature_names

pca = decomposition.PCA()
iris_pca = pca.fit_transform(X)

print(pca.explained_variance_ratio_.sum())

comps = pd.DataFrame(pca.components_, columns=variable_names)
sb.heatmap(comps)
plt.show()
