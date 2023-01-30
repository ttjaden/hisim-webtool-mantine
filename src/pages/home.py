import dash_mantine_components as dmc
import dash
from dash import html

dash.register_page(__name__,
                   path='/',
                   title='Start',
                   name='home')

def function():
    """
    Generates user input forms for upload screen
    """
    value1 = dmc.Text('Text 1')  
    value2 = dmc.Text('Text 2')
    return dmc.Stack([value1, value2],align='stretch')

layout =  html.Div(
    children=[
        dmc.Grid(
            children=[
                dmc.Col(span=12,
                children=[
                    dmc.Container([
                        dmc.Title(f"HiSim Webtool", align='center', order=1),
                        dmc.Title(f"Digital Energy Consulting", align='center', order=5),
                        dmc.Space(h=20),
                        # Content form function
                        function(),]
                        )
                    ]
                )
            ]
        )
    ],
)