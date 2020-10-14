# -*- coding: utf-8 -*-
from dotenv import load_dotenv

load_dotenv()

import argparse
import os

import dash
from dash.dependencies import Input as DInput
from dash.dependencies import Output as DOutput
from dash_core_components import Link, Location
from dash_html_components import (H1, Aside, Div, Footer, Header, Main, Nav, P,
                                  Span)
from dotmap import DotMap as dot

from app import app
from components.navbar import Navbar
from pages.home_page import home_page

#
# App Routes
#
routes = dot({
  '/': dot({
    'layout': home_page,
    'nav': 'Home',
    'title': 'Home'
  })
  # '/maps/heat': dot({
  #   'layout': heat_maps_page,
  #   'nav': 'Heat',
  #   'title': 'MM Heat Maps'
  # }),
  # '/maps/choro': dot({
  #   'layout': choro_maps_page,
  #   'nav': 'Choropleth',
  #   'title': 'MM Choropleth Maps'
  # })
})

#
# App Base Layout
#
app.layout = Div([
  Location(id='url', refresh=True),
  Navbar(routes),
  Main(P('Loading...', style={ 'text-align': 'center' }), id='app-main')
], id='app-root')

@app.callback(DOutput('app-main', 'children'),
              [DInput('url', 'pathname')])
def display_main(pathname):
    return routes[pathname].layout.main

@app.callback([DOutput('app-toolbar-content', 'children'),
               DOutput('app-toolbar', 'className'),],
              [DInput('url', 'pathname')])
def display_toolbar(pathname):
  children = routes[pathname].layout.toolbar
  className = ""

  if len(children) > 0:
    className = "show"

  return children, className

#
# Args
#
argparser = argparse.ArgumentParser()

argparser.add_argument(
  '-d',
  '--debug',
  action='store_true',
  required=False,
  help='Start server in debug'
)

argparser.add_argument(
  '-j',
  '--host',
  required=False,
  type=str,
  default=os.getenv('HOST'),
  help='Server host'
)

argparser.add_argument(
  '-p',
  '--port',
  required=False,
  type=str,
  default=os.getenv('PORT'),
  help='Server port'
)

#
# Main
#
if __name__ == '__main__':
  # Parse args
  args = argparser.parse_args()

  debug = args.debug
  host = args.host
  port = args.port

  # Start server
  app.run_server(debug=debug, host=host, port=port)
