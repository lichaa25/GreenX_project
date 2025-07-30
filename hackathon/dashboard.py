import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import datetime

# Load the data
df = pd.read_csv("simulated_river_data_with_anomalies.csv")

# Parse timestamp
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
else:
    df['timestamp'] = pd.date_range(start=datetime.datetime.now(), periods=len(df), freq='min')

# Handle missing anomaly_flag
if 'anomaly_flag' not in df.columns:
    df['anomaly_flag'] = 0

# Add status column
df['status'] = df['anomaly_flag'].apply(lambda x: 'Anomaly' if x == 1 else 'Normal')

# List of features to plot
features = ["turbidity", "temperature", "pH", "dissolved_oxygen"]

# Create the Dash app
app = Dash(__name__)
app.title = "PolluTrack Dashboard"

# Layout with tabs
app.layout = html.Div([
    html.H1("Real-Time River Pollution Dashboard"),
    dcc.Tabs(
        id='feature-tabs',
        value='turbidity',
        children=[
            dcc.Tab(label='Turbidity', value='turbidity'),
            dcc.Tab(label='Temperature', value='temperature'),
            dcc.Tab(label='pH', value='pH'),
            dcc.Tab(label='Dissolved Oxygen', value='dissolved_oxygen')
        ]
    ),
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=5 * 1000,  # every 5 seconds
        n_intervals=0
    )
])

# Callback to update the graph
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('interval-component', 'n_intervals'),
     Input('feature-tabs', 'value')]
)
def update_graph(n, selected_feature):
    slice_size = 50
    data = df.iloc[:min((n + 1) * slice_size, len(df))]

    fig = px.line(
        data, 
        x='timestamp', 
        y=selected_feature, 
        color='status',
        title=f"{selected_feature.capitalize()} Over Time (With Anomaly Detection)",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title=selected_feature.capitalize(),
        template='plotly_dark'
    )

    return fig

if __name__ == '_main_':
    app.run(debug=True)