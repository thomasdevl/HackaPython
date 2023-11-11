import pyautogui
from PIL import ImageGrab
from pynput import keyboard
import time

# TO DEFINE ACCORDING TO THE SCREEN 
new_game_x, new_game_y = 723, 455

first_piece_x, first_piece_y = 836, 433
next_piece_x, next_piece_y = 696, 576

color_to_piece = {(243, 176, 68): 'Z',
          (237, 112, 45): 'Z',
          (86, 162, 243): 'J',
          (190, 91, 191): 'T',
          (153, 153, 153): 'O',
          (234, 51, 35) : 'I',
          (243, 176, 68): 'S',
          (101, 193, 94): 'L'}

def get_pixel_color(x, y):
    if 0 <= x < screen_width and 0 <= y < screen_height:
        PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
        return PIXEL.getcolors()[0][1][:3]
    else:
        return None
    
def click(x, y):
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(x, y, duration=0.1)
    

if __name__ == '__main__':

    time.sleep(2)
    
    screen_width, screen_height = pyautogui.size()

    # start the game    
    click(new_game_x, new_game_y)
    pyautogui.keyDown('enter')

    # get pixel color of the first piece
    next_piece_color = get_pixel_color(first_piece_x, first_piece_y)
    print(f"first piece color {next_piece_color}")
    print(f"type {color_to_piece[next_piece_color]}")

    # get pixel color of the next key
    next_piece_color = get_pixel_color(next_piece_x, next_piece_y)
    print(f"next piece color {next_piece_color}")
    print(f"type {color_to_piece[next_piece_color]}")