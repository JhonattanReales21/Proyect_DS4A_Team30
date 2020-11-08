import dash_core_components as dcc
import dash_html_components as html

from scripts import dashboard, analysis, segmentation

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'color':'#0e0817',
    'font-weight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#07040d',
    'color': 'white',
    'font-weight': 'bold'
}

def create_tab():

    return dcc.Tabs(
        id="tabs",
        className="custom-tab",
        value='Dashboard',
        children=[
            dcc.Tab(label='Dashboard', value='Dashboard', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Analysis', value='Analysis', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Segmentation', value='Segmentation', style=tab_style, selected_style=tab_selected_style)
        ],
        colors={
            "border": "white",
            "primary": "white",
            "background": "Gainsboro"
        }
    )

def create_content_tab(tab_name):
    if tab_name == 'Dashboard':
        return dashboard.create_dashboard()
    elif tab_name == 'Analysis':
        return analysis.create_analysis()
    elif tab_name == 'Segmentation':
        return segmentation.create_segmentation()