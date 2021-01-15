from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:   #Program will not run if q is pressed
    #Change dep on coordinates of each
    click(1401,621) #searches
    time.sleep(0.5) #time to load
    click(1420,740) #buy now
    time.sleep(0.25)
    click(961,620) #press ok
    click(125,190) #press back
    time.sleep(0.5)
    click(970,774) #increase price
    click(1311,938) #searches
    time.sleep(0.5)
    click(1420,740) #buys
    time.sleep(0.25)
    click(961,620) #press ok
    click(129,190) #press back
    time.sleep(0.5)
    click(506,772) #decrease
