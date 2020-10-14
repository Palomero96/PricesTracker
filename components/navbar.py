from dash_bootstrap_components import NavbarSimple, NavItem, NavLink
from dotmap import DotMap as dot


def Navbar(routes: dot = dot()):
  children = [NavItem(
    NavLink(value.nav, href=key, active=True)
  ) for key, value in routes.items()]

  return NavbarSimple(children,
    brand="PriceTracker",
    brand_href="#",
    color="primary",
    dark=True,
    id='app-navbar')
