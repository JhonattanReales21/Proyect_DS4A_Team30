import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from scripts import Col_map, Cities_map, stats, call_maps	

Cities_map.create_map_cities()

def create_dashboard():
	return [
		html.H5("Initial dashboard"),
		html.P("Basic graphs"),
		html.Div(
			[	
				dbc.Row([
					dbc.Col(
						html.Div(
						[
						# Place the main graph component here:
						html.H4("Sales frequency and amount per store (city)"),
						html.Iframe(id="call_cities_map",width='100%',height=600)
						],
						className="ds4a-body",
						)
						
						
					),
					dbc.Col(
						Col_map.create_map()
						
					)
					]), 
    			dbc.Row([
					stats.create_stats()
					]),
			],
			id = "basic-graphs",
		)
	]
