from app import app
from dash_bootstrap_components import Container
from dash.exceptions import PreventUpdate
from dash_html_components import H1
from dash_html_components import H4
from dash_html_components import P
from dash_html_components import Button
from dash.dependencies import Input as DInput
from dash.dependencies import Output as DOutput
from dotmap import DotMap as dot
import plotly.express as px
import pandas as pd
from dash.dash import no_update

import dash_core_components as dcc

__prices_file = 'csv/prices.csv'

prices_df = pd.read_csv(__prices_file)
names = prices_df["name"].unique()
names=names[1:20]

shops = prices_df.shop.unique()

selected   = dot({
    'shop':         None,
    'kind':         None
})
#TODO:
#Dropdown limit
#Shop dropdown?
#Line
evolution_page = [
    Container([
    H1('Evolution'),
    H4('Select product'),
    P("Shop"),
    dcc.Dropdown(
        id='shopEvo',
        options=[{'label': i, 'value': i} for i in shops],
        value=[i for i in shops],
        placeholder="Shop"),
    P("Kind"),
      dcc.Dropdown(
        id='productEvo',
        ),
    Button("Load Products", id="LoadNamesEvo", n_clicks=0),
    P("Product name"),
    dcc.Dropdown(
        id='evolutionDropdown',),
    
    dcc.Graph(
        id="evolutionGraph"
    )
    ],
    id='app-main-evolution')
 ]

@app.callback(DOutput("LoadNamesEvo", "disabled"),
                [DInput("shopEvo","value"),
                DInput("productEvo","value")])

def changeLoadButton(valueOne, valueTwo):
    selected.shop=valueOne
    selected.kind=valueTwo
    if selected.shop is None or selected.kind is None:
        return True
    else:
        return False
#Update Product Dropdown
@app.callback(DOutput('productEvo', 'options'),
              DInput('shopEvo', 'value'))

def changeProductDropdownEvo(shopDropdown):
    prices_df = pd.read_csv(__prices_file)
    filter_prices_df = prices_df[prices_df["shop"]==shopDropdown]
    aux = filter_prices_df['kind'].unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options  

#Update load names Button
@app.callback(DOutput("evolutionDropdown", "options"),
                DInput("LoadNamesEvo","n_clicks"))

def changeNameDropdownEvo(n_clicks):
    # Don't trigger update on page load
    if n_clicks == 0:
        return no_update
    prices_df = pd.read_csv(__prices_file)
    filter_prices_df = prices_df[prices_df["shop"]==selected.shop]
    filter_prices_df = filter_prices_df[filter_prices_df["kind"]==selected.kind]
    aux = filter_prices_df.name.unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options




#Update Evolution Graph
@app.callback(DOutput("evolutionGraph", "figure"),
                DInput("evolutionDropdown","value"))

def display_evolutionGraph(value):
    filter_prices_df = prices_df[prices_df["name"]==value]
    #fig = px.bar(prices_df, x='name', y='price',color="shop",title="Product Prices")
    fig = px.scatter(filter_prices_df, x="date", y="price", color="shop",
                 title="Price Evolution",
                )
    #fig = px.line(filter_prices_df, x="date", y="price", color="shop",title="Price Evolution",)
    return fig
