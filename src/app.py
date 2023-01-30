import dash_mantine_components as dmc
from dash import Dash, html, Input, Output, ClientsideFunction
from dash_iconify import DashIconify
import dash

app = Dash(__name__, title="HiSim Webtool", use_pages=True)

# Declare server for Heroku or Render deployment. Needed for Procfile.
server = app.server

######################################################################
# Header and Footer ##################################################
######################################################################
header = dmc.Header(height=60,style={"backgroundColor": "#FFFFFF"},children=[
    dmc.Grid(
        children=[
            dmc.Col(span=4,style={"textAlign": "left"},children=
                [dmc.Anchor(dmc.Image(src="/assets/img/banner.svg",alt="Logo",width=150),href='/')]),
            dmc.Col(span=4,style={"textAlign": "center"},children=
                [dmc.Anchor(dmc.Button('About', color='gray', variant='subtle', size='md', leftIcon=DashIconify(icon='feather:info')),href='/about')]),
            dmc.Col(span=4,style={"textAlign": "right"},children=
                [dmc.Burger(id='burger-button', opened=False, size='lg')])
        ]
)]
)

footer = dmc.Footer(
    height=35,
    fixed=True,
    children=[dmc.Anchor(dmc.Text("FZ Jülich GmbH | Impressum",
              align="center",
              color='white'),
              href='https://www.fz-juelich.de/de/impressum',
              target='_blank',
              variant='text')
              ],
    style={"backgroundColor": "#033E6C"},
)

######################################################################
# App layout #########################################################
######################################################################

hidden_div = html.Div(id="hidden-div", style={"display": "none"})

app.layout = html.Div([
    hidden_div,
    header,
    dmc.Container(
        dmc.Center(style={"height": 500, "width": "100%"},
        children=[
            dash.page_container
        ]),
    ),
    footer,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

######################################################################
# Callbacks ##########################################################
######################################################################
