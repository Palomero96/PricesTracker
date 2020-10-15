from app import app
from dash_bootstrap_components import Container
from dash_html_components import H1
from dotmap import DotMap as dot
import pandas as pd
import dash_table
import datetime as date


__prices_file = 'csv/prices.csv'

prices_df = pd.read_csv(__prices_file)


table_page =  [
    Container([
      H1('Table'),
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
    }
)
    ],
    id='app-main-table')
  ]
