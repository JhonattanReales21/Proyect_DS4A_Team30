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
from data_fetch import get_views

def create_map():
	#############################
	# Load paths
	#############################


	#############################
	# Load map data
	#############################
	
	df_for_map = get_views.get_view_by_name('tiendas_frecuencia')
	df_for_map["Radio_for_map"]=df_for_map["valor_neto"]/37000000

	# Create the map:
	m_prueba = folium.Map(location=[5.543949, -73.917579],max_zoom=18, zoom_start=5)
	tooltip = 'Click me!'

	group1=folium.FeatureGroup(name='<span style="color:red">Freq [1,1.25]</span>')
	m_prueba.add_child(group1)
	group2=folium.FeatureGroup(name="Freq [1.25,1.35]", show=False)
	m_prueba.add_child(group2)
	group3=folium.FeatureGroup(name="Freq [1.35,1.5]", show=False)
	m_prueba.add_child(group3)
	group4=folium.FeatureGroup(name="Freq [1.5,1.8]", show=False)
	m_prueba.add_child(group4)
	group5=folium.FeatureGroup(name="Freq > 1.8", show=False)
	m_prueba.add_child(group5)

	

	for i in range(df_for_map.shape[0]):
		sales=df_for_map.loc[i,"valor_neto"]
		if (df_for_map.loc[i,"frequency"] > 1) & (df_for_map.loc[i,"frequency"] <= 1.25):
			folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"],
						location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
						popup=df_for_map.loc[i,"centro_comercial"],color="black",fill=True,fill_color="red",weight=1,
								fill_opacity=0.5,
						tooltip=f"Sales:{sales}").add_to(group1)
		elif (df_for_map.loc[i,"frequency"] > 1.25) & (df_for_map.loc[i,"frequency"] <= 1.35):
			folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"],
						location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
						popup=df_for_map.loc[i,"centro_comercial"],color="black",fill=True,fill_color="blue",weight=1,
								fill_opacity=0.5,
						tooltip=f"Sales:{sales}").add_to(group2)
		elif (df_for_map.loc[i,"frequency"] > 1.35) & (df_for_map.loc[i,"frequency"] <= 1.5):
			folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"],
						location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
						popup=df_for_map.loc[i,"centro_comercial"],color="black",fill=True,fill_color="coral",weight=1,
								fill_opacity=0.5,
						tooltip=f"Sales:{sales}").add_to(group3)
		elif (df_for_map.loc[i,"frequency"] > 1.5) & (df_for_map.loc[i,"frequency"] <= 1.8):
			folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"],
						location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
						popup=df_for_map.loc[i,"centro_comercial"],color="black",fill=True,fill_color="green",weight=1,
								fill_opacity=0.5,
						tooltip=f"Sales:{sales}").add_to(group4)
		else:
			folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"],
						location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
						popup=df_for_map.loc[i,"centro_comercial"],color="black",fill=True,fill_color="purple",weight=1,
								fill_opacity=0.5,
						tooltip=f"Sales:{sales}").add_to(group5)
	folium.TileLayer('cartodbpositron').add_to(m_prueba)
	folium.LayerControl(collapsed=False).add_to(m_prueba)
	m_prueba.save('Colombia_map.html')
	##############################
	# Map Layout
	##############################
	map = html.Div(
	    [
			html.H1("Map title"),
	        # Place the main graph component here:
	        html.Iframe(srcDoc = open('Colombia_map.html','r').read()
	        	, id="COL_map",width='100%',height=600)
			
	    ],
	    className="ds4a-body",
	)

	return map
