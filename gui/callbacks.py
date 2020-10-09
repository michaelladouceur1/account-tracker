# Third Party Imports
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Local Imports
from gui.app import app

# open_metrics_modal
@app.callback(
    Output('metrics-modal','is_open'),
    [Input('metrics-button','n_clicks')],
    [State('metrics-modal','is_open')],
)
def open_metrics_modal(n, is_open):
    if n:
        return not is_open
    return is_open

# open_watchlist_modal
@app.callback(
    Output('watchlist-modal','is_open'),
    [Input('watchlist-button','n_clicks')],
    [State('watchlist-modal','is_open')],
)
def open_watchlist_modal(n, is_open):
    if n:
        return not is_open
    return is_open