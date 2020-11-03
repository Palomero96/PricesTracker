from app import app
from datetime import date
from dash_bootstrap_components import Container
from dash_html_components import H1
from dash_html_components import H4
from dash_html_components import Button
from dash.dependencies import Input as DInput
from dash.dependencies import Output as DOutput
from dotmap import DotMap as dot
import pandas as pd
import numpy as np
import plotly.express as px
import dash_core_components as dcc
from dash.dash import no_update

selected   = dot({
    'date':         None,
    'shop':         None,
    'kind':         None
})
__prices_file = 'csv/prices.csv'

prices_df = pd.read_csv(__prices_file)

productOptions= prices_df.kind.unique()
productOptions = np.append(productOptions, ['All'])
dates = prices_df.date.unique()
shops = prices_df.shop.unique()
shops = np.append(shops, ["All"])



#TODO:
#Dropdown limit

today = date.today().strftime("%Y-%m-%d")
prices_today = prices_df[prices_df['date']==today]
fig = px.bar(prices_today, x='name', y='price',title="Product Prices")

bars_page = [
    Container([
      H1('Bar plot'),
      H4('Select Date'),
      dcc.Dropdown(
        id='dateDropdown',
        options=[{'label': i, 'value': i} for i in dates],
        value=[i for i in dates]),
        
      H4('Select shop'),
      dcc.Dropdown(
        id='shopDropdown',
        options=[{'label': i, 'value': i} for i in shops],
        value=[i for i in shops]),

    H4('Select type of product'),
      dcc.Dropdown(
        id='productDropdown',
        ),
    Button('Reload', id='loadButton', n_clicks=0),
    dcc.Graph(
        id='graph',
        figure=fig
    )
        
    ],
    id='app-main-bars')
 ]


@app.callback(DOutput('productDropdown', 'options'),
              DInput('shopDropdown', 'value'))

def changeProductDropdown(shopDropdown):
  prices_df = pd.read_csv(__prices_file)
  if shopDropdown=="All":
    aux=prices_df['kind'].unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options
  else:
    
    filter_prices_df = prices_df[prices_df["shop"]==shopDropdown]
    aux = filter_prices_df['kind'].unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options
  


@app.callback(DOutput('loadButton', 'disabled'),
              [DInput('productDropdown', 'value'),
              DInput('dateDropdown', 'value'),
              DInput('shopDropdown', 'value')])

def changeLoadButton(productDropdown, dateDropdown,shopDropdown):
    selected.date=dateDropdown
    selected.shop=shopDropdown
    selected.kind=productDropdown

    if productDropdown is None or dateDropdown is None or shopDropdown is None:
        return True
    else:
        return False
    


@app.callback(DOutput("graph", "figure"),
              DInput("loadButton","n_clicks"))  

def display_bar(n_clicks):
  # Don't trigger update on page load
    if n_clicks == 0:
        return no_update
    prices_df = pd.read_csv(__prices_file)
    prices_df = prices_df[prices_df["date"]==selected.date]

    if(selected.kind!="All"):
      prices_df =prices_df[prices_df["kind"]==selected.kind]
      
    if(selected.shop!="All"):
      prices_df = prices_df[prices_df["shop"]==selected.shop]

    fig = px.bar(prices_df, x='name', y='price',color="shop", title="Product Prices")
    return fig
