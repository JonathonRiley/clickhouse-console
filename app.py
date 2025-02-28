from edifice import (App, HBoxView, VScrollView, Label, TextInputMultiline,
                     Window, component, Button, use_state)

from components.explorer import Explorer
from components.query_box import QueryInput
from styles.app import *
from db.connector import Connector
from db.configs import Config


@component
def MyApp(self):
    config, set_config = use_state(Config())
    conn, set_conn = use_state(Connector(config))
    conn.build_structure()
    with Window(title="Clickhouse Console", style=app_window):
        with HBoxView():
            Explorer(conn)
            with VScrollView(style=content_wrapper):
                QueryInput()
                


if __name__ == "__main__":
    App(MyApp()).start()