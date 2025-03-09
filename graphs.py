import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from app import server

df = pd.read_csv('./static/data/art_data.csv')

# Genre Bar Graph
genre_bar_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/genre-bar-graph/')

genre_counts = df['field_genre_library'].value_counts().head(10).reset_index()
genre_counts.columns = ['Genres', 'Count']
genre_fig = px.bar(genre_counts, x='Genres', y='Count', title='Top 10 Genres among Items')

genre_bar_app.layout = html.Div([
    dcc.Graph(id='genre-bar-graph', figure=genre_fig)
])

# Classification Bar Graph
classification_bar_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/classification-bar-graph/')
classification_counts = df['field_classification'].value_counts().head(10).reset_index()
classification_counts.columns = ['Classification', 'Count']

class_fig = px.bar(classification_counts, x='Classification', y='Count', title='Top 10 Classifications among Items')

classification_bar_app.layout = html.Div([
    dcc.Graph(id='classification-bar-graph', figure=class_fig)
])

# Location vs Classification Heat Map
df_pairs = df[['field_place_published_objects', 'field_classification']].dropna()
pair_counts = df_pairs.groupby(['field_place_published_objects', 'field_classification']).size().reset_index(name='count')
top_pairs = pair_counts.sort_values(by='count', ascending=False).head(100)
heatmap_data = top_pairs.pivot(index='field_place_published_objects', 
                               columns='field_classification', 
                               values='count').fillna(0).astype(int)
heatmap_fig = px.imshow(
    heatmap_data,
    labels=dict(x="Field Classification", y="Country Published", color="Count"),
    x=heatmap_data.columns,
    y=heatmap_data.index,
    text_auto=True,
    aspect="auto"
)
heatmap_fig.update_layout(
    title='Top 100 Pairs of Countries Published and Field Classification',
    xaxis=dict(tickangle=45)
)
heatmap_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/heatmap/')
heatmap_app.layout = html.Div([
    dcc.Graph(id='heatmap-graph', figure=heatmap_fig)
])