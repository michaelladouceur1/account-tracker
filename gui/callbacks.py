# Third Party Imports
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import json

# Local Imports
from gui.app import app

@app.callback(
    Output('position-collapse','is_open'),
    [Input('position-open','n_clicks')],
    [State('position-collapse','is_open')],
)
def open_dashboard_positions(n, is_open):
    if n:
        return not is_open
    return is_open