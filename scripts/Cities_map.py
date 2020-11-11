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

    # Create dictionary with cities, location and zoom:

    locations_dict ={'ciudad': ['Medellín', 'Bogotá', 'Barrancabermeja', 'Cali', 'Santa Marta', 'Cartagena', 'Yopal',
                            'Chía', 'Armenia', 'Villavicencio', 'Ipiales', 'Pasto', 'Bucaramanga', 'Cúcuta',
                            'Tunja', 'Pitalito', 'Barranquilla', 'Valledupar', 'Popayán', 'Ibagué', 'Montería',
                            'Riohacha', 'Ocaña', 'Girardot', 'Rionegro', 'Neiva', 'San Andres', 'Apartadó',
                            'Yumbo', 'Manizales', 'La Ceja', 'Aguachica', 'Envigado', 'Pereira', 'Duitama',
                            'Sogamoso', 'Arauca', 'Sincelejo', 'Florencia', 'Cartago', 'Palmira'],
                    'location': [[6.2501125,-75.5803933], [4.683925, -74.087004], [7.064098, -73.856063],
                                [3.427341, -76.521280], [11.235145, -74.192268], [10.397664, -75.506810],
                                [5.333906, -72.395035], [4.877329, -74.034782], [4.540616, -75.674956],
                                [4.136571, -73.626914], [0.826007, -77.640272], [1.211466, -77.277567],
                                [7.107962, -73.113924], [7.902127, -72.506138], [5.550740, -73.349890], 
                                [1.852723, -76.048825], [10.992978, -74.806297], [10.469399, -73.251555], 
                                [2.457041, -76.592210], [4.434196, -75.197765], [8.749607, -75.879484], 
                                [11.537468, -72.912597], [8.247508, -73.356539], [4.302750, -74.801321], 
                                [6.147482, -75.375835], [2.932439, -75.282356], [12.561642, -81.717021], 
                                [7.883654, -76.625723], [3.582594, -76.489090], [5.061344, -75.5049307], 
                                [6.029851, -75.428421], [8.307962, -73.612180], [6.168872, -75.584505], 
                                [4.811958, -75.709814], [5.823173, -73.031070], [5.724299, -72.924044], 
                                [7.081708, -70.753947], [9.302024, -75.396304], [1.617380, -75.609830], 
                                [4.746874, -75.921079], [3.531945, -76.297079]],
                    'zoom': [12, 11, 14, 12, 14, 12, 14, 13, 13, 14, 14, 13, 13, 12, 14, 14, 13, 13, 13, 13,
                            14, 13, 14, 14, 13, 13, 13, 14, 14, 14, 14, 14, 14, 13, 14, 14, 14, 14, 14, 14, 14]
                    }


    # Create the map:
    locations_df = pd.DataFrame(locations_dict)
    
    for index, row in locations_df.iterrows():

        m_prueba = folium.Map(location=row[1],max_zoom=18, zoom_start=row[2])

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
        
        map_name = row[0]+'_map.html'

        m_prueba.save('maps/'+map_name)




















































