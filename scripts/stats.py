import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import os

# Recall app
from app import app

# Import data
from data_fetch import get_views
  

def create_stats():
    ##############################################################
    # LINE PLOT
    ###############################################################
    line_df = get_views.get_view_by_name('ventas_diarias')

    line_fig = px.line(line_df, 
        x = 'fecha_compra', 
        y = 'promedio_ventas', 
        hover_data=['volumen_ventas'])

    line_fig.update_layout(
         height=500
    )

    ###############################################################
    # BAR PLOT
    ###############################################################
    bar_df = get_views.get_view_by_name('venta_ciudad_tienda').head(10)

    bar_fig = px.bar(bar_df
           , y = 'ciudad_tienda', x = 'tienda_x_ciudad'
           , color = 'canal'
           , hover_data=['canal']
           , barmode = 'stack'
           , orientation = 'h'
          )
    bar_fig.update_layout(
        autosize=True,
        #width=1000,
        height=500,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        yaxis={'categoryorder':'total ascending'}
    )
    #################################################################################
    # Here the layout for the plots to use.
    #################################################################################
    stats =  [
                    dbc.Col(
                        dbc.Card(
                            dcc.Graph(figure=bar_fig, id="bar"),body=True, color="dark"
                            ),
                            width={"size": 5, "offset": 2},
                            ),
                    dbc.Col(
                        dbc.Card(
                            dcc.Graph(figure=line_fig, id="line"),body=True, color="dark"
                            ),
                            width=5
                        )
                ]
            


    return stats