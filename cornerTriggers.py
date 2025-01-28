import pyautogui
from pynput.keyboard import Controller , Key
import time



keyboard = Controller()
CORNER_THRESHOLD = 10



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



def monitor_cursor(stop_flag):

    avoid_repeated_triggers =  True

    while not stop_flag['isRunning']:
        x, y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()

        if x <= CORNER_THRESHOLD and y <= CORNER_THRESHOLD and avoid_repeated_triggers:
            callback("upper_left")
            avoid_repeated_triggers = False
        elif x <= CORNER_THRESHOLD and y >= screen_height - CORNER_THRESHOLD and avoid_repeated_triggers:
            callback("lower_left")
            avoid_repeated_triggers = False
        elif not (x <= CORNER_THRESHOLD and y <= CORNER_THRESHOLD) and not (x <= CORNER_THRESHOLD and y >= screen_height - CORNER_THRESHOLD) and not avoid_repeated_triggers:
            avoid_repeated_triggers = True
            
        time.sleep(0.1)