import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import datetime


df = pd.read_csv("simulated_river_data_with_anomalies.csv")


if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
else:
    
    df['timestamp'] = pd.date_range(start=datetime.datetime.now(), periods=len(df), freq='min')


if 'anomaly_flag' not in df.columns:
    df['anomaly_flag'] = 0  


df['status'] = df['anomaly_flag'].apply(lambda x: 'Anomaly' if x == 1 else 'Normal')


app = Dash(__name__)
app.title = "PolluTrack Dashboard"

app.layout = html.Div([
    html.H1("Real-Time River Pollution Dashboard"),
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=5*1000,  
        n_intervals=0
    )
])

@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph(n):
    
    slice_size = 50
    data = df.iloc[:min((n+1)*slice_size, len(df))]

    fig = px.line(data, x='timestamp', y='turbidity', color='status',
                  title="Turbidity Over Time (With Anomaly Detection)",
                  markers=True)

    fig.update_layout(xaxis_title="Time", yaxis_title="Turbidity",
                      template='plotly_dark')

    return fig

if __name__ == '__main__':
    app.run(debug=True)