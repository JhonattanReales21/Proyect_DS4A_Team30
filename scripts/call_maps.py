from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import os


##############################
# Map Layout
##############################
def call_cities_map(ciudad):

    map = html.Div(
            [
            # Place the main graph component here:
            html.H4("Sales frequency and amount per store (city)"),
            html.Iframe(srcDoc = open('maps/'+ciudad+'_map.html','r').read()
            , id="call_cities_map",width='100%',height=500)
    ],
    className="ds4a-body",
    )
    return map