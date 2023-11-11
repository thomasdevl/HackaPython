import numpy as np
import puzzles as pz

class Tetris:
    def __init__(self, width=12, height=20):
        self.width = width
        self.height = height

        self.board = np.zeros((self.height, self.width), dtype=np.int8)
        self.score = 0
        self.puzzle = pz.Puzzle()

    def add_piece(self, piece: str):
        best_result = self.generate_max(piece)
        self.place_piece(best_result[1], best_result[2][0], best_result[2][1])

    def check_position(self, limit: tuple, x: int, y: int) -> bool:
        # print("Limit:", limit)
        # print("Pos:", x, y)
        if y == self.height:
            return 
        for i in range(len(limit)):
            # print(x + i, y - limit[i] + 1):
            if self.board[y - limit[i] + 1][x + i] == 1:
                return False
            
        return True
        
    def place_dispo(self, dispo: tuple) -> tuple:
        shape = dispo[0]
        limit = dispo[1]
        width = len(shape[0])
        height = len(shape)

        best = None
        
        for x in (0, self.width - width):
            for y in range(0+height, self.height):
                if self.check_position(limit, x, y):
                    score = self.get_score(shape, limit, x, y)
                    
                    if best == None or score > best[0]:
                        best = (score, dispo, (x, y))
                    continue
                else:
                    break
                
        return best             
                

    def generate_max(self, piece: str) -> tuple:
        dispositions = self.puzzle.dp.get(piece)
        
        # (score, dispo, (x, y))
        result = None
        
        for dispo in dispositions:
            tmp = self.place_dispo(dispo)

            if result[0] < tmp[0]:
                result = tmp
                
        return result

    __weight_hole_constant = 2
    @classmethod
    def set_weight_hole_constant(cls, constant):
        cls.__weight_hole_constant = constant
    
    def get_score(self, shape: tuple, limit: tuple, x: int, y: int) -> int:
        weight_hole = 0
        weight_height = len(self.board) - y - 1

        width = len(shape)
        height = len(shape[0])

        for k in range(len(limit)):
            j = x + k
            
            for i in range(y - limit[k] + 1, len(self.board)):
                if self.board[i][j] == 0:
                    weight_hole += 1
                    
        return weight_height + Tetris.__weight_hole_constant * weight_hole

    def place_piece(self, position: tuple, x: int, y: int):
        # position = (dis, (x, y))
        shape = position[0]
        height = len(shape)
        width = len(shape[0])
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] == 1:
                    self.board[x+width-i][y+height-j] = 1
                    if sum(self.board[x+width-i]) == 12:
                        self.update_line(x+width-i)
                        
    def update_line(self, line: int):
        for i in range(line, 0, -1):
            self.board[i] = self.board[i-1]
        self.board[0] = np.zeros((1, self.width), dtype=np.int8)

    def print_board(self):
        print(self.board)        
        
if __name__ == "__main__":
    t = Tetris()
    Tetris.set_weight_hole_constant(2)
    
    t.board = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0]
    ]
    
    print(t.get_score(
        [[1, 0],
         [1, 1],
         [1, 0]],
        [0, 1],
        1, 2
    ))
    
    print(t.get_score(
        [[1, 0, 0],
         [1, 1, 1]],
        [0, 0, 0],
        1, 1
    ))
    
    print(t.get_score(
        [[1, 1, 1, 1]],
        [0, 0, 0, 0],
        0, 0
    ))