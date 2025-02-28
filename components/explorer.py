from edifice import component, use_state,HBoxView, VBoxView, VScrollView, Label, Button

from db.connector import Connector
from styles.explorer import explorer_wrapper, left, inner_height, explorer_window, explorer_item

@component
def Explorer(self, conn:Connector):
    with HBoxView(style=explorer_wrapper):
        with VBoxView(style={**left, **inner_height}):
            with VScrollView(style=explorer_window):
                for db in conn.structure.databases:
                    Label(db.name, style=explorer_item)
                    for table in db.tables:
                        Label(f'  {table.name}', style=explorer_item)
