import dash_mantine_components as dmc
import dash
from dash_iconify import DashIconify
from dash import html

dash.register_page(__name__)

layout = html.Div(
    children=[
        dmc.Grid(
            children=[
                dmc.Col(span=12,
                children=[
                    dmc.Container([
                        dmc.Title(f"About this tool", align='center', order=1),
                        dmc.Space(h=20),
                        dmc.Timeline(
                        active=1,
                        bulletSize=15,
                        lineWidth=2,
                        children=[
                        dmc.TimelineItem(
                            title="Kickoff",
                            children=[
                                dmc.Text(
                                    [
                                        "Kickoff with dash and ",
                                        dmc.Anchor("dash-mantine-components",
                                        href="https://www.dash-mantine-components.com/",
                                        size="sm",
                                        target='_blank'),
                                        " for styling",
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                        ),
                        dmc.TimelineItem(
                            title="Functional styling",
                            children=[
                                dmc.Text(
                                    [
                                        "Build visual style like draft on ",
                                        dmc.Anchor("Excalidraw", href="https://app.excalidraw.com/l/5Wer9oRbCV7/6hToDGZOluV", size="sm", target='_blank'),
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                        ),
                        dmc.TimelineItem(
                            title="Marriage with UTSP",
                            children=[
                                dmc.Text(
                                    [
                                        "Create and send simulation job to UTSP and deal with answer",
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                        ),
                        dmc.TimelineItem(
                            title="Ready for publish",
                            children=[
                                dmc.Text(
                                    [
                                        "and win the best-software-in-the-world award",
                                    ],
                                    color="dimmed",
                                    size="sm",
                                ),
                            ],
                        )],),
                        dmc.Space(h=20),
                        dmc.Anchor(dmc.Button('Back to start', color='gray', size='md', leftIcon=DashIconify(icon='material-symbols:rocket-launch-outline')),href='/')
                        ]
                    )]
                )
            ]
        )
    ]
)