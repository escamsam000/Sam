import numpy as np
import pandas as pd

from pandas import Series, DataFrame

missing = np.nan

series_obj = Series(['row 1', 'row 2', missing, 'row 4',
                     'row 5', 'row 6', missing, 'row 8'])

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6, 6))

DF_obj.ix[3:5, 0] = missing
DF_obj.ix[1:4, 5] = missing

filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})

fill_DF = DF_obj.fillna(method='ffill')

DF_no_NaN = DF_obj.dropna(axis=1)
print(DF_obj.dropna(how='all'))

