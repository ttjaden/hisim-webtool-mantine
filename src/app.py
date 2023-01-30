import dash_mantine_components as dmc
from dash import Dash, html
import dash

app = Dash(__name__, title="HiSim Webtool", use_pages=True)

# Declare server for Heroku or Render deployment. Needed for Procfile.
server = app.server

header = dmc.Header(
        height=60,
        children=[dmc.Image(
                  src="/assets/img/banner.svg",
                  alt="Logo",
                  width=150
        )], 
        style={"backgroundColor": "#FFFFFF"},
)

footer = dmc.Footer(
    height=30,
    fixed=True,
    children=[dmc.Text("Forschungszentrum Jülich GmbH | Impressumg & Datenschutz",
              align="center",
              color='white')],
    style={"backgroundColor": "#033E6C"},
)

navbar = dmc.Navbar(
    p="md",
    width={"base": 300},
    height=500,
    children=[
        dmc.Anchor("Home", href="/"),
        dmc.Anchor("About", href="/about"),
    ],
    fixed=False,
    hidden=True,
)

app.layout = html.Div([
    header,
    dmc.Center(
    children=[
        dash.page_container
    ]),
    footer,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
