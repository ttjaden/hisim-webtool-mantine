import dash_mantine_components as dmc
import dash
from dash import html
from dash_iconify import DashIconify

dash.register_page(__name__,
                   path='/settings',
                   title='HiSim | Settings',
                   name='settings')

layout =  html.Div(
    children=[
        dmc.Grid(
            children=[
                dmc.Col(span=12,
                    children=[dmc.Text('Text')
                    ]
                )
            ]
        )
    ]
)