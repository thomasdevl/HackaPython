import Tetris as t
import puzzles as pz

# Test the Tetris class
Test1 = t.Tetris()
Test1.add_piece("L")
# # Test1.print_board()
<<<<<<< HEAD
# Test1.add_piece("O")
# Test1.print_board()
=======
Test1.add_piece("O")
>>>>>>> e574fcba5254cc7711b93789b08679ccf82d56a8
# Test1.add_piece("L")
# Test1.print_board()
# Test1.add_piece("L")
# Test1.print_board()
# Test1.add_piece("L")
# Test1.print_board()
# Test1.add_piece("L")
# Test1.print_board()
# Test1.add_piece("I")
# Test1.print_board()
# Test1.add_piece("I")
# Test1.add_piece("S")
# Test1.add_piece("J")
# Test1.add_piece("Z")
# Test1.add_piece("T")
# Test1.print_board()
# Test1.add_piece("I")

for i in range(12):
    Test1.add_piece("I")
    Test1.print_board()

# p = pz.Puzzle()

# print(p.T[0][0])
# Test1.place_piece(p.T[0], 4, 4)

# print(p.T[0])

Test1.print_board()