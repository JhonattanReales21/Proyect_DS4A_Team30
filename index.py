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
app.layout = html.Div(
    [
    	html.Div([
    			# left image
    			html.Div(
    				[
    					html.Img(
    							src = app.get_asset_url("ds4a-img.svg"), 
    							id="ds4a-image",
    							style = {
    								"height": "60px",
    								"width": "auto",
    								"margin-bottom": "25px",
    							},
    						),
    				],
    				className = "one-third column",
    			),
    			# title
    			html.Div(
    				[
	    				html.Div(
	    					[
		    					html.H3(
									"OFFCORSS Segmentation Analysis",
									style = {"margin-bottom": "0px"},
		    					),
	    					],
	    				),
	    			],
	    			className = "one-third column",
	    			id = "title",
	    			style = {'display': 'block'},
    			),
    			# tabs
    			html.Div(
    				[
    					tabs.create_tab()
    				],
    				className = "one-third column",
    				id = "button",
    			),
    		],
    		id = "header",
    		className = "row flex-display",
    		style = {"margin-bottom": "25px"}
    	),
    	html.Div(children = dashboard.create_dashboard(), id = "app-content"),
    ],
    #className="ds4a-app",  # You can also add your own css files by locating them into the assets folder
    id = "MainContent",
   	style = {"display":"flex", "flex-direction":"column"},
)

###############################################
#
#           APP INTERACTIVITY:
#
###############################################

return_callbacks(app)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)