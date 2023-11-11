import numpy as np
import puzzles as pz

class Tetris:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size

        self.board = np.zeros((self.height, self.width), dtype=np.int8)
        self.current_piece = None
        self.next_piece = None
        self.score = 0
        self.puzzle = pz.Puzzle()
        
    def place_dispo(self, dispo: np.ndarray) -> tuple:
        width = len(dispo)
        height = len(dispo[0])
        
        for x in (0, 12 - width):
            for y in range(0, 20 - height):
                pass
                

    def generate_max(self, piece: str, x: int, y: int) -> tuple:
        dispositions = self.puzzle.dp.get(piece)
        
        # (score, dispo, (x, y))
        result = None
        
        for dispo in dispositions:
            tmp = self.place_dispo(dispo)

            if result[0] < tmp[0]:
                result = tmp
                
        return result
    
    def get_score(self, dispo: np.ndarray, x: int, y: int) -> int:
        pass