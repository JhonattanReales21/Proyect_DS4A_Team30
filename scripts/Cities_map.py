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
import branca

# Recall app
from app import app
from data_fetch import get_views

def create_map_cities():

    #############################
	# Load paths
	#############################


	#############################
	# Load map data
	#############################
	
    df_for_map = get_views.get_view_by_name('tiendas_frecuencia')
    df_for_map["Radio_for_map"]=((df_for_map["valor_neto"])/df_for_map["valor_neto"].mean())*10+5

    # Create the map:
    
    if input_location=="Medellin":
        Location=[6.2501125,-75.5803933]
        zoom=12
    elif input_location=="Bogotá":
        Location=[4.683925, -74.087004]
        zoom=11
    elif input_location=="Barrancabermeja":
        Location=[7.064098, -73.856063]
        zoom=14
    elif input_location=="Cali":
        Location=[3.427341, -76.521280]
        zoom=12
    elif input_location=="Santa Marta":
        Location=[11.235145, -74.192268]
        zoom=14
    elif input_location=="Cartagena":
        Location=[10.397664, -75.506810]
        zoom=12
    elif input_location=="Yopal":
        Location=[5.333906, -72.395035]
        zoom=14
    elif input_location=="Chia":
        Location=[4.877329, -74.034782]
        zoom=13
    elif input_location=="Armenia":
        Location=[4.540616, -75.674956]
        zoom=13
    elif input_location=="Villavicencio":
        Location=[4.136571, -73.626914]
        zoom=14
    elif input_location=="Ipiales":
        Location=[0.826007, -77.640272]
        zoom=14
    elif input_location=="Pasto":
        Location=[1.211466, -77.277567]
        zoom=13
    elif input_location=="Bucaramanga":
        Location=[7.107962, -73.113924]
        zoom=13
    elif input_location=="Cúcuta":
        Location=[7.902127, -72.506138]
        zoom=12
    elif input_location=="Tunja":
        Location=[5.550740, -73.349890]
        zoom=14
    elif input_location=="Pitalito":
        Location=[1.852723, -76.048825]
        zoom=14
    elif input_location=="Barranquilla":
        Location=[10.992978, -74.806297]
        zoom=13
    elif input_location=="Valledupar":
        Location=[10.469399, -73.251555]
        zoom=13
    elif input_location=="Popayán":
        Location=[2.457041, -76.592210]
        zoom=13
    elif input_location=="Ibagué":
        Location=[4.434196, -75.197765]
        zoom=13
    elif input_location=="Montería":
        Location=[8.749607, -75.879484]
        zoom=14
    elif input_location=="Riohacha":
        Location=[11.537468, -72.912597]
        zoom=13
    elif input_location=="Ocaña":
        Location=[8.247508, -73.356539]
        zoom=14
    elif input_location=="Girardot":
        Location=[4.302750, -74.801321]
        zoom=14
    elif input_location=="Rionegro":
        Location=[6.147482, -75.375835]
        zoom=13
    elif input_location=="Neiva":
        Location=[2.932439, -75.282356]
        zoom=13
    elif input_location=="San Andres":
        Location=[12.561642, -81.717021]
        zoom=13
    elif input_location=="Apartadó":
        Location=[7.883654, -76.625723]
        zoom=14
    elif input_location=="Yumbo":
        Location=[3.582594, -76.489090]
        zoom=14
    elif input_location=="Manizales":
        Location=[5.061344, -75.5049307]
        zoom=14
    elif input_location=="La Ceja":
        Location=[6.029851, -75.428421]
        zoom=14
    elif input_location=="Aguachica":
        Location=[8.307962, -73.612180]
        zoom=14
    elif input_location=="Envigado":
        Location=[6.168872, -75.584505]
        zoom=14
    elif input_location=="Pereira":
        Location=[4.811958, -75.709814]
        zoom=13 
    elif input_location=="Duitama":
        Location=[5.823173, -73.031070]
        zoom=14
    elif input_location=="Sogamoso":
        Location=[5.724299, -72.924044]
        zoom=14
    elif input_location=="Arauca":
        Location=[7.081708, -70.753947]
        zoom=14
    elif input_location=="Sincelejo":
        Location=[9.302024, -75.396304]
        zoom=14
    elif input_location=="Florencia":
        Location=[1.617380, -75.609830]
        zoom=14    
    elif input_location=="Cartago":
        Location=[4.746874, -75.921079]
        zoom=14
    elif input_location=="Palmira":
        Location=[3.531945, -76.297079]
        zoom=14

    m_prueba = folium.Map(location=Location,max_zoom=18, zoom_start=zoom)

    circle="""
	<svg version='1.1' xmlns='http://www.w3.org/2000/svg'
		width='25' height='25' viewBox='0 0 120 120'>
	<circle cx='60' cy='60' r='50'
			fill={} />
	</svg>
	"""
    group1=folium.FeatureGroup(name=circle.format('#FF0000')+"<FONT SIZE=2>Freq. [1,1.25]</font>  ")
    m_prueba.add_child(group1)

    group2=folium.FeatureGroup(name=circle.format('#FF7070')+"<FONT SIZE=2>Freq. [1.25,1.35]</font>")
    m_prueba.add_child(group2)
    
    group3=folium.FeatureGroup(name=circle.format('#FF6B22')+"<FONT SIZE=2>Freq. [1.35,1.5]</font>" )
    m_prueba.add_child(group3)

    group4=folium.FeatureGroup(name=circle.format('#0FFB0E')+"<FONT SIZE=2>Freq. [1.5,1.8]</font>")
    m_prueba.add_child(group4)

    group5=folium.FeatureGroup(name=circle.format('#019F00')+"<FONT SIZE=2>Freq. > 1.8</font>")
    m_prueba.add_child(group5)

    for i in range(df_for_map.shape[0]):

	    sales=round(df_for_map.loc[i,"valor_neto"]/1000000,1)
	    sales=f"${sales}M"

	    html_ = """
        <h2 style="margin-bottom:-10"; align="center">{}</h2>""".format(df_for_map.loc[i,'punto_venta']) + """ <br>
        <b>Total ventas (1 año):</b> {}""".format(sales) + """ <br/>
        <b>Frec. de venta (1 año):</b> {}""".format(round(df_for_map.loc[i,'frequency'],4)) + """ <br/>
        <b>Centro comercial:</b> {}""".format(df_for_map.loc[i,'centro_comercial']) + """ <br/>
        <b>Canal:</b> {}""".format(df_for_map.loc[i,'canal']) + """ <br/>
        <b>Codigo tienda:</b> {}""".format(df_for_map.loc[i,'codigo_tienda']) + """ <br/>
        <b>IDGEO:</b> {}""".format(df_for_map.loc[i,'id_geo'])

        iframe = branca.element.IFrame(html=html_, width=300, height=250)
	    popup = folium.Popup(iframe, max_width=305, parse_html=True)
        
        if (df_for_map.loc[i,"frequency"] > 1) & (df_for_map.loc[i,"frequency"] <= 1.25):
            folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"], 
                        location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
                        popup=popup,
                                color="black",fill=True,fill_color="#FF0000",weight=1,
                                fill_opacity=0.7,
                        tooltip=f"<FONT SIZE=4><b>Ventas</b>:{sales}</font>").add_to(group1)

        elif (df_for_map.loc[i,"frequency"] > 1.25) & (df_for_map.loc[i,"frequency"] <= 1.35):
            folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"], 
                        location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
                        popup=popup,color="black",fill=True,fill_color="#FF7070",weight=1,
                                fill_opacity=0.7,
                        tooltip=f"<FONT SIZE=4><b>Ventas</b>:{sales}</font>").add_to(group2)
        
        elif (df_for_map.loc[i,"frequency"] > 1.35) & (df_for_map.loc[i,"frequency"] <= 1.5):
            folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"], 
                        location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
                        popup=popup,color="black",fill=True,fill_color="#FF6B22",weight=1,
							    fill_opacity=0.8,
					    tooltip=f"<FONT SIZE=4><b>Ventas</b>:{sales}</font>").add_to(group3)

        elif (df_for_map.loc[i,"frequency"] > 1.5) & (df_for_map.loc[i,"frequency"] <= 1.8):
		    folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"], 
					    location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
					    popup=popup,color="black",fill=True,fill_color="#8EFF94",weight=1,
							    fill_opacity=0.8,
					    tooltip=f"<FONT SIZE=4><b>Ventas</b>:{sales}</font>").add_to(group4)
	    else:
		    folium.CircleMarker(radius=df_for_map.loc[i,"Radio_for_map"], 
					    location=[df_for_map.loc[i,"latitude"],df_for_map.loc[i,"longitude"]],
					    popup=popup,color="black",fill=True,fill_color="#2B9A00",weight=1,
							    fill_opacity=0.8,
					    tooltip=f"<FONT SIZE=4><b>Ventas</b>:{sales}</font>").add_to(group5)
			
	folium.LayerControl(collapsed=True).add_to(m_prueba)
	m_prueba.save('Colombia_cities_map.html')
	##############################
	# Map Layout
	##############################
	map = html.Div(
	    [
	        # Place the main graph component here:
	        html.Iframe(srcDoc = open('Colombia_cities_map.html','r').read()
	        	, id="COL_cities_map",width='100%',height=600)
	    ],
	    className="ds4a-body",
	)

	return map





















































