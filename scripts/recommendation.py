import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
import dash_table
import pandas as pd
import numpy as np
import boto3

from scripts import Col_map, stats

def create_recommendation():
	df_show = pd.DataFrame()
	df_show['Recommended Articles'] = ['---', '---', '---', '---', '---'] 
	return [
		html.Div([
		
		dbc.Row(dbc.Col(html.H3("OFFCORS - Cluster Based Recommendation System"),
						width={'size':6, 'offset': 4, 'order': 1}
						),
				),

		dbc.Row(
			[
				dbc.Col(html.Div('City Store'),
						width={'size': 2, 'offset': 1, 'order':1},
						#align='stretch'
					),
				dbc.Col(dcc.Dropdown(id='ciudad_dropdown', 
									placeholder='please select...',
									#options=[{'label': i, 'value': i} for i in sorted(df_recoms['Ciudad Tienda'].unique())],
									options = [{'label':'AGUACHICA','value':'AGUACHICA'},
											   {'label':'TUNJA','value':'TUNJA'},
											   {'label':'BARRANQUILLA','value':'BARRANQUILLA'}]
									,style={'color':'black'}
									),
																		
						width={'size': 2, "offset": 1, 'order': 2},
		
						),
			], no_gutters=True
		),

		dbc.Row(
			[
				dbc.Col(html.Div('Client Code'),
						width={'size': 2, 'offset': 1, 'order':1},
						#align='stretch'
					),
				dbc.Col(dcc.Dropdown(id='user', 
									placeholder='please select a client...'
									#options=[{'label': i, 'value': i} for i in sorted(df_recoms['Codigo_Cliente'].unique())],
									#value='ATLANTICO'
									,style={'color':'black'},
									),
																		
						width={'size': 2, "offset": 1, 'order': 2}
						),
			], no_gutters=True
				
		),
		dbc.Row(
			[
				#dbc.Col(dcc.Graph(id='pie_chart1', figure={}),
				#        width=8, lg={'size': 6,  "offset": 0, 'order': 'first'}
				#        ),
				#dbc.Col(dcc.Graph(id='pie_chart2', figure={}),
				#        width=4, lg={'size': 6,  "offset": 0, 'order': 'last'}
				#        ),

				dbc.Col(dash_table.DataTable(id='table',
											#columns=[{'name':'Article Type'},{'name':'Result'}],
											columns=[{'name':i, 'id':i} for i in df_show.columns],
											data=df_show.head(10).to_dict('records'),
											style_cell = {
													'color':'black',
												}
											),
						width=4, lg={'size': 3,  "offset": 1, 'order': '1'}
						),
			]
		)
])
]