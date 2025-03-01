from edifice import (VScrollView, HBoxView, TableGridView, TableGridRow, Label, component)

from styles.results import *

@component
def BlankResults(self, text:str):
    with HBoxView(style=results_wrapper):
        Label(text=text, style=blank_box)

@component
def ErrorResults(self, error:str):
    # with VScrollView(style={**debug,**results_wrapper}):
    Label(text=error, word_wrap=True,style = {**results_wrapper, **error_box})

@component
def ResultsTable(self, data):
    with TableGridView(style=results_wrapper):
        for i, row in data.iterrows():
            TableGridRow(row=row.to_list())