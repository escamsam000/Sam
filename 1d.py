import numpy as np
import pandas as pd

from pandas import Series, DataFrame

DF_obj = pd.DataFrame(np.arange(36).reshape(6, 6))

DF_obj2 = pd.DataFrame(np.arange(15).reshape(5, 3))


series_obj = Series(np.arange(6))
series_obj.name = 'added_variable'

variable_added = DataFrame.join(DF_obj, series_obj)
added_datatable = variable_added.append(variable_added, ignore_index=True)

DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
print(DF_sorted)
