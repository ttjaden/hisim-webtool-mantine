'''
 # @ Create Time: 2023-01-29 21:05:31.038994
'''

import dash_mantine_components as dmc
from dash import Dash

app = Dash(__name__, title="hisim-webtool-mantine")

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

app.layout = dmc.Alert(
    [
        "Hi from Dash Mantine Components. You can create some great looking dashboards using me!"
    ],
    title="Welcome!",
    color="violet",
)

if __name__ == "__main__":
    app.run_server(debug=True)
