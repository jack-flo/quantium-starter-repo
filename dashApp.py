# Create a line chart to display the data

import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

app = Dash()

df = pd.read_csv('formattedDataset.csv')

fig = px.line(df, x='date', y='sales',
              title='Pink Morsel Sales By Region', color='region')
fig.add_vline(x='2021-01-15', line_width=3,
              # to add once fixed : annotation_text='Jan 15th 2021', annotation_position='bottom right'
              line_dash='dash', line_color='green')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales By Region'),

    html.Div(children='''
        Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

app.run(debug=True)
