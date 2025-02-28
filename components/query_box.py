import re
from edifice import (VBoxView, TextInputMultiline, Button, component, use_state)

from styles.query_box import *

@component 
def QueryInput(self):
    query, set_query = use_state("")
    with VBoxView(style={'width':'565px', 
                 'height':'250px',**debug}):
        TextInputMultiline(text=query, on_change=set_query, style=query_wrapper )
        Button("Run", on_click=lambda _ : print(re.sub(r'\s+', ' ', query)), style=button_style)