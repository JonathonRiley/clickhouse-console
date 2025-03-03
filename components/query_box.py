import re
from edifice import (HBoxView, VBoxView, TextInputMultiline, Button, component, use_state)
from typing import Callable

from db.connector import Connector
from styles.query_box import *

def query_db(conn:Connector, query:str, set_data:Callable):
    clean_query = re.sub(r'\s+', ' ', query)
    try:
        data = conn.query(clean_query)
        set_data(data.to_dict(orient='records'))
    except Exception as e:
        data = str(e)
        set_data(data)


@component 
def QueryInput(self, conn:Connector, set_data:Callable):
    query, set_query = use_state("")
    with HBoxView(style=query_input):
        TextInputMultiline(text=query, on_change=set_query, style=query_wrapper )
        with VBoxView(style={'align':'bottom'}):
            Button("Run", on_click=lambda _ : query_db(conn, query, set_data), style=button_style)