from edifice import component, use_state,HBoxView, VBoxView, VScrollView, Label, Button

from styles.explorer import explorer_wrapper, left, inner_height, explorer_window, explorer_item

@component
def Explorer(self):
    with HBoxView(style=explorer_wrapper):
        with VBoxView(style={**left, **inner_height}):
            with VScrollView(style=explorer_window):
                for i in range(40):
                    Label(f"Nav Item {i+1}", style=explorer_item)
