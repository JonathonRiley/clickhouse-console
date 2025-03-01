from edifice import component, use_state, HBoxView, VBoxView, VScrollView, Label, Button

from db.structure import *
from db.connector import Connector
from styles.explorer import *

@component
def Explorer(self, conn:Connector):
    with HBoxView(style={**explorer_wrapper, **left, **inner_height}):
        with VScrollView(style={**top, **explorer_window, 'background-color':'white'}):
            for db in conn.structure.databases:
                DatabaseButton(conn, db)

@component
def DatabaseButton(self, conn:Connector, db:Database):
    show_tables, set_show_tables = use_state(False)
    with VBoxView():
        Button(title=db.name,
               style=explorer_button,
               on_click=lambda _ : set_show_tables(not show_tables))
        if show_tables:
            if db.tables is None:
                tables = conn.tables(db.name)
                db.tables = [Table(table_name) for table_name in tables.name.to_list()]
            for table in db.tables:
                TableButton(conn, table, db.name)
        
@component
def TableButton(self, conn:Connector, table:Table, database_name:str):
    show_details, set_show_details = use_state(False)
    with VBoxView():
        Button(title=f'{" "*6}-> {table.name}',
                style=explorer_button,
                on_click=lambda _ : set_show_details(not show_details))
        if show_details:
            if table.columns is None:
                details = conn.describe(table.name, database_name)
                table.columns = [Column(*column) for column in details.values]
            for column in table.columns:
                Label(text=f'\t* {column.name} : {column.type}', style=explorer_item)
