from typing import List

from edifice import (VScrollView, HBoxView, TableGridView, TableGridRow, Label, component)

from styles.results import *

@component
def BlankResults(self, text:str):
    with HBoxView(style=results_wrapper):
        Label(text=text, style=blank_box)

@component
def ErrorResults(self, error:str):
    Label(text=error, word_wrap=True,style = {**results_wrapper, **error_box})

@component
def ResultsTable(self, data:List[dict], page:int):
    page_data = data[page*10:(page+1)*10]
    cols = list(page_data[0].keys())
    widths = {col: max(10, len(str(col))) for col in cols}
    for row in page_data:
        for col in cols:
            widths[col] = max(widths[col], len(str(row[col])))
    with VScrollView(style=results_wrapper):
        with TableGridView(style={**results_wrapper, 'width': f'{sum(widths.values())*7}px', 'align':'left'}):
            with TableGridRow():
                for col in cols:
                    Label(text=col, style={**header_style})
            for idx, row in enumerate(page_data):
                with TableGridRow():
                    for col, val in row.items():
                        Label(text=str(val), style={**row_style, 'width': f'{widths[col]*6}px'}).set_key(f'{col}_{idx}')