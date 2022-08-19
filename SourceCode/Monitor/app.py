import eel as eel
import os as os
import micro as micro
import aog as aog
from operator import index

gui_folder = os.path.dirname(os.path.realpath(__file__))+'\web'
eel.init(gui_folder)

def avg(list):
    avg = sum(list) / len(list)
    return avg

def index_min(list):
    return list.index(min(list))


@eel.expose
def update_gui():
    print('updating gui')
    print('current seed count per sec', micro.current_seed_count_per_second)
    


@eel.expose
def row_count():
    return micro.imp['row_count']

eel.start('index.html')
######################################################################################
