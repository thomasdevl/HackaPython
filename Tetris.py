import numpy as np
import puzzles as pz
import copy as cp

class Tetris:
    def __init__(self, width=12, height=20, weight_y=2, weight_hole=4, weight_contact=1, weight_burn=6):
        self.width = width
        self.height = height

        self.next_piece = None
        
        self.weight_y = weight_y
        self.weight_hole = weight_hole
        self.weight_contact = weight_contact
        self.weight_burn = weight_burn

        self.board = np.zeros((self.height, self.width), dtype=np.int8)
        self.score = 0
        self.puzzle = pz.Puzzle()

        self.tetris_mode = True
        self.burn_mode = False

        self.burned_lines = 0
        
        self.burner = np.array(((1,), (1,), (1,), (1,)), np.uint8)

    def add_piece(self, piece: str, next_piece: str):
        """
        pre: the argument piece here is a character identificator of the piece
        post: place the piece in the board as best as possible
        """
        self.next_piece = next_piece
        best_result = self.generate_max(piece)
    
        
        if best_result != None:
            self.place_piece(best_result[1], best_result[2][0], best_result[2][1], True)

        # print("Best score:", best_result[0])

        return (best_result[2],[arr.tolist() for arr in best_result[1][0]])


    def check_position(self, limit: tuple, x: int, y: int) -> bool:
        """
        pre: limit is a tuple where each element indicates where is the first case for a given x with y position starting from the bottom
        (x, y) the coordinates of the left-bottom corner of the piece
        post: True if there is the place to drop the pice once else False if there are obstacles
        """
        
        if y + 1 == self.height:
            return False
        
        for i in range(len(limit)):
            if self.board[y - limit[i] + 1][x + i] == 1:
                return False
            
        return True
        
        
    def place_dispo(self, dispo: tuple) -> tuple:
        """
        pre: dispo is a tuple that contains the informations of a piece
            => first is the description matrix of the piece
            => second is the limits so the list of distances between first case in the piece for a given x and the y coordinates
        post:
            A tuple that contains three informations, the best score gotten to place the piece, the piece and the coordinates of this placement
            If no places is found returns None
        """
        
        shape = dispo[0]
        limit = dispo[1]
        width = len(shape[0])
        height = len(shape)
        best = None

        xWidth = self.width - width

        if self.burn_mode or (width == 1 and height == 4):
            xWidth = self.width - width + 1
            
        
        for x in range(0, xWidth):
            for y in range(height-1, self.height):
                # print("x, y:", x, y)

                if not self.check_position(limit, x, y):
                    # The piece is placed as low as possible for a given x and it checks
                    # if this placement is better than the previous ones
                    score = self.get_score(dispo, limit, x, y)
                    
                    if best == None or score > best[0]:
                        best = (score, dispo, (x, y))
                    
                    break
                
        return best             
                

    def generate_max(self, piece: str) -> tuple:
        """
        pre: the argument piece here is a character identificator of the piece
        post:
            A tuple that contains three informations about the best place of the piece to do
                => the score, the piece and the coordinates of this placement
            If no places is found returns None
        """
        dispositions = self.puzzle.dp.get(piece)
        
        result = None
        
        for dispo in dispositions:
            tmp = self.place_dispo(dispo)

            if result == None or result[0] < tmp[0]:
                result = tmp
                
        return result
    
    def get_score(self, dispo: tuple, limit: tuple, x: int, y: int) -> int:
        nholes = 0
        ncases_beyond = y - max(limit)
        nContactsSol = 0

        for k in range(len(limit)):
            j = x + k
            
            yp = y - limit[k] + 1
            if yp == self.height or self.board[yp][x + k]:
                nContactsSol += 1
            
            for i in range(y - limit[k] + 1, self.height):
                if self.board[i][j] == 0:
                    nholes += 1
        
        nb_updated_lines = self.place_piece(dispo, x, y, False)

        resultNext = 0

        if self.next_piece != None:
            test_next = cp.deepcopy(self)
            test_next.place_piece(dispo, x, y, True)
            test_next.next_piece = None
            resultNext = test_next.generate_max(self.next_piece)[0]

        # if y >= 11:
        #     ncases_beyond *= 3
                    
        ncases_beyond *= self.weight_y
        nholes *= self.weight_hole
        nb_updated_lines += self.weight_burn * nb_updated_lines**2
                    
        return ncases_beyond - nholes + nContactsSol + nb_updated_lines + resultNext * 0.5


    def place_piece(self, position: tuple, x: int, y: int, update=False):
        # position = (dis, (x, y))
    
        shape = position[0]
        height = len(shape)
        width = len(shape[0])

        update_line = np.zeros(height, dtype=np.int8)

        for i in range(height-1, -1, -1):
            for j in range(width-1, -1, -1):
                # test += 1
                if shape[i][j] != 1:
                    continue
                
                if update:
                    self.board[y + i - height + 1][x + j] += 1
                if x + i - height +1 >= 8:
                    self.burn_mode = True
                    self.tetris_mode = False
                if np.sum(self.board[y + i - height + 1]) == self.width:
                    update_line[i] = y + i - height + 1

        if not update:
            return sum(update_line)

        for line in update_line:
            if line != 0:
                self.update_line(line) 

    def update_line(self, line: int):
        """
        pre: line an array line of the board to update
        post: update the targeted lines according the rules of the game
        """
        if self.burned_lines >= 4:
            self.burned_lines = 0
            self.burn_mode = False
            self.tetris_mode = True
            # self.weight_hole = 4

        for i in range(line, 0, -1):
            self.board[i] = self.board[i - 1]
            
        self.board[0] = np.zeros((1, self.width), dtype=np.int8)
        if self.burn_mode:
            self.burned_lines += 1

    def print_board(self):
        for i in range(self.height):
            print(i, end="\t")
            for j in range(self.width):
                if self.board[i][j] == 0:
                    print(" ", end="")
                else:
                    print(self.board[i][j], end="")
            print()
        print("\t", end="")
        for _ in range(self.width):
            print(".", end="")
        print()
        
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