# Create a line chart to display the data

import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output

app = Dash()

df = pd.read_csv('formattedDataset.csv')

# Create graph and vertial line
fig = px.line(df, x='date', y='sales',
              title='Pink Morsel Sales By Region', color='region')
fig.add_vline(x='2021-01-15', line_width=3,
              # to add once fixed : annotation_text='Jan 15th 2021', annotation_position='bottom right'
              line_dash='dash', line_color='green')

# App HTML
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales By Region'),
    html.H2(children='Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?'),

    dcc.Graph(
        id='Sales Graph',
        figure=fig
    ),
    html.Div(
        [
            html.P('Select a Region'),
            dcc.RadioItems(
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'},
                ],
                value='all',
                id='radio-options',
                labelClassName='label_option',
                inputClassName='input_option',
                className='radio-container'
            )
        ]
    )
])

# Interactivity

# Callback to update the graph


@app.callback(
    Output('Sales Graph', 'figure'),
    Input('radio-options', 'value')
)
def updateGraph(region):
    # filtering the df based on region selected
    if region == 'all':
        dff = df.copy()
    else:
        # changing the df to only include the selected region
        dff = df[df['region'].str.lower() == region]

    # rebuild chart
    fig = px.line(dff, x='date', y='sales',
                  color='region')
    fig.add_vline(x='2021-01-15', line_width=3,
                  # to add once fixed : annotation_text='Jan 15th 2021', annotation_position='bottom right'
                  line_dash='dash', line_color='green')

    return fig


app.run(debug=True)
