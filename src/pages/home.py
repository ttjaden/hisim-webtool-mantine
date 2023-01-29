import dash_mantine_components as dmc
import dash
from dash import html

dash.register_page(__name__,
                   path='/',
                   title='Start',
                   name='home')

style = {
    "marginTop": 20,
    "marginBottom": 20,
}

def funtion():
    """
    Generates user input forms for upload screen
    """

    value1 = dmc.Text('Text 1')
        
    value2 = dmc.Text('Text 2')

    return dmc.Stack([value1, value2],align='stretch')

layout =  html.Div([
            dmc.Container([
            dmc.Title(f"HiSim Webtool", order=2),
            dmc.Title(f"Digital Energy Consulting", order=5),
            dmc.Space(h=20),
            # Content form function
            funtion(),
            ],style=style)
])