import pyautogui
import time
from rotation_dict import rot_dic
from Tetris import Tetris
from config import *

pyautogui.PAUSE = 0

class TetrisBot:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.new_game_x, self.new_game_y = new_game_x, new_game_y
        self.first_piece_x, self.first_piece_y = first_piece_x, first_piece_y
        self.next_piece_x, self.next_piece_y = next_piece_x, next_piece_y
        self.color_to_piece = { Z_1: 'Z',
                                Z_2: 'Z',
                                J: 'J',
                                T: 'T',
                                O: 'O',
                                I : 'I',
                                S: 'S',
                                L: 'L'}
        self.current_piece = None
        self.next_piece = None
        self.Tetris = Tetris()
        self.yellow = Bg_Yellow
        self.game_over_coord = (game_over_x, game_over_y)
        self.game_over_color = game_over_color

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
        time.sleep(1)
        self.click(accept_x,accept_y)
        time.sleep(0.5)
        self.current_piece = self.get_pixel_color(self.first_piece_x, self.first_piece_y)
        self.next_piece = self.get_pixel_color(self.next_piece_x, self.next_piece_y)
        #print(f"first piece type {self.color_to_piece[self.current_piece]}")
        #print(f"next piece type {self.color_to_piece[self.next_piece]}")

        if self.color_to_piece[self.current_piece] == 'S' or self.color_to_piece[self.current_piece] == 'Z':
            print("bad start")
            self.start_game()

    def wait_for_pixel_change(self, x, y, target_color, timeout):
        start_time = time.time()

        while time.time() - start_time < timeout:
            current_color = self.get_pixel_color(x, y)
            if current_color != target_color:
                return True  

            time.sleep(0.05)  

        # Timeout
        return False  



    def play(self):
        # caclulate the best move
        try:
            # start_time = time.time()
            data = self.Tetris.add_piece(self.color_to_piece[self.current_piece], self.color_to_piece[self.next_piece])
            # print(f"Time to calculate: {time.time() - start_time}s")
        except KeyError:
            self.game_over()
            return False
 
        # execute the best move
        move = self.calculate_moves(data)
        
        rot = rot_dic[str(data[1]).replace(" ", "")][1]
        self.move_piece(move, rot)

        # update the current and next piece
        self.wait_for_pixel_change(self.first_piece_x, self.first_piece_y, self.yellow, 1)
        self.current_piece = self.next_piece
        self.next_piece = self.get_pixel_color(self.next_piece_x, self.next_piece_y)

        #print(self.get_pixel_color(game_over_x, game_over_y))
        if self.get_pixel_color(game_over_x, game_over_y) == game_over_color:
            self.game_over()
            return False
        
        return True

    def game_over(self):
        time.sleep(1)
        print("Game over")
        real_time = str(time.strftime("%H:%M:%S", time.localtime()))
        pyautogui.write(f"HqckqPython ")
        pyautogui.press('enter')
        time.sleep(1)
        return

        
    def calculate_moves(self, data):
        lst_str = str(data[1]).replace(" ", "")
        decalage = rot_dic[lst_str][0]
        return 5 + decalage - data[0][0]
    
    def move_piece(self, move, rot):
        #print(self.color_to_piece[self.current_piece])

        for _ in range(rot):
            pyautogui.keyDown('up')

        if 0 < move:
            for _ in range(abs(move)):
                pyautogui.press('left', presses=1)
        elif 0 > move:
            for _ in range(abs(move)):
                pyautogui.press('right', presses=1)
        
        pyautogui.keyDown('space')


        

if __name__ == '__main__':

    time.sleep(2)

    for _ in range(10): 
        bot = TetrisBot()
        bot.start_game()

        bool_value = True
        i = 0
        while bool_value:
            # print(f"Pieces: {i}")
            bool_value = bot.play()
            i += 1    