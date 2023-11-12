import pyautogui

# get color of pixel poitend by the mouse
while 1:
    x, y = pyautogui.position()
    print(pyautogui.screenshot().getpixel((x, y)))
    