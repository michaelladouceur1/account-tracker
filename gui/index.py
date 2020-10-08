# Third Party Imports
import dash_core_components as dcc
import dash_html_components as html 

# Local Imports
from gui.app import app
from gui import body
from gui import callbacks

app.layout = html.Div([
    body.page
])