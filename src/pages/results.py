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
        dmc.Text('Based on public data for your building the following metrics were calculated:', weight=700),
        dmc.Space(h=10),
        dmc.Accordion(
            chevron=DashIconify(icon="material-symbols:display-settings-outline", width=50),
            disableChevronRotation=True,
            chevronSize = 50,
            variant = 'separated',
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl(dmc.Grid(
                            children=[
                                dmc.Col(html.Div(dmc.Grid(children=[dmc.Col(DashIconify(icon="mdi:building", width=30),span=2),dmc.Col(dmc.Text('Reburbished Single Family House from 1964',size='xs'),span=10)])), span=4),
                                dmc.Col(html.Div(dmc.Grid(children=[dmc.Col(DashIconify(icon="et:gears", width=30),span=2),dmc.Col([dmc.Text('Heating: Gas-Heater',size='xs'),dmc.Text('Electr.: Public Grid',size='xs'),dmc.Text('Mobility: 2x fossil cars',size='xs')],span=10)])), span=4),
                                dmc.Col(html.Div(dmc.Grid(children=[dmc.Col(DashIconify(icon="bx:euro", width=30),span=2),dmc.Col([dmc.Text('Gas: 780 €/a',size='xs'),dmc.Text('Electr.: 1200 €/a',size='xs'), dmc.Text('Fuel: 925 €/a',size='xs')],span=10)])), span=4),
                            ],
                            gutter="xs",
                            )),
                        dmc.AccordionPanel(dmc.Grid(
                            children=[
                                dmc.Col(html.Div(dmc.Grid(children=[dmc.Col(dmc.Center(DashIconify(icon="mdi:building", width=30)),span=1),dmc.Col(dmc.ChipGroup([dmc.Chip(x, value=x, size='xs', color='gray') for x in ["SFH", "MFH", "Other"]],value="SFH"),span=5), dmc.Col(dmc.Slider(min=50, max=250, step=10, color='gray', marks = [{'value': 50, 'label': '50 m²'}, {'value': 250, 'label': '250 m²'}]),span=4),dmc.Col(dmc.Switch(size='xs'),span=1,offset=1)])), span=12),
                                dmc.Col(html.Div(dmc.Grid(children=[dmc.Col(dmc.Center(DashIconify(icon="et:gears", width=30)),span=1),dmc.Col(dmc.ChipGroup([dmc.Chip(x, value=x, size='xs', color='gray') for x in ["Gas", "Oil", "Wood", "Electric"]],value="SFH"),span=5), dmc.Col(dmc.Slider(min=1, max=25, step=1, color='gray', marks = [{'value': 1, 'label': '1 kW'}, {'value': 25, 'label': '25 kW'}]),span=4),dmc.Col(dmc.Switch(size='xs'),span=1,offset=1)])), span=12),
                                dmc.Col(html.Div(dmc.Grid(children=[dmc.Col(dmc.Center(DashIconify(icon="bx:euro", width=30)),span=1),dmc.Col([dmc.Text('Gas:',size='xs'),dmc.Text('Electr.:',size='xs'), dmc.Text('Fuel:',size='xs')],span=5), dmc.Col(dmc.Slider(min=5, max=50, step=10, color='gray', marks = [{'value': 5, 'label': '5 Ct/kWh'}, {'value': 50, 'label': '50 Ct/kWh'}]),span=4),dmc.Col(dmc.Switch(size='xs'),span=1,offset=1)])), span=12),
                            ],
                            gutter="xs",
                            )),
                    ],
                    value="Building KPIs",
                )
            ]
        ),
        dmc.Space(h=10),
        dmc.Alert(
            'Before diving into the results, please check and adjust the building metrics!',
            title='Warning!',
            color='red',
            icon=DashIconify(icon="material-symbols:warning-outline-rounded", width=40),
            variant='outline',
            withCloseButton=True),
        dmc.Space(h=20),
        dmc.Divider(variant="dashed", size='xs', label='Results', labelPosition='center'),
        dmc.Space(h=20),
        dmc.Text('With the metrics from your current building status the following measures are recommended', weight=700),
        dmc.Space(h=10),
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