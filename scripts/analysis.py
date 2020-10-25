import dash_core_components as dcc
import dash_html_components as html

from scripts import Col_map, stats

def create_analysis():
	return [
		html.H5("Initial Analysis"),
		html.Br(),
		html.P("Basic Analysis"),
		html.Div(
			[
				Col_map.create_map(), 
    			stats.create_stats(),
			],
			id = "basic-graphs",
		)
	]