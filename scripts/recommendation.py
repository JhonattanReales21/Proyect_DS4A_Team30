import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
import dash_table
import pandas as pd
import numpy as np
import boto3

from scripts import Col_map, stats

# Recall app
from app import app

def create_recommendation():
	df_show = pd.DataFrame()
	df_show['Recommended Articles'] = ['---', '---', '---', '---', '---'] 
	return [
		html.Div([
		
		dbc.Row(
			dbc.Col(
				html.H3("OFFCORSS - Cluster Based Recommendation System",
				 style={"text-align":"center"}),
				 width={'size':10, 'offset': 1, 'order': 1}
					),
				),

		dbc.Row(
			[
				dbc.Col([
					dbc.Card(
						html.P('City Store', style={"font-weight":"bold"}),
						body=True, className="sidebar-inner",
						),
						dbc.Card(
							html.P('Client Code', style={"font-weight":"bold"}), 
						body=True, className="sidebar-inner"
						),
						
				],width={'size': 2, 'offset': 1, 'order':1}),
				dbc.Col([
					dbc.Card(
						dcc.Dropdown(id='ciudad_dropdown', 
									placeholder='please select...',
									options = [{'label':'AGUACHICA','value':'AGUACHICA'},
											   {'label':'TUNJA','value':'TUNJA'},
											   {'label':'BARRANQUILLA','value':'BARRANQUILLA'}]
									,style={'color':'black'}
									),body=True),

					dbc.Card(
						dcc.Dropdown(id='user', 
									placeholder='please select a client...'
									,style={'color':'black'},
									), body=True),
																		
				], width={'size': 2, "offset": 0, 'order': 2},
						),

				dbc.Col(
					dbc.Card(
						dash_table.DataTable(id='table',
											columns=[{'name':i, 'id':i} for i in df_show.columns],
											data=df_show.head(10).to_dict('records'),
											style_cell = {'color':'black'}
											),body=True,
											style={"margin-top":"2em"}
											),
						width={'size': 3,  "offset": 0, 'order': 3}
						,),
				dbc.Col(
					dbc.Card(
						html.Img(src = app.get_asset_url("podium.png"), height=200),
					body=True)
				,width={'size': 4,  "offset": 0, 'order': 4})
			], no_gutters=False
		,align="center"),
])
]