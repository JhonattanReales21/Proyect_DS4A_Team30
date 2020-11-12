import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from scripts import Col_map, Cities_map, stats, call_maps	

ciudades= ['Medellín', 'Bogotá', 'Barrancabermeja', 'Cali', 'Santa Marta', 'Cartagena', 'Yopal',
		'Chía', 'Armenia', 'Villavicencio', 'Ipiales', 'Pasto', 'Bucaramanga', 'Cúcuta',
		'Tunja', 'Pitalito', 'Barranquilla', 'Valledupar', 'Popayán', 'Ibagué', 'Montería',
		'Riohacha', 'Ocaña', 'Girardot', 'Rionegro', 'Neiva', 'San Andres', 'Apartadó',
		'Yumbo', 'Manizales', 'La Ceja', 'Aguachica', 'Envigado', 'Pereira', 'Duitama',
		'Sogamoso', 'Arauca', 'Sincelejo', 'Florencia', 'Cartago', 'Palmira']

Cities_map.create_map_cities()

def create_dashboard():
	return [
		#html.H5("Initial dashboard"),
		#html.P("Basic graphs"),
		html.Div(
			[	
				dbc.Row([
					dbc.Col(
						#html.Div([
							dcc.Dropdown(
								id="slct_ciudad_map",placeholder='Ciudad...',
								options=[{'label': i, 'value': i} for i in sorted(ciudades)],
								multi=False,
								value='Bogotá',
								clearable=False,                                 
								style={"color":"black"}
							),
							#]),
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
						),
						

					dbc.Col(
						dbc.Card(
							Col_map.create_map(), body=True, color="dark"
							),
						width=6,
						),
					]), 
    			dbc.Row(
					stats.create_stats()
					),
			],
			id = "basic-graphs",
		)
	]
