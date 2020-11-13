import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from scripts import Col_map, stats
from data_fetch import get_views
from get_callbacks import return_callbacks

card_main = dbc.Card(
    [

        dbc.CardBody(
            [
                html.H4("Analysis of sales values by city and items offered by OFFCORSS", className="card-title"),

                html.P(
                    "choose the city to see the main items sold in each of the stores.",
                    className="card-text",
                ),
                dcc.Dropdown(id="ciudades-dpdn",placeholder='Ciudad...',
                 options=[{'label': i, 'value': i} for i in get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')['ciudad_tienda'].unique()],
                 multi=False,
                 value='YUMBO',
                 clearable=False,
                 style={'width': "60%",'color':'black'}),
                # dbc.Button("Press me", color="primary"),
                # dbc.CardLink("GirlsWhoCode", href="https://girlswhocode.com/", target="_blank"),
                html.P(
                    "select the cluster you want to view",
                    className="card-text",
                ),
                dcc.Dropdown(id='cluster-dpdn', options=[], multi=False,style={'width': "60%",'color':'black'}),
                html.P(
                    "Choose several categories to observe the profits produced",
                    className="card-text",
                ),
                dcc.Checklist(id='check',
                    options=[
                    {'label': 'Canal', 'value': 'canal'},
                    {'label': 'Edad', 'value': 'edad'},
                    {'label': 'Tipo de Negocio', 'value': 'tipo_neogcio'},
                    {'label': 'Saldo', 'value': 'saldo'},
                    {'label': 'Tipo de Tejido', 'value': 'tipo_tejido'}

                    ],
                    value=['canal'],
                labelStyle={'display': 'inline-block'},
                style={'width': "60%",'color':'black'}
                ),
                html.P(
                    "Choose the variable to observe its trend during these years.",
                    className="card-text",
                ),
                dcc.Dropdown(id="slct_year3",placeholder='Ciudad...',
                 options=[
                     {"label": "Edad", "value":'edad'},
                     {"label": "Canal de compra", "value":'canal'},
                    ],
                 multi=False,
                 value='canal',
                 clearable=False,
                 style={'width': "60%",'color':'black'}),
                # dbc.Button("Press me", color="primary"),
                # dbc.CardLink("GirlsWhoCode", href="https://girlswhocode.com/", target="_blank"),
                html.P(
                    "Select the variable to view your sales behavior.",
                    className="card-text",
                ),
                dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': 'Canal', 'value': 'canal'},
                         {'label': 'Sublínea', 'value': 'sublinea'},
                         {'label': 'Tipo de Tejido', 'value': 'tipo_tejido'},
                         {'label': 'Grupo de Artículo', 'value': 'grupo_articulo'},
                         {'label': 'Tipo de Artículo', 'value': 'tipo_articulo'},
                         {'label': 'Mes de Venta', 'value': 'mes_venta'},
                         {'label': 'Saldo', 'value': 'saldo'},
                ],
                value='canal',
                style={"width": "50%",'color':'black'}
            ),
            ]
        ),
    ],
    color="warning",   # https://bootswatch.com/default/ for more card colors
    inverse=False,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
)


card_main2 = dbc.Card(
    [

        dbc.CardBody(
            [

                # dbc.Button("Press me", color="primary"),
                # dbc.CardLink("GirlsWhoCode", href="https://girlswhocode.com/", target="_blank"),
                dbc.Card(dcc.Graph(id='fig1', figure={}), color="dark"),
                dbc.Card(dcc.Graph(id='fig2', figure={})),
                dbc.Card(dcc.Graph(id='fig4', figure={})),
                dbc.Card(dcc.Graph(id='fig3', figure={})),
                    ]
        ),
    ],
    color="dark",   # https://bootswatch.com/default/ for more card colors
    inverse=False,   # change color of text (black or white)
    outline=False,  # True = remove the block colors from the background and header
)


def create_analysis():
    return [
        html.Br(),

        html.Div([
            dbc.Row([dbc.Col(card_main, width=4),
            dbc.Col(card_main2, width=8)], justify="around"),


        ])

        ]
