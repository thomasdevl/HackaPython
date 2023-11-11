import numpy as np
import puzzles as pz

class Tetris:
    def __init__(self, width=12, height=20):
        self.width = width
        self.height = height
        
        self.weight_height = 1
        self.weight_hole = 1

        self.board = np.zeros((self.height, self.width), dtype=np.int8)
        self.score = 0
        self.puzzle = pz.Puzzle()

    def add_piece(self, piece: str):
        best_result = self.generate_max(piece)
        # print("Best result:", best_result)
        self.place_piece(best_result[1], best_result[2][0], best_result[2][1])
        return (best_result[2],[arr.tolist() for arr in best_result[1][0]])

    def check_position(self, limit: tuple, x: int, y: int) -> bool:
        # print("Limit:", limit)
        # print("Pos:", x, y)
        if y + 1 == self.height:
            return False
        
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

        index_constraint = np.argmin(limit)

        best = None
        
        for x in range(0, self.width - width):
            for y in range(0+height-1, self.height):
                # print("x, y:", x, y)

                if not self.check_position(limit, x, y):
                    score = self.get_score(shape, limit, x, y)
                    
                    if best == None or score > best[0]:
                        best = (score, dispo, (x, y))
                        # print("Best:", best)
                    
                    break
                
        return best             
                

    def generate_max(self, piece: str) -> tuple:
        dispositions = self.puzzle.dp.get(piece)
        
        # (score, dispo, (x, y))
        result = (-np.inf, None, None)
        
        for dispo in dispositions:
            tmp = self.place_dispo(dispo)
            # print("Tmp:", tmp)
            # print("Result:", result)
            if result[0] < tmp[0]:
                result = tmp
                
        return result
    
    def get_score(self, shape: tuple, limit: tuple, x: int, y: int) -> int:
        nholes = 0
        ncases_beyond = y
        nContacts = 0
    
        width = len(shape)
        height = len(shape[0])

        for k in range(len(limit)):
            j = x + k
            
            yp = y - limit[k] + 1
            if yp == self.height or self.board[yp][x + k]:
                nContacts += 1
            
            for i in range(y - limit[k] + 1, self.height):
                if self.board[i][j] == 0:
                    nholes += 1
                    
        ncases_beyond *= self.weight_height
        nholes *= self.weight_hole
                    
        return ncases_beyond - nholes + nContacts

    def place_piece(self, position: tuple, x: int, y: int):
        # position = (dis, (x, y))
        shape = position[0]
        height = len(shape)
        width = len(shape[0])

        # print("Placed piece: \n", shape)
        # print("Placed at:", x, y)

        for i in range(height-1, -1, -1):
            for j in range(width-1, -1, -1):
                if shape[i][j] != 1:
                    continue

                self.board[y + i - height + 1][x + j] = 1
                
                if np.sum(self.board[y-j]) == self.width:
                    self.update_line(x+width-i)
                        
    def update_line(self, line: int):
        for i in range(line, 0, -1):
            self.board[i] = self.board[i-1]
        self.board[0] = np.zeros((1, self.width), dtype=np.int8)

    def print_board(self):
        print(self.board)
        
# if __name__ == "__main__":        
#     t = Tetris(4, 4)
    
#     t.board = [
#         [0, 0, 0, 0],
#         [1, 0, 0, 0],
#         [1, 0, 1, 0],
#         [1, 1, 1, 0]
#     ]
    
#     print(t.get_score(
#         [[1, 0],
#          [1, 1],
#          [1, 0]],
#         [0, 1],
#         1, 2
#     ))
    
#     print(t.get_score(
#         [[1, 0, 0],
#          [1, 1, 1]],
#         [0, 0, 0],
#         1, 1
#     ))
    
#     print(t.get_score(
#         [[1, 1, 1, 1]],
#         [0, 0, 0, 0],
#         0, 0
#     ))