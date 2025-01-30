from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

server = Flask(__name__)
app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/')

df = px.data.gapminder()

app.layout = html.Div([
    html.H1("Interactive Plotly Dash in Flask"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='United States'
    ),
    dcc.Graph(id='line-graph')
])

@app.callback(
    Output('line-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'GDP per Capita of {selected_country}')
    return fig

@server.route('/dash_redirect')
def dash_redirect():
    return '', 302, {'Location': '/dash/'}

@server.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    server.run(debug=True)
