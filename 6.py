import numpy as np
import pandas as pd

import plotly.plotly as py
import plotly.tools as tls

tls.set_credentials_file(username='escamsam000', api_key='oK1bf48TasO9a6Fhl1AY')

address = '/Users/escamsam000/Desktop/Exercise Files/Ch09/09_04/snow_inventory.csv'
snow = pd.read_csv(address)
snow.columns = ['stn_id', 'lat', 'long', 'elev', 'code']

snow_sample = snow.sample(n=200, random_state=25, axis=0)


data = [dict(type='scattergeo', locationmode='USA-states', lon=snow_sample['long'],
             lat=snow_sample['lat'], marker=dict(size=12, autocolorscale=False,
                                                 colorscale='custom-colorscale',
                                                 color=snow_sample['elev'],
                                                 colorbar=dict(title='Elevation (m)')))]

layout = dict(title='NOAA Weather Snowfall Station Elevations', colorbar=True,
              geo=dict(scope='usa', projection=dict(type='albers usa'), showland=True,
                       landcolor="rgb(250,250,250)", subunitcolor="rgb(217,217,217)",
                       countrycolor="rgb(217,217,217)",
                       countrywidth=0.5, subunitwidth=0.5),)

fig = dict(data=data, layout=layout)

py.iplot(fig, validate=False, filename='d3-elevation')
