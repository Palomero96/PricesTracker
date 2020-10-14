from dash_core_components import (
  Link
)

from dash_html_components import (
  Header,
  Nav,
  H1
)

from dotmap import DotMap as dot

def NavBar(routes: dot = dot()):
  return Header([
    H1('PriceTracker'),
    Nav([Link(v.nav, href=k) for k, v in routes.items()])
  ], id='app-navbar')
