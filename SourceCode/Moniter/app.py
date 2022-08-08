import eel as eel
import os as os
import hardwareinterface as micro
import agopengpsinterface as aog

gui_folder = os.path.dirname(os.path.realpath(__file__))+'\Web'
eel.init(gui_folder)


@eel.expose
def gui_thread():
    while True:
        eel.sleep(1)
        print('updating gui')


eel.spawn(gui_thread)

eel.start('index.html')


while True:
    get_speed()
