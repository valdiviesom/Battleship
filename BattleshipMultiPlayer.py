from random import randint

p1_board = []
p2_board = []

print("Let's play 2 player Battleship!")
board_size = int(input("Input board size: "))
turns = int(input("Number of allowed turns: "))
p1_name = input("Name of player 1: ")
p2_name = input("Name of player 2: ")

# initialize boards
for x in range(board_size):
    p1_board.append(["O"] * board_size)
    p2_board.append(["O"] * board_size)


def print_board(board):
    for row in board:
        print(" ".join(row))

def random_par(board):
    return randint(0, len(board) - 1)

# create boats
p1_ship_row = random_par(p1_board)
p1_ship_col = random_par(p1_board)
p1_ship = [p1_ship_row, p1_ship_col]
p2_ship_row = random_par(p2_board)
p2_ship_col = random_par(p2_board)
p2_ship = [p2_ship_row, p2_ship_col]
"""
# locations of ships for debugging
print ("%s\'s ship is at (%s,%s)" % (p1_name, p1_ship_row, p1_ship_col))
print ("%s\'s is at (%s,%s)" % (p2_name, p2_ship_row, p2_ship_col))
"""
# return whether or not the ship was sunk
def play_turn(targetBoard, targetShip, targetPlayer, playing):
    print("%s\'s guess: " % (playing))
    guess_row = int(input("   Row:"))
    guess_col = int(input("   Col:"))
    while (guess_row < 0 or guess_row > board_size-1) or (guess_col < 0 or guess_col > board_size-1):
        print("Oops, that's not even in the ocean, guess again (remember size is %s)" % (board_size))
        guess_row = int(input("   Row:"))
        guess_col = int(input("   Col:"))
    if guess_row == targetShip[0] and guess_col == targetShip[1]:
        print("Congratulations! You sunk %s\'s battleship! %s wins!" %(targetPlayer,playing))
        return True
    if targetBoard[guess_row][guess_col] == "X":
        print("You guessed that one already. Wasted Shot")
        return False
    else:
        print("%s missed %s\'s battleship!" %(playing, targetPlayer))
        targetBoard[guess_row][guess_col] = "X"
        print_board(targetBoard)
        return False


for turn in range(turns):
    print("==============  Turn ", turn + 1," =============")
    if (play_turn(p2_board, p2_ship, p2_name, p1_name)): break
    if (play_turn(p1_board, p1_ship, p1_name, p2_name)): break
    if (turn+1==turns):
        print ("Game Over, neither player could sink the other's ship")