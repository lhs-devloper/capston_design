from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

df = pd.read_csv("data/predict_new_hitter.csv", encoding="cp949")

# fig = px.line(df, x="year", y="WAR", color="Name", height=800)


app.layout = html.Div(
    html.Div(
        [
            html.H1(children="Capston DashBoard"),
            dcc.Dropdown(
                df["Name"].unique(),
                "강백호",
                id="xaxis-column",
                style={"text-align": "center", "color": "black"},
            ),
            dcc.Graph(id="plotly-output-graph"),  # , figure=fig),
        ],
        style={"margin-left": "10%", "width": "80%", "display": "inline-block"},
    ),
)


@app.callback(Output("plotly-output-graph", "figure"), Input("xaxis-column", "value"))
def update_output(xaxis_column_value):
    dff = df[df["Name"] == xaxis_column_value]
    fig = px.line(dff, x="year", y="WAR", color="Name", height=800)
    fig.update_xaxes(title=xaxis_column_value)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
