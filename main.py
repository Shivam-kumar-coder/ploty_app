import dash 
from dash import dcc , html
from dash.dependencies import Input,Output
import plotly.express  as px
import pandas as pd
app=dash.Dash(__name__)
data={'area':[100,200,300,400,500,600,700,750,800,900,1000],
      'cost':[98,150,200,250,300,350,400,450,500,550,600]}
app.layout=html.Div([html.H1("my application"),
html.H2("my analysis and graph")],style={'textAlign':'center','color':'red'})

app.run(debug=True)