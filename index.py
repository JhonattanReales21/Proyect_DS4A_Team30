# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Recall app
from app import app

###########################################################
#
#           APP LAYOUT:
#
###########################################################

# LOAD THE DIFFERENT FILES
from scripts import dashboard,tabs
from data_fetch import get_views
from get_callbacks import return_callbacks

# PLACE THE COMPONENTS IN THE LAYOUT
app.layout = html.Div([
	dbc.Row([
				
		dbc.Col(html.Img(src = app.get_asset_url("ds4a-img.svg"), 
				height=50),
				width = {'size': 1.5},
				style={'padding-right':'0px'},
				

				),

		dbc.Col(html.Img(src = app.get_asset_url("logooffcorss.svg"), 
				height=50),
				width = {'size': 1.5},
				style={'padding-right':'0px'},
				

				),

		dbc.Col(html.H1("OFFCORSS Segmentation Analysis"),
				width = {'size': 9},
				style = {'text-align':'center'},
				),


	], className="ds4a-title"),
	dbc.Row([
			html.Div([tabs.create_tab()], id="button"),		
	], className="custom-tab"),

	
	dbc.Row([
		dbc.Col(
			children = dashboard.create_dashboard(),
			id="app-content",
			className="ds4a-app"
		)
		], style={'margin-right':'0px', 'margin-left':'0px'})		
	])
   

###############################################
#
#           APP INTERACTIVITY:
#
###############################################

return_callbacks(app)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)