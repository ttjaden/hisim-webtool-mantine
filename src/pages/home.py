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
                        dmc.MultiSelect(
                            data=['Avenue 1, 67890 Munich','Heerweg 26, 26629 Aurich','Example Street No.1, 12345 Berlin'],
                            id='selected-location',
                            label="Building Location",
                            description='Please type in Street with number, postal code and city',
                            searchable=True,
                            clearable=True,
                            maxSelectedValues=1,
                            icon=DashIconify(icon="material-symbols:not-listed-location-outline", width=20),
                            size='md',
                            style={"width": 400},
                            radius='md'),
                        dmc.Space(h=10),
                        dmc.Center(dmc.Anchor(dmc.Button('Show me the results',
                            id='first-calculation',
                            n_clicks=0,
                            type='button',
                            color='gray',
                            size='md',
                            radius='md',
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