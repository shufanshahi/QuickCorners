import pystray
import PIL.Image
from threading import Thread
import pyautogui
from pynput.keyboard import Controller , Key
import time

keyboard = Controller()
CORNER_THRESHOLD = 10
running = False
monitor_thread = None
stop_flag = False



def trigger_hotkey(hotkey):
    if hotkey == "tab":
        hotkey = Key.tab
    elif hotkey == "d":
        hotkey = "d"
        
    with keyboard.pressed(Key.cmd):
        keyboard.press(hotkey)
        keyboard.release(hotkey)



def callback(action):
    if action == "upper_left":
        trigger_hotkey("tab")
    elif action == "lower_left":
        trigger_hotkey("d")



def monitor_cursor():
    while not stop_flag:
        x, y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()

        if x <= CORNER_THRESHOLD and y <= CORNER_THRESHOLD:
            callback("upper_left")
            time.sleep(1)
        elif x <= CORNER_THRESHOLD and y >= screen_height - CORNER_THRESHOLD:
            callback("lower_left")
            time.sleep(1)
            
        time.sleep(0.1)



def start_monitoring():
    global running, stop_flag, monitor_thread
    if not running:
        stop_flag = False 
        running = True
        print("Starting cursor monitoring...")
        monitor_thread = Thread(target=monitor_cursor, daemon=True)
        monitor_thread.start()



def stop_monitoring():
    global running, stop_flag
    stop_flag = True  
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



def run_ui():
    image = PIL.Image.open("./images/logo.png")
    icon = pystray.Icon("QuickCorners", image, menu=pystray.Menu(
        pystray.MenuItem("Start", on_clicked),
        pystray.MenuItem("Stop", on_clicked),
        pystray.MenuItem("Exit", on_clicked)
    ))
    icon.run()