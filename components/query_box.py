import re
from edifice import (TextInputMultiline, component, use_state)

from styles.query_box import *

@component 
def QueryInput(self):
    query, set_query = use_state("")
    print(re.sub(r'\s+', ' ', query))
    TextInputMultiline(text=query, on_change=set_query, style=query_wrapper )