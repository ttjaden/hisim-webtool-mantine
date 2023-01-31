import dash
from dash import html

dash.register_page(__name__,
                   path='/error',
                   title='HiSim | Error',
                   name='error')

layout = html.H1('Page not found')
