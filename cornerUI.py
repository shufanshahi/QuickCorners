import pystray
import PIL.Image
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
        print("Starting cursor monitoring...")
        monitor_thread = Thread(target=run_monitor, daemon=True)
        monitor_thread.start()



def stop_monitoring():
    global running, stop_flag
    stop_flag['isRunning'] = True  
    running = False
    print("Stopping cursor monitoring...")



def on_clicked(icon, item):
    if str(item) == "Start":
        start_monitoring()
    elif str(item) == "Stop":
        stop_monitoring()
    elif str(item) == "Exit":
        stop_monitoring()
        icon.stop()



def run_monitor():
    monitor_cursor(stop_flag)



def run_ui():
    image = PIL.Image.open("./images/logo.png")
    icon = pystray.Icon("QuickCorners", image, menu=pystray.Menu(
        pystray.MenuItem("Start", on_clicked),
        pystray.MenuItem("Stop", on_clicked),
        pystray.MenuItem("Exit", on_clicked)
    ))
    icon.run()