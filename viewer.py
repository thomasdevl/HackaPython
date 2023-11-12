import numpy as np
from time import sleep
from random import randint
import Tetris

t = Tetris.Tetris()

pieces = list(t.puzzle.dp.keys())
print(pieces)

def print_board(t: Tetris.Tetris, piece: str):
    copy = np.zeros((t.height, t.width), np.uint8)
    
    for i in range(t.height):
        for j in range(t.width):
            copy[i][j] = t.board[i][j]
            
    value = t.add_piece(piece)
    
    for i in range(t.height):
        print("{", end="")
        
        for j in range(t.width):
            if copy[i][j] == t.board[i][j]:
                if t.board[i][j] == 1:
                    print("[{1}{0}{2}]".format(t.board[i][j], "\033[91m", "\033[0m"), end="")
                else:
                    print("[{0}]".format(t.board[i][j]), end="")
            else:
                print("[{1}{0}{2}]".format(t.board[i][j], "\033[93m", "\033[0m"), end="")
        
        print("}")
                
    print("Add =>\n", t.puzzle.dp.get(piece)[0][0])

    return value

value = 0
i = 0

def isValid(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] not in (0, 1):
                return False
    return True

while isValid(t.board):
    print_board(t, pieces[randint(0, len(pieces) - 1)])
    print("Score : ", t.score)
    sleep(0.001)
    i += 1
    
print("Loops count ==> ", i)