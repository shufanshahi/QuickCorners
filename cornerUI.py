import pystray
import PIL.Image
from PIL import Image
import os
import sys
from threading import Thread
from cornerTriggers import monitor_cursor



running = False
monitor_thread = None
stop_flag = {'isRunning' : False}



def start_monitoring():
    global running, stop_flag, monitor_thread
    if not running:
        stop_flag['isRunning'] = False 
        running = True
        print("Starting cursor monitoring.....")
        monitor_thread = Thread(target=run_monitor, daemon=True)
        monitor_thread.start()



def stop_monitoring():
    global running, stop_flag
    stop_flag['isRunning'] = True  
    running = False
    print("Stopping cursor monitoring.....")



def on_clicked(icon, item):
    if str(item) == "Start":
        start_monitoring()
    elif str(item) == "Stop":
        stop_monitoring()
    elif str(item) == "Exit":
        stop_monitoring()
        print("Program exiting................")
        icon.stop()



def run_monitor():
    monitor_cursor(stop_flag)

def resource_path(relative_path):
    """ Get the absolute path to a resource bundled with the app. """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

logo_path = resource_path("images/logo.png")
image = Image.open(logo_path)


def run_ui():
    print("Program running................")
    icon = pystray.Icon("QuickCorners", image, menu=pystray.Menu(
        pystray.MenuItem("Start", on_clicked),
        pystray.MenuItem("Stop", on_clicked),
        pystray.MenuItem("Exit", on_clicked)
    ))
    icon.run()