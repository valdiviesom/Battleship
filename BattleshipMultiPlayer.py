from random import randint

board1 = []
board2 = []

print("Let's play 2 player Battleship!")
size = int(input("Input board size: "))
turns = int(input("Number of allowed turns: "))
p1 = input("Name of player 1: ")
p2 = input("Name of player 2: ")

# initialize boards
for x in range(size):
    board1.append(["O"] * size)
    board2.append(["O"] * size)


def print_board(board):
    for row in board:
        print(" ".join(row))

def random_par(board):
    return randint(0, len(board) - 1)

# create boats
p1_ship_row = random_par(board1)
p1_ship_col = random_par(board1)
ship1 = [p1_ship_row,p1_ship_col]
p2_ship_row = random_par(board2)
p2_ship_col = random_par(board2)
ship2 = [p2_ship_row,p2_ship_col]

# locations of ships for debugging
print ("%s\'s ship is at (%s,%s)"%(p1,p1_ship_row,p1_ship_col))
print ("%s\'s is at (%s,%s)"%(p2,p2_ship_row,p2_ship_col))

# return whether or not the ship was sunk
def play_turn(targetBoard, targetShip, targetPlayer, playing):
    print("%s\'s guess: " % (playing))
    guess_row = int(input("   Row:"))
    guess_col = int(input("   Col:"))
    while (guess_row < 0 or guess_row > size-1) or (guess_col < 0 or guess_col > size-1):
        print("Oops, that's not even in the ocean, guess again (remember size is %s)" %(size))
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
    if (play_turn(board2,ship2,p2,p1)): break
    if (play_turn(board1,ship1,p1,p2)): break
    if (turn+1==turns):
        print ("Game Over, neither player could sink the other's ship")