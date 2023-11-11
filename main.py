import pyautogui
from PIL import ImageGrab
from pynput import keyboard
import time

class TetrisBot:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.new_game_x, self.new_game_y = 723, 455
        self.first_piece_x, self.first_piece_y = 836, 433
        self.next_piece_x, self.next_piece_y = 696, 576
        self.color_to_piece = { (243, 176, 68): 'Z',
                                (237, 112, 45): 'Z',
                                (86, 162, 243): 'J',
                                (190, 91, 191): 'T',
                                (153, 153, 153): 'O',
                                (234, 51, 35) : 'I',
                                (243, 176, 68): 'S',
                                (101, 193, 94): 'L'}
        self.current_piece = None
        self.next_piece = None

    def get_pixel_color(self, x, y):
        if 0 <= x < self.screen_width and 0 <= y < self.screen_height:
            PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
            return PIXEL.getcolors()[0][1][:3]
        else:
            return None
        
    def click(self, x, y):
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click(x, y, duration=0.1)

    def start_game(self):
        self.click(self.new_game_x, self.new_game_y)
        pyautogui.keyDown('enter')
        self.current_piece = self.get_pixel_color(self.first_piece_x, self.first_piece_y)
        self.next_piece = self.get_pixel_color(self.next_piece_x, self.next_piece_y)
        print(f"first piece color {self.current_piece}: type {self.color_to_piece[self.current_piece]}")
        print(f"next piece color {self.next_piece}: type {self.color_to_piece[self.next_piece]}")

    def play(self):
        pass


if __name__ == '__main__':

    time.sleep(2)
    
    bot = TetrisBot()
    bot.start_game()