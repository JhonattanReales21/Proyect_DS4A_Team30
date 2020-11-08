import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from scripts import Col_map, stats

def create_dashboard():
	return [
		html.H5("Initial dashboard"),
		html.P("Basic graphs"),
		html.Div(
			[	
				dbc.Row([
					dbc.Col(
						Col_map.create_map()
					),
					dbc.Col(
						html.Iframe(srcDoc = open('Colombia_map.html','r').read()
	        			, id="COL_map2",width='100%',height=600)
					)
					]), 
    			dbc.Row([
					stats.create_stats()
					]),
			],
			id = "basic-graphs",
		)
	]
