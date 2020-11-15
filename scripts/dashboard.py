import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from scripts import Col_map, Cities_map, stats, call_maps	

# Cities
ciudades= ['Medellín', 'Bogotá', 'Barrancabermeja', 'Cali', 'Santa Marta', 'Cartagena', 'Yopal',
		'Chía', 'Armenia', 'Villavicencio', 'Ipiales', 'Pasto', 'Bucaramanga', 'Cúcuta',
		'Tunja', 'Pitalito', 'Barranquilla', 'Valledupar', 'Popayán', 'Ibagué', 'Montería',
		'Riohacha', 'Ocaña', 'Girardot', 'Rionegro', 'Neiva', 'San Andres', 'Apartadó',
		'Yumbo', 'Manizales', 'La Ceja', 'Aguachica', 'Envigado', 'Pereira', 'Duitama',
		'Sogamoso', 'Arauca', 'Sincelejo', 'Florencia', 'Cartago', 'Palmira']


# Pre-render all city maps
Cities_map.create_map_cities()


def create_dashboard():
	'''
	This function creates the layout where the initial dashboard is going to be
	displayed in the dash.
	'''
	return [

		html.Div(
			[	
				dbc.Row([
					dbc.Col(
						dbc.CardBody(
							dcc.Dropdown(
								id="slct_ciudad_map",placeholder='Ciudad...',
								options=[{'label': i, 'value': i} for i in sorted(ciudades)],
								multi=False,
								value='Bogotá',
								clearable=False,                                 
								style={"color":"black"}
							),
							className="sidebar-inner"),
						width = 2,
						className="ds4a-sidebar"
						),
					dbc.Col(

			
						dbc.Card([
							html.H5("Sales frequency and amount per store"),
							html.P("City"),
							html.Iframe(id="call_cities_map",width='100%',height=500),
						], body=True, color="dark"),

						width={"size": 4, "offset": 2},
						className="ds4a-app"
						),
						

					dbc.Col(
						dbc.Card(
							Col_map.create_map(), body=True, color="dark"
							),
						width=6,
						className="ds4a-app" 
						),
					]), 
    			dbc.Row([
						dbc.Col(
								dbc.Card([
									html.H5('Sales history per city'),
									dcc.Graph(
										id='line_plot_cities',
										figure={"layout": {"height": 500}},
									),
								], body=True, color="dark"),
						width={"size": 10, "offset": 2},
						className="ds4a-app" 
						),
					]),
			],
			id = "basic-graphs",
		)
	]
