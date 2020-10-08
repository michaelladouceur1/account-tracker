# Third Party Imports
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Local Imports
from gui.app import app

@app.callback(
    Output('positions-modal','is_open'),
    [Input('positions-card','n_clicks')],
    [State('positions-modal','is_open')],
)
def open_dashboard_positions(n, is_open):
    if n:
        return not is_open
    return is_open