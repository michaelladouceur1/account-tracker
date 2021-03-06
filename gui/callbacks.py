# Third Party Imports
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Local Imports
from gui.app import app
from utils.router import Router

router = Router()

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

# open_research_modal
@app.callback(
    Output('research-modal','is_open'),
    [Input('research-button','n_clicks')],
    [State('research-modal','is_open')],
)
def open_research_modal(n, is_open):
    if n:
        return not is_open
    return is_open

# open_download_modal
@app.callback(
    Output('download-modal','is_open'),
    [Input('download-button','n_clicks')],
    [State('download-modal','is_open')],
)
def open_download_modal(n, is_open):
    if n:
        return not is_open
    return is_open

# open_settings_modal
@app.callback(
    Output('settings-modal','is_open'),
    [Input('settings-button','n_clicks')],
    [State('settings-modal','is_open')],
)
def open_settings_modal(n, is_open):
    if n:
        return not is_open
    return is_open


# DOWNLOAD
@app.callback(
    Output('download-symbol-dropdown','options'),
    [Input('download-sector-dropdown','value')]
)
def filter_symbols_by_sector(value):
    return router.update_download_symbols_dropdown(value)