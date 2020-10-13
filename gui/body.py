# Third Party Imports
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import dash_table
from dash.dependencies import Input, Output

# Local Imports
from gui.app import app
from utils.router import Router

router = Router()

page = html.Div(children=[
    dbc.Row([

        # DASHBOARD
        dbc.Col([

            # GENERAL INFO
            html.Div([
                dbc.Card([
                    dbc.CardHeader(html.P('Account Balance', className='label')),
                    dbc.CardBody([
                        html.P('$3203.71')
                    ])
                ])
            ], className='dashboard-element-div'),

            # POSITIONS
            html.Div([
                dbc.Card([
                    dbc.CardHeader(html.P('Top Positions', className='label')),
                    dbc.CardBody([
                        html.P('QQQ: $276.71 (0.37%)'),
                        html.P('TSLA: $420.69 (0.31%)'),
                        html.P('GLD: $315.81 (0.27%)'),
                        html.P('FNV: $154.17 (0.26%)'),
                        html.P('SAND: $42.93 (0.15%)')
                    ])
                ], id='positions-card')
            ], id='position-div', className='dashboard-element-div'),

            # NAVIGATION
            html.Div([
                html.Button([
                    html.I(className='fas fa-chart-bar'),
                    html.Span('Metrics')
                ], id='metrics-button', className='navigation-button'),
                html.Button([
                    html.I(className='fas fa-eye'),
                    html.Span('Watchlist')
                ], id='watchlist-button', className='navigation-button'),
                html.Button([
                    html.I(className='fas fa-wave-square'),
                    html.Span('Research')
                ], id='research-button', className='navigation-button'),
                html.Button([
                    html.I(className='fas fa-arrow-circle-down'),
                    html.Span('Download')
                ], id='download-button', className='navigation-button'),
                html.Button([
                    html.I(className='fas fa-cog'),
                    html.Span('Settings')
                ], id='settings-button', className='navigation-button')
            ], className='dashboard-element-div')
        ], id='dashboard-container', width='auto'),

        # BODY
        dbc.Col([

            # METRICS MODAL
            dbc.Modal([
                dbc.ModalHeader('Metrics', className='modal-header'),
                dbc.ModalBody('POSITIONSPOSITIONSPOSITIONS')
            ], id='metrics-modal', centered=True, size='lg'),

            # WATCHLIST MODAL
            dbc.Modal([
                dbc.ModalHeader('Watchlist', className='modal-header'),
                dbc.ModalBody('POSITIONSPOSITIONSPOSITIONS')
            ], id='watchlist-modal', centered=True, size='lg'),

            # RESEARCH MODAL
            dbc.Modal([
                dbc.ModalHeader('Research', className='modal-header'),
                dbc.ModalBody('POSITIONSPOSITIONSPOSITIONS')
            ], id='research-modal', centered=True, size='lg'),

            # DOWNLOAD MODAL
            dbc.Modal([
                dbc.ModalHeader('Download', className='modal-header'),
                dbc.ModalBody([
                    dcc.Dropdown(
                        id='download-symbol-dropdown',
                        options=router.dropdown_symbols(),
                        multi=True
                    )
                ])
            ], id='download-modal', centered=True, size='lg'),

            # SETTINGS MODAL
            dbc.Modal([
                dbc.ModalHeader('Settings', className='modal-header'),
                dbc.ModalBody('POSITIONSPOSITIONSPOSITIONS')
            ], id='settings-modal', centered=True, size='lg'),

            html.P('Main Body'),
        ], id='body-container')
    ])
])