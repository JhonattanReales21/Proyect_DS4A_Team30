import dash_core_components as dcc
import dash_html_components as html

from scripts import dashboard, analysis, segmentation

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
#'#07040d' - original black
#'#121212' - background black darker
tab_selected_style = {

    'backgroundColor': '#07040d',
    'color': 'white',
    'font-weight': 'bold',
    'padding': '6px'

}

def create_tab():

    return dcc.Tabs(
        id="tabs",
        value='Dashboard',
        children=[
            dcc.Tab(label='Dashboard', value='Dashboard', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Analysis', value='Analysis', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Segmentation', value='Segmentation', style=tab_style, selected_style=tab_selected_style)
        ],
    style=tabs_styles
    )

def create_content_tab(tab_name):
    if tab_name == 'Dashboard':
        return dashboard.create_dashboard()
    elif tab_name == 'Analysis':
        return analysis.create_analysis()
    elif tab_name == 'Segmentation':
        return segmentation.create_segmentation()