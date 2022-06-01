import numpy as np

row = 4
column = 4
count = 1 #Used to fill board with numbers

# Used to check for winning.
values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 

#Display main full board
def create_board():
    global board, count
    board = np.zeros([4,4], dtype= "int32")
    for i in range(row):
        for j in range(column):
            board[i][j] = count
            count = count + 1
    print(board)

#Display board after changes    
def updated_board(): 
    print(board)
    print("----------------------")

#Checks if all inputs are numbers no chcracters
def check_input():
    global move
    i = 0
    while i < len(move):
        if move[i].isdigit():
            move[i] = int(move[i])
        else:
            return False
        i += 1
    return True
   

#Get input from both users
def get_input(player):
    global move
    message = f"{player} player choose two boxes to cover: "
    while True:
        move = [i for i in input(message).split(",")]
        if (check_input()):
            if len(move) == 2:
                if move[0] in board and move[1] in board:
                    move.sort()
                    if move[0] + 1 == move[1] or move[0] + 4 == move[1]:
                        values.remove(move[0])
                        values.remove(move[1])
                        for i in range(row):
                            for j in range(column):
                                if move[0] == board[i][j]:
                                    board[i][j] = 0
                                if move[1] == board[i][j]:
                                    board[i][j] = 0
                        break
                    else:
                        print("Boxes must be horizontal or verticle...Try again")
                else:
                    print(f"Boxes used before...Try again")
            else:
                print("You have to choose just TWO boxes like (1,2)")
        else:
            print("Numbers Only is avaliable.")

#Check Who wins
def winner(player):
    global values
    if len(values) == 2:
        if  values[0] + 1 == values[1] or values[0] + 4 == values[1]:
            return False
        else:
            return True
    elif len(values) == 0:
        return True


#Main game
def main_game():
    create_board() 
    while True:
        get_input("First")

        if (winner("First")):
            print("First player Win.")
            break

        updated_board()

        get_input("Second")

        if (winner("Second")):
            print("Second player Win.")
            break

        updated_board()

main_game()

