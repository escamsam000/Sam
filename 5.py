import numpy as np
import pandas as pd

import cufflinks as cf

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

import sklearn
from sklearn.preprocessing import StandardScaler

tls.set_credentials_file(username='escamsam000', api_key='VLsKstyWVZ8UwvtWSYxB')

address = '/Users/escamsam000/Desktop/Exercise Files/Ch03/03_06/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp',
                'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg

cars_data = cars.ix[:, (1, 3, 4)].values

cars_data_std = StandardScaler().fit_transform(cars_data)

cars_select = pd.DataFrame(cars_data_std)
cars_select.columns = ['mpg', 'disp', 'hp']

cars_select.iplot(kind='box', filename='box-plots')
fig = {'data': [{'x': cars_select.mpg, 'y': cars_select.disp, 'mode': 'markers', 'name': 'mpg'},
                {'x': cars_select.hp, 'y': cars_select.disp, 'mode': 'markers', 'name': 'hp'}],
       'layout': {'xaxis': {'title': ''}, 'yaxis': {'title': 'Standardized Displacement'}}}
py.iplot(fig, filename='grouped-scatter-plot')
