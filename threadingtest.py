import threading
import time
from pynput.keyboard import Controller, Key
import pyautogui
keyboard = Controller()
from pixelcolor import get_pixel_color
import subprocess


class PixelChangeChecker(threading.Thread):
    def __init__(self, x, y, target_color, timeout):
        super().__init__()

        self.x = x
        self.y = y
        self.target_color = target_color
        self.timeout = timeout

        self.pixel_changed = False

    def run(self):
        start_time = time.time()

        while time.time() - start_time < self.timeout:
            current_color = get_pixel_color(self.x, self.y)
            if current_color != self.target_color:
                self.pixel_changed = True
                break

class DownKeyPresser(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while not pixel_change_checker.pixel_changed:
            keyboard.press(Key.down)
            time.sleep(0.01)

pixel_change_checker = PixelChangeChecker(838, 438,(243, 239, 234), 5)
down_key_presser = DownKeyPresser()

time.sleep(2)

pixel_change_checker.start()
down_key_presser.start()

pixel_change_checker.join()
down_key_presser.join()

if pixel_change_checker.pixel_changed:
    print("Pixel changed color.")
else:
    print("Timeout reached.")