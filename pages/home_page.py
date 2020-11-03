from app import app
from dash_bootstrap_components import Container
from dash_html_components import H1
from dash.dependencies import Input as DInput
from dash.dependencies import Output as DOutput
from dotmap import DotMap as dot
import pandas as pd

import dash_core_components as dcc

__prices_file = 'csv/prices.csv'

prices_df = pd.read_csv(__prices_file)
dates= prices_df.name.unique()
home_page = [
    Container([
      H1('Home'),
      dcc.Dropdown(
        id='dateDropdown',
        options=[{'label': i, 'value': i} for i in dates],
        value=[i for i in dates]),
    ],
    id='app-main-home')
 ]
