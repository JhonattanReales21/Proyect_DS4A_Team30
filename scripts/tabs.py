import dash_core_components as dcc
import dash_html_components as html

from scripts import dashboard, analysis, segmentation

def create_tab():

    return dcc.Tabs(
        id="tabs",
        value='Dashboard',
        children=[
            dcc.Tab(label='Dashboard', value='Dashboard'),
            dcc.Tab(label='Analysis', value='Analysis'),
            dcc.Tab(label='Segmentation', value='Segmentation')
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