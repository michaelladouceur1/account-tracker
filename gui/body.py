# Third Party Imports
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_table
from dash.dependencies import Input, Output

# Local Imports
from gui.app import app

# DASHBOARD

page = html.Div(children=[
    dbc.Row([

        # DASHBOARD
        dbc.Col([
            html.Div([
                html.P('Account Balance', className='label'),
                html.H4('$3203.71')
            ], className='dashboard-element-div'),
            html.Div([
                html.P('Account Balance', className='label'),
                html.H4('$3203.71')
            ], className='dashboard-element-div')
        ], id='dashboard-container', width='auto'),

        # BODY
        dbc.Col([
            html.P('Main Body')
        ], id='body-container')
    ])
])

# dashboard = html.Div(children=[
#     dbc.Row([
#         dbc.Col([
#             html.Div([
#                 html.P('Account Balance'),
#                 html.H4('$3203.71')
#             ], className='column')
#         ]),
#         dbc.Col([
#             html.Div([
#                 html.P('Account Balance'),
#                 html.H4('$3203.71')
#             ], className='column')
#         ])
#     ])
# ], id='dashboard-container')