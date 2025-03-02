from .generic import *
from styles.query_box import query_wrapper

size = {'width':'565px', 
        'height':'285px',
        }

color = {
    'color':'black',
    'background-color':'white',
}

results_wrapper = { 
    **size,
    **color,
    'font-size':'10px',
    'padding':'1px',
    'margin':'1px',
    'align': 'center'
}

blank_box = {
    **size,
    **color,
    'align': 'center'

}

error_box = {
    **size,
    **color,
    'padding':'0px',
    'margin':'5px',
    'align':'top',
    'font-size':'10px',
    }

grid_item = {
    'color':'black',
    'padding':'5px',
    'font-size':'10px',
}
header_style = {
    **grid_item,
    'background-color':'lightgrey',
    'border':'1px solid black',
}
row_style = {
    **grid_item,
    'background-color':'white',
    'border':'1px solid grey',
}
