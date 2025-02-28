from edifice import component, use_state,HBoxView, VBoxView, VScrollView, Label, Button

from .styles import *

@component
def Explorer(self):
    show_explorer, set_show_explorer = use_state(True)
    
    with HBoxView(style={**debug, **explorer_wrapper}):
        with VBoxView(style={'align':'left',}):
            if show_explorer:
                Button("<", 
                        style=expander_button,
                        on_click=lambda _: set_show_explorer(False))
                with VScrollView(style=explorer_window):
                    Label("Nav Item 1")
                    Label("Nav Item 2")
                    Label("Nav Item 3")
            else:
                Button(">",
                        style=expander_button,
                        on_click=lambda _: set_show_explorer(True))
