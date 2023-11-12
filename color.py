import pyautogui
import time

# get color of pixel poitend by the mouse
while 1:
    # print the time well formated
    
    x, y = pyautogui.position()
    print(pyautogui.screenshot().getpixel((x, y)))
    