from app import app
from dash_bootstrap_components import Container
from dash_html_components import H1
from dotmap import DotMap as dot

home_page = [
    Container(children=[
      H1('Home')
    ],
    id='app-main-home')
 ]
