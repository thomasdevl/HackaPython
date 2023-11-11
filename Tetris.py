import numpy as np

class Tetris:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size

        self.board = np.zeros((self.height, self.width), dtype=np.int8)
        self.current_piece = None
        self.next_piece = None
        self.score = 0





