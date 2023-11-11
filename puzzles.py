import numpy as np

class Puzzle:
    I =(
        (
            np.array(((1, 1, 1, 1),), np.uint8), 
            np.array((0, 0, 0, 0), np.uint8)
        ),
        (
        np.array(
            ((1,), (1,), (1,), (1,))
        , np.uint8), 
        np.array((0,), np.uint8)
        )
    )
    
    O = [(
        np.array((
            (1, 1),
            (1, 1)
        ), np.uint8), 
        np.array((0, 0), np.uint8)
        )
    ]
    
    T = (
        (
        np.array((
            (0, 1, 0),
            (1, 1, 1)
        ), np.uint8), 
        np.array((0, 0, 0), np.uint8)
        ),
        (
        np.array((
            (0, 1),
            (1, 1),
            (0, 1)
        ), np.uint8), 
        np.array((1, 0), np.uint8)
        ),
        (
        np.array((
            (1, 1, 1),
            (0, 1, 0)
        ), np.uint8), 
        np.array((1, 0, 1), np.uint8)
        ),
        (
        np.array((
            (1, 0),
            (1, 1),
            (1, 0)
        ), np.uint8), 
        np.array((0, 1), np.uint8)
        )
    )
    
    L = (
        (
        np.array((
            (1, 1, 1),
            (1, 0, 0)
        ), np.uint8), 
        np.array((0, 1, 1), np.uint8)
        ),
        (
        np.array((
            (1, 0),
            (1, 0),
            (1, 1)
        ), np.uint8), 
        np.array((0, 0), np.uint8)
        ),
        (
        np.array((
            (0, 0, 1),
            (1, 1, 1)
        ), np.uint8),
        np.array((0, 0, 0), np.uint8)
        ),
        (
        np.array((
            (1, 1),
            (0, 1),
            (0, 1)
        ), np.uint8), 
        np.array((2, 0), np.uint8)
        )
    )
    
    J = (
        (
        np.array((
            (1, 1, 1),
            (0, 0, 1)
        ), np.uint8),
        np.array((1, 1, 0), np.uint8)
        ),
        (
        np.array((
            (1, 1),
            (1, 0),
            (1, 0)
        ), np.uint8),
        np.array((0, 2), np.uint8)
        ),
        (
        np.array((
            (1, 0, 0),
            (1, 1, 1)
        ), np.uint8),
        np.array((0, 0, 0), np.uint8)
        ),
        (
        np.array((
            (0, 1),
            (0, 1),
            (1, 1)
        ), np.uint8),
        np.array((0, 0), np.uint8)
        )
    )
    
    Z = (
        (
        np.array((
            (1, 1, 0),
            (0, 1, 1)
        ), np.uint8),
        np.array((1, 0, 0), np.uint8)
        ),
        (
        np.array((
            (0, 1),
            (1, 1),
            (1, 0)
        ), np.uint8),
        np.array((0, 1), np.uint8)
        )
    )
    
    S = (
        (np.array((
            (0, 1, 1),
            (1, 1, 0)
        ), np.uint8), 
        np.array((0, 0, 1), np.uint8)
        ),
        (
        np.array((
            (1, 0),
            (1, 1),
            (0, 1)
        ), np.uint8), 
        np.array((1, 0), np.uint8)
        )
    )
    
    dp = {
        "I": I,
        "O": O,
        "T": T,
        "L": L,
        "J": J,
        "Z": Z,
        "S": S
    }

    all = []
    for key in dp.keys():
        for each in dp[key]:
            all.append(each[0])
    all = tuple(all)
    
    def play(game, piece):
        # pre : game is the tetris board and piece is a new piece to place
        # post : 
        return