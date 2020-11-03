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

#TODO:
#Dropdown limit
#Shop dropdown?

selected   = dot({
    'One':         None,
    'Two':         None
})
selectedOne   = dot({
    'shop':         None,
    'kind':         None
})
selectedTwo   = dot({
    'shop':         None,
    'kind':         None
})

__prices_file = 'csv/prices.csv'

prices_df = pd.read_csv(__prices_file)
names = prices_df["name"].unique()
shops = prices_df.shop.unique()

comp_page = [
    Container([
    H1('Comparator'),
    #First Product
    H4('Select first product'),
    P("Shop"),
    dcc.Dropdown(
        id='shopCompOne',
        options=[{'label': i, 'value': i} for i in shops],
        value=[i for i in shops],
        placeholder="Shop"),
    P("Kind"),
      dcc.Dropdown(
        id='productCompOne',
        ),
    Button("Load Products", id="LoadNamesCompOne", n_clicks=0),
    P("Product name"),
    dcc.Dropdown(
        id='nameCompOne',),
    #Second Product
    H4('Select second product'),
    P("Shop"),
    dcc.Dropdown(
        id='shopCompTwo',
        options=[{'label': i, 'value': i} for i in shops],
        value=[i for i in shops],
        placeholder="Shop"),
    P("Kind"),
      dcc.Dropdown(
        id='productCompTwo',
        ),
    Button("Load Products", id="LoadNamesCompTwo", n_clicks=0),
    P("Product name"),
    dcc.Dropdown(
        id='nameCompTwo',),

    #Graph
    Button("Show comparation graph", id="loadButtonComp", n_clicks=0),
    dcc.Graph(
        id="compGraph",

    )
    ],
    id='app-main-comparator')
 ]

##FIRST PRODUCT
@app.callback(DOutput("LoadNamesCompOne", "disabled"),
                [DInput("shopCompOne","value"),
                DInput("productCompOne","value")])

def changeLoadButtonCompOne(valueOne, valueTwo):
    selectedOne.shop=valueOne
    selectedOne.kind=valueTwo
    if selectedOne.shop is None or selectedOne.kind is None:
        return True
    else:
        return False
#Update Product Dropdown
@app.callback(DOutput('productCompOne', 'options'),
              DInput('shopCompOne', 'value'))

def changeProductDropdownCompOne(shopDropdown):
    prices_df = pd.read_csv(__prices_file)
    filter_prices_df = prices_df[prices_df["shop"]==shopDropdown]
    aux = filter_prices_df['kind'].unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options  

#Update load names Button
@app.callback(DOutput("nameCompOne", "options"),
                DInput("LoadNamesCompOne","n_clicks"))

def changeNameDropdownCompOne(n_clicks):
    # Don't trigger update on page load
    if n_clicks == 0:
        return no_update
    prices_df = pd.read_csv(__prices_file)
    filter_prices_df = prices_df[prices_df["shop"]==selectedOne.shop]
    filter_prices_df = filter_prices_df[filter_prices_df["kind"]==selectedOne.kind]
    aux = filter_prices_df.name.unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options

##SECOND PRODUCT
@app.callback(DOutput("LoadNamesCompTwo", "disabled"),
                [DInput("shopCompTwo","value"),
                DInput("productCompTwo","value")])

def changeLoadButtonCompTwo(valueOne, valueTwo):
    selectedTwo.shop=valueOne
    selectedTwo.kind=valueTwo
    if selectedTwo.shop is None or selectedTwo.kind is None:
        return True
    else:
        return False
#Update Product Dropdown
@app.callback(DOutput('productCompTwo', 'options'),
              DInput('shopCompTwo', 'value'))

def changeProductDropdownCompTwo(shopDropdown):
    prices_df = pd.read_csv(__prices_file)
    filter_prices_df = prices_df[prices_df["shop"]==shopDropdown]
    aux = filter_prices_df['kind'].unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options  

#Update load names Button
@app.callback(DOutput("nameCompTwo", "options"),
                DInput("LoadNamesCompTwo","n_clicks"))

def changeNameDropdownCompTwo(n_clicks):
    # Don't trigger update on page load
    if n_clicks == 0:
        return no_update
    prices_df = pd.read_csv(__prices_file)
    filter_prices_df = prices_df[prices_df["shop"]==selectedTwo.shop]
    filter_prices_df = filter_prices_df[filter_prices_df["kind"]==selectedTwo.kind]
    aux = filter_prices_df.name.unique()
    options=[{'label': i, 'value': i} for i in aux]
    return options



##GRAPH
#Update Graph
@app.callback(DOutput("loadButtonComp", "disabled"),
                [DInput("nameCompOne","value"),
                DInput("nameCompTwo","value")])

def changeLoadButton(valueOne, valueTwo):
    selected.One=valueOne
    selected.Two=valueTwo
    if selected.One is None or selected.Two is None:
        return True
    else:
        return False

@app.callback(DOutput("compGraph", "figure"),
              DInput("loadButtonComp","n_clicks"))  

def display_Compgraph(n_clicks):
  # Don't trigger update on page load
    if n_clicks == 0:
        return no_update
    
    dfone = prices_df[prices_df["name"]==selected.One]
    dftwo = prices_df[prices_df["name"]==selected.Two]
    filter_prices_df = dfone.append(dftwo)
    fig = px.line(filter_prices_df, x="date", y="price", color="name",
                 title="Price Evolution"
                
                )
    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.5,
    xanchor="right",
    x=1
))
    return fig