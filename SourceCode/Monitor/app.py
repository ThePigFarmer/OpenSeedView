import eel as eel
import os as os
import micro as micro
import aog as aog

gui_folder = os.path.dirname(os.path.realpath(__file__))+'\web'
eel.init(gui_folder)


@eel.expose
def update_gui():
    print('updating gui')


@eel.expose
def row_count():
    print('js wants row count')
    return micro.imp['row_count']

eel.start('index.html')