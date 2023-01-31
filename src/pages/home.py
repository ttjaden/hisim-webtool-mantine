import dash_mantine_components as dmc
import dash
from dash import html
from dash_iconify import DashIconify

dash.register_page(__name__,
                   path='/',
                   title='HiSim | Start',
                   name='home')

layout =  html.Div(
    children=[
        dmc.Grid(
            children=[
                dmc.Col(span=12,
                children=[
                    dmc.Container([
                        dmc.Title(f"HiSim Webtool", align='center', order=1),
                        dmc.Title(f"Digital Energy Consulting", align='center', order=5),
                        dmc.Space(h=40),
                        dmc.Text("Please type in your building location", align='center'),
                        dmc.Space(h=10),
                        dmc.TextInput(
                            placeholder="Example Street No. 1, 12345 Berlin",
                            icon=DashIconify(icon="material-symbols:not-listed-location-outline"),
                            size='md',
                            style={"width": 400},
                            radius='lg'),
                        dmc.Space(h=10),
                        dmc.Center(dmc.Anchor(dmc.Button('Show me the results',
                            id='first-calculation',
                            n_clicks=0,
                            type='button',
                            color='gray',
                            size='md',
                            leftIcon=DashIconify(icon='material-symbols:settings')),
                            href='/results'))
                        ]
                        )
                    ]
                )
            ]
        )
    ]
)