from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-provinces.geojson') as response:
    provinces = json.load(response)

import pandas as pd
df = pd.read_csv('../data/cum.csv', dtype={'postal': str})

import plotly
import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=provinces, locations='postal', color='positive', featureidkey = 'properties.cod_prov',
                           color_continuous_scale="brwnyl",
                           range_color=(4101, 453683),
                           mapbox_style="carto-positron",
                           zoom=6,
                           center = {"lat": 40, "lon": -4},
                           opacity=0.5,
                           labels={'positive':'Total cases', 'postal':'Postal code'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

plotly.offline.plot(fig, filename='../plots/map_cum_positive.html')
