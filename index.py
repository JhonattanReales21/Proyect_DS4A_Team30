# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Recall app
from app import app

###########################################################
#
#           APP LAYOUT:
#
###########################################################

# LOAD THE DIFFERENT FILES
from scripts import title, sidebar, Col_map, stats, tabs
from data_fetch import get_views

# PLACE THE COMPONENTS IN THE LAYOUT
app.layout = html.Div(
    [Col_map.create_map(), stats.create_stats(), title.create_title(), sidebar.create_sidebar(), tabs.create_tab()],
    className="ds4a-app",  # You can also add your own css files by locating them into the assets folder
)

###############################################
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
# Load and modify the data that will be used in the app.
#################################################################



#############################################################
# SCATTER & LINE PLOT : Add sidebar interaction here
#############################################################


#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)