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
header = dmc.Header(height=45,
                    style={"backgroundColor": "#033E6C"},
                    fixed=True,
                    children=[
    dmc.Grid(
        children=[
            dmc.Col(span=6,style={"textAlign": "left"},children=
                [dmc.Anchor(dmc.Image(src="/assets/img/fzj-white.svg",alt="Logo",width=150),href='/')]),
            dmc.Col(span=6,style={"textAlign": "right"},children=
                [dmc.Burger(id='burger-button', opened=False, size='lg', color='white')])
        ]
)]
)

footer = dmc.Footer(
    height=30,
    fixed=True,
    children=[dmc.Grid(children=[
        dmc.Col(span=5,
                style={"textAlign": "right"},
                children=
                    [dmc.Anchor("Impressum",
                    href='https://www.fz-juelich.de/de/impressum',
                    target='_blank',
                    variant='text')]),
        dmc.Col(span=2,
                style={"textAlign": "center"},
                children=['|']),
        dmc.Col(span=5,
                style={"textAlign": "left"},
                children=
                    [dmc.Anchor("About",
                    href='/about',
                    variant='text')])
    ])],
    style={"backgroundColor": "#033E6C", 'color': 'white'})

######################################################################
# App layout #########################################################
######################################################################

hidden_div = html.Div(id="hidden-div", style={"display": "none"})

app.layout = html.Div([
    dmc.MantineProvider(
        withGlobalStyles=True,
        theme={'colorScheme': 'light'},
        children=[    
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
])

if __name__ == "__main__":
    app.run_server(debug=True)

######################################################################
# Callbacks ##########################################################
######################################################################
