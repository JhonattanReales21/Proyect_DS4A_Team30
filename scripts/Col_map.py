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
from geopy.geocoders import Nominatim
import folium
import geopandas

# Recall app
from app import app


def create_map():
	#############################
	# Load paths
	#############################


	#############################
	# Load map data
	#############################


	# Create the map:
	Colombia_map = folium.Map(location=[4.570868, -74.297333],
	                        zoom_start=5,
	                        tiles="OpenStreetMap")
	Colombia_map.save('Colombia_map.html')
	##############################
	# Map Layout
	##############################
	map = html.Div(
	    [
	        # Place the main graph component here:
	        html.Iframe(srcDoc = open('Colombia_map.html','r').read()
	        	, id="COL_map",width='100%',height=600)
	    ],
	    className="ds4a-body",
	)

	return map
