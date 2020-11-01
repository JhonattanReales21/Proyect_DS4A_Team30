import dash_core_components as dcc
import dash_html_components as html

from scripts import Col_map, stats

def create_analysis():
	return [
		html.H5("Initial Analysis"),
		html.Br(),
		html.P("Basic Analysis"),
		html.Div([
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id="slct_year",placeholder='Ciudad...',
                 options=[{'label': i, 'value': i} for i in get_views.get_view_by_name('canal_edad_tipo_ciudad')['ciudad_tienda'].unique()],
                 multi=False,
                 value='BOGOTÁ',
                 clearable=False,
                 style={'width': "60%"}),
                        width={'size': 6, "offset": 0, 'order': 1}
                        ),
                dbc.Col(
                    dcc.Checklist(id='check',
                    options=[
                    {'label': 'Canal', 'value': 'canal'},
                    {'label': 'Edad', 'value': 'edad'},
                    {'label': 'Tipo de Negocio', 'value': 'tipo_negocio'},
                    {'label': 'Saldo', 'value': 'saldo'},
                    {'label': 'Tipo de Tejido', 'value': 'tipo_tejido'}

                    ],
                    value=['canal'],
                labelStyle={'display': 'inline-block'}
                ),width={'size': 6, "offset": 0, 'order':2 }
                ),


            ], no_gutters=True
        ),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='pie_chart1', figure={}),
                        width=4, lg={'size': 6,  "offset": 0, 'order': 'first'}
                        ),
                dbc.Col(dcc.Graph(id='par', figure={}),
                        width=4, lg={'size': 6,  "offset": 0, 'order': 'last'}
                        ),
            ]
        ),

    dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id="slct_year3",placeholder='Ciudad...',
                 options=[
                     {"label": "Edad", "value":'Edad'},
                     {"label": "Canal de compra", "value":'Canal'},
                    ],
                 multi=False,
                 value='Canal',
                 clearable=False,
                 style={'width': "60%"}),
                        width={'size': 6, "offset": 0, 'order': 1}
                        ),

                 dbc.Col( dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': 'Canal', 'value': 'Canal'},
                         {'label': 'Sublínea', 'value': 'Sublínea'},
                         {'label': 'Grupo de Articulo', 'value': 'Grupo de Artículo'},
                         {'label': 'Tipo de Negocio', 'value': 'Tipo de Negocio'},
                         {'label': 'Tipo de Tejido', 'value': 'Tipo de Tejido'},
                         {'label': 'Mes de Venta', 'value': 'Mes de Venta'},
                         {'label': 'Saldo', 'value': 'Saldo'},
                ],
                value='Canal',
                style={"width": "50%"}
            ),width={'size': 6, "offset": 1.5, 'order':2 }
                ),


            ], no_gutters=False
        ),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='fig3', figure={}),
                        width=4, lg={'size': 6,  "offset": 0, 'order': 'first'}
                        ),
                dbc.Col(dcc.Graph(id='fig4', figure={}),
                        width=4, lg={'size': 6,  "offset": 0, 'order': 'last'}
                        ),
            ]
        )
		])
			]
