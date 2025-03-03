from typing import List, Callable

from edifice import (VBoxView, HBoxView, Dropdown, 
                     use_state, Label, component)

from styles.results import *
from components.results import BlankResults, ErrorResults

CHARTS = ['Bar', 'Line', 'Scatter']


@component
def ChartResults(self, data:List[dict]):
    chart_type, set_chart_type = use_state(0)
    x, set_x = use_state(0)
    y, set_y = use_state(0)
    group_, set_group_ = use_state(0)


    with HBoxView(style=results_wrapper):
        if data is None:
            BlankResults('No data')
        elif type(data) == str:
            ErrorResults(data)
        elif type(data) == list:
            Chart(data)
        ChartDetails(list(data[0].keys()) if data else [], 
                     chart_type, set_chart_type, 
                     x, set_x, 
                     y, set_y, 
                     group_, set_group_)
        

def update_graph(setter:Callable,
                 set_value:int):
    setter(set_value)
    pass


@component
def ChartDetails(self,
                 data_cols: List[str],
                 chart_type:int,
                 set_chart_type:Callable,
                 x:int,
                 set_x:Callable,
                 y:int,
                 set_y:Callable,
                 group_:int,
                 set_group_:Callable):
    with VBoxView():
        Label(text='Chart Details')
        Label(text='Chart Type')
        Dropdown(selection = ['--'] + CHARTS, on_select=lambda x: update_graph(set_x, x, chart_type, x, y, group_))
        Label(text='X Axis')
        Dropdown(selection = ['--'] + data_cols, on_select=lambda x: update_graph(set_x, x, chart_type, x, y, group_))
        Label(text='Y Axis')
        Dropdown(selection = ['--'] + data_cols, on_select=lambda y: update_graph(set_y, y, chart_type, x, y, group_))
        Label(text='Group By')
        Dropdown(selection = ['--'] + data_cols, on_select=lambda group_: update_graph(set_group_, group_, chart_type, x, y, group_))


@component
def Chart(self, data:List[dict]):
    with HBoxView():
        Label(text='Chart')