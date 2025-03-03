

from edifice import (App, HBoxView, VBoxView, RadioButton,Label, Button,
                     Window, component, use_state)

from components.charts import ChartResults
from components.explorer import Explorer
from components.query_box import QueryInput
from components.results import BlankResults, ErrorResults, ResultsTable
from styles.app import *
from styles.query_box import *
from db.connector import Connector
from db.configs import Config


@component
def MyApp(self):
    config, set_config = use_state(Config())
    conn, set_conn = use_state(Connector(config))
    data, set_data = use_state(None)
    page, set_page = use_state(0)
    display_table, set_display_table = use_state(True)
    with Window(title="Clickhouse Console", style=app_window):
        with HBoxView():
            Explorer(conn)
            with VBoxView(style=content_wrapper):
                QueryInput(conn, set_data)
                

                # Selector display type
                with HBoxView(style={'width':inner_width.get('width'), 'align':'left'}):
                    with HBoxView(style={'align':'center', 'height':'40px', 'width':f'{int((SIZE[1]-20)*0.5)}px'}):
                        RadioButton(text="Table", checked=display_table, on_click=lambda _: set_display_table(True), style={'padding-right':'100px'})
                        RadioButton(text="Chart", checked=not display_table, on_click=lambda _: set_display_table(False))
                    if display_table:
                        with HBoxView(style={'align':'center', 'height':'40px', 'width':f'{int((SIZE[1]-20)*0.2)}px'}):
                            Label(text=f"Page {page+1}", style={'padding-right':'10px'})
                            Button(title="Prev", on_click=lambda _: set_page(page-1) if page >0 else None, )
                            Button(title="Next", on_click=lambda _: set_page(page+1) if page < len(data)//10 else None)

                # Results
                if display_table:
                    if data is None:
                        BlankResults('No data')
                    if type(data) == str:
                        ErrorResults(data)
                    if type(data) == list:
                        ResultsTable(data, page)
                else:
                    ChartResults(data)

                    


if __name__ == "__main__":
    App(MyApp()).start()