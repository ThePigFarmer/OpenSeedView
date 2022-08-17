import eel as eel
import os as os
import micro as micro
import aog as aog

gui_folder = os.path.dirname(os.path.realpath(__file__))+'\web'
eel.init(gui_folder)


@eel.expose
def gui_thread():
    print('updating gui')


eel.start('index.html')


while True:
    x=3
