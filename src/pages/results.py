import dash_mantine_components as dmc
import dash
from dash import html
from dash_iconify import DashIconify

dash.register_page(__name__,
                   path='/results',
                   title='HiSim | Results',
                   name='results')

layout =  html.Div(
    children=[
        dmc.Text('Based on public data for your building the following metrics were calculated:'),
        dmc.Accordion(
            chevron=DashIconify(icon="material-symbols:display-settings-outline", width=50),
            disableChevronRotation=True,
            chevronSize = 50,
            variant = 'separated',
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Building KPIs"),
                        dmc.AccordionPanel("Description"),
                    ],
                    value="Building KPIs",
                )
            ]
        ),
        dmc.Space(h=40),
        dmc.Text('With the metrics from your current building status the following measures are recommended'),
        dmc.Accordion(
            chevronSize = 50,
            variant = 'separated',
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("System 1"),
                        dmc.AccordionPanel("Description"),
                    ],
                    value="System-1",
                ),
             dmc.AccordionItem(
                    [
                        dmc.AccordionControl("System 2"),
                        dmc.AccordionPanel("Description"),
                    ],
                    value="System-2",
                ),
             dmc.AccordionItem(
                    [
                        dmc.AccordionControl("System 3"),
                        dmc.AccordionPanel("Description"),
                    ],
                    value="System-3",
                ),
            ]
        ),
    ],
)    