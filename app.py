from edifice import (App, HBoxView, VScrollView, Label, TextInputMultiline,
                     Window, component, Button, use_state)

from components.explorer import Explorer
from components.query_box import QueryInput
from styles.app import *
from db.connector import Connector
from db.configs import Config

CONFIG = Config()
connector = Connector(CONFIG)
connector.build_structure()

@component
def MyApp(self):
    with Window(title="Clickhouse Console", style=app_window):
        with HBoxView():
            Explorer()
            with VScrollView(style=content_wrapper):
                QueryInput()
                


if __name__ == "__main__":
    App(MyApp()).start()