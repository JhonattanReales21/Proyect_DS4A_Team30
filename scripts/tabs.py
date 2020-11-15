import dash_core_components as dcc
import dash_html_components as html

from scripts import dashboard, clustering, recommendation

tab_height = '30px'

tabs_styles = {
    'height': '44px',

}

tab_style = {

    'border': '1px solid white',
    'color':'#0e0817',
    'backgroundColor': 'Gainsboro',
    'font-weight': 'bold',
    'padding': '6px'

}
tab_selected_style = {

    'backgroundColor': '#07040d',
    'color': 'white',
    'font-weight': 'bold',
    'padding': '6px'

}

def create_tab():
    '''
    This function creates the layout where the tabs are going to be
    displayed in the dash.
    '''
    return dcc.Tabs(
        id="tabs",
        value='Dashboard',
        children=[
            dcc.Tab(label='Dashboard', value='Dashboard', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Clustering', value='Clustering', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Recommendation', value='Recommendation', style=tab_style, selected_style=tab_selected_style)
        ],
    style=tabs_styles
    )

def create_content_tab(tab_name):
    '''
    This function calls the render of each tab that is in the system
    '''
    if tab_name == 'Dashboard':
        return dashboard.create_dashboard()
    elif tab_name == 'Clustering':
        return clustering.create_clustering()
    elif tab_name == 'Recommendation':
        return recommendation.create_recommendation()