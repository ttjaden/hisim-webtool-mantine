import dash_mantine_components as dmc
from dash import Dash, html
import dash

app = Dash(__name__, title="HiSim Webtool", use_pages=True)

# Declare server for Heroku or Render deployment. Needed for Procfile.
server = app.server

app.layout = html.Div([
    dmc.Header(
        height=60,
        children=[dmc.Image(
                  src="/assets/img/banner.svg",
                  alt="Logo",
                  width=150
        )], 
        style={"backgroundColor": "#FFFFFF"}
    ),
    dmc.Center(
    children=[
        dash.page_container
    ])
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
