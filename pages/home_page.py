from dash_html_components import (
  Div,
  P
)

from app import app

from dotmap import DotMap as dot

home_page = dot({
  'main': [
    Div([
      P('Home')
    ],
    id='app-main')
  ]
})
