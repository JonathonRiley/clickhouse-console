from edifice import (App, HBoxView, VScrollView, Label, 
                     Window, component, Button, use_state)

from components.explorer import Explorer
from components.styles import *

@component
def MyApp(self):
    with Window(title="Clickhouse Console", style=app_window):
        Explorer()

if __name__ == "__main__":
    App(MyApp()).start()