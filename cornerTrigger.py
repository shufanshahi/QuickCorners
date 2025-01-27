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



def monitor_cursor():
    while True:
        x, y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()

        if x <= CORNER_THRESHOLD and y <= CORNER_THRESHOLD:
            callback("upper_left")
            time.sleep(1)
        elif x <= CORNER_THRESHOLD and y >= screen_height - CORNER_THRESHOLD:
            callback("lower_left")
            time.sleep(1)
            
        time.sleep(0.1)