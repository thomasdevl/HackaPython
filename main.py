import pyautogui
import numpy as np
import time
from rotation_dict import rot_dic
from Tetris import Tetris

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
        self.Tetris = Tetris()

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
        time.sleep(0.5)
        self.click(945,209)
        self.current_piece = self.get_pixel_color(self.first_piece_x, self.first_piece_y)
        self.next_piece = self.get_pixel_color(self.next_piece_x, self.next_piece_y)
        print(f"first piece type {self.color_to_piece[self.current_piece]}")
        print(f"next piece type {self.color_to_piece[self.next_piece]}")

        if self.color_to_piece[self.current_piece] == 'S' or self.color_to_piece[self.current_piece] == 'Z':
            print("bad start")
            self.start_game()


    def play(self):
        # caclulate the best move
        data = self.Tetris.add_piece(self.color_to_piece[self.current_piece])
        
        # execute the best move
        move = self.calculate_moves(data)
        rot = rot_dic[str(data[1]).replace(" ", "")][1]
        self.move_piece(move, rot)

        # update the current and next piece
        time.sleep(1)
        self.current_piece = self.next_piece
        self.next_piece = self.get_pixel_color(self.next_piece_x, self.next_piece_y)
        self.play()

        
    def calculate_moves(self, data):
        lst_str = str(data[1]).replace(" ", "")
        decalage = rot_dic[lst_str][0]
        return 5 + decalage - data[0][0]
    
    def move_piece(self, move, rot):
        print(self.color_to_piece[self.current_piece])

        print(f"rotating {rot} times")
        for _ in range(rot):
            pyautogui.keyDown('up')
            time.sleep(0.05)

        if 0 < move:
            print(f"moving {abs(move)} left")
            for _ in range(abs(move)):
                pyautogui.keyDown('left')
                time.sleep(0.05)
        elif 0 > move:
            print(f"moving {abs(move)} right")
            for _ in range(abs(move)):
                pyautogui.keyDown('right')
                time.sleep(0.05)
        
        print("dropping")
        pyautogui.keyDown('space')

        print(self.Tetris.print_board())

        

if __name__ == '__main__':

    time.sleep(2)
    
    bot = TetrisBot()
    bot.start_game()

    bot.play()