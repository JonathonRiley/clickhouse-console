

from edifice import (App, HBoxView, VScrollView, RadioButton,
                     Window, component, use_state)

from components.explorer import Explorer
from components.query_box import QueryInput
from components.results import BlankResults, ErrorResults, ResultsTable
from styles.app import *
from styles.query_box import *
from db.connector import Connector
from db.configs import Config

alphabet = 'abcdefghijklmnopqrstuvwxyz'
mock_data = [{f'col_{c}':c*(i+1) for i, c in enumerate(alphabet)} for _ in range(10)]

@component
def MyApp(self):
    config, set_config = use_state(Config())
    conn, set_conn = use_state(Connector(config))
    data, set_data = use_state(mock_data)
    display_table, set_display_table = use_state(True)
    with Window(title="Clickhouse Console", style=app_window):
        with HBoxView():
            Explorer(conn)
            with VScrollView(style=content_wrapper):
                QueryInput(conn, set_data)
                

                # Selector display type
                with HBoxView(style={'align':'center', 'height':'40px'}):
                    RadioButton(text="Table", checked=display_table, on_click=lambda _: set_display_table(True), style={'padding-right':'100px'})
                    RadioButton(text="Chart", checked=not display_table, on_click=lambda _: set_display_table(False))

                # Results
                if data is None:
                    BlankResults('No data')
                if type(data) == str:
                    ErrorResults(data)
                if type(data) == list:
                    ResultsTable(data)
                


if __name__ == "__main__":
    App(MyApp()).start()