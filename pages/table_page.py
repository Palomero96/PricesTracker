from app import app
from dash_bootstrap_components import Container
from dash_html_components import H1
from dash_html_components import H4
from dash.dependencies import Input as DInput
from dash.dependencies import Output as DOutput
from dotmap import DotMap as dot
import pandas as pd
import dash_table
import datetime as date
import dash_core_components as dcc

__prices_file = 'csv/prices.csv'

prices_df = pd.read_csv(__prices_file)
productOptions= prices_df.kind.unique()

table_page =  [
    Container([
      H1('Table'),
      H4('Select type of product'),
        dcc.Dropdown(
        id='productDropdown',
        options=[{'label': i, 'value': i} for i in productOptions],
        value=[i for i in productOptions]),
      dash_table.DataTable(
    columns=[
        {'name': 'Name', 'id': 'name', 'type': 'text'},
        {'name': 'Kind', 'id': 'kind', 'type': 'text'},
        {'name': 'Shop', 'id': 'shop', 'type': 'text'},
        {'name': 'Url', 'id': 'url', 'type': 'text'},
        {'name': 'Price', 'id': 'price', 'type': 'numeric'},
        {'name': 'Date', 'id': 'date', 'type': 'datetime'}
    ],
    data=prices_df.to_dict('records'),
    filter_action='native',
    sort_action='native',
    sort_mode='multi',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },
    id="table"
)
    ],
    id='app-main-table')
  ]

@app.callback(DOutput('table', 'data'),
              [DInput('productDropdown', 'value')])
def display_table(value):
    filter_prices_df = prices_df[prices_df["kind"]==value]
    return filter_prices_df.to_dict("records")