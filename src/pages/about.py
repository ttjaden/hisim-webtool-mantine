import dash_mantine_components as dmc
import dash
from dash import html

dash.register_page(__name__)

style = {
    "marginTop": 20,
    "marginBottom": 20,
}

layout = html.Div(
    [
        dmc.Container([
        dmc.Title(f"About this tool", order=2),
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
                        size="sm"),
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
                        dmc.Anchor("Excalidraw", href="https://app.excalidraw.com/l/5Wer9oRbCV7/6hToDGZOluV", size="sm"),
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
        ),
    ],
)]
,px=0,style=style)]
)