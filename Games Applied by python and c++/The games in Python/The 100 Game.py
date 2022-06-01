added_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

#Display game status
def sum_review():
    if sum <= 100:
        print(f"Sum = {sum}")
        print("---------------------")

#Get input from both player
def get_input(player):
    global sum
    while True: 
        message_each_turn = player + " player turn: "
        move = input(message_each_turn)
        update_added_numbers()
        if move.isdigit():
            move = int(move)
            if move in added_numbers:
                sum += move
                sum_review()
                break
            else:
                print("Invalid number...TRY AGAIN. ")
                print("--------------")
        else:
            print("Invalid input...TRY AGAIN. ")
            print("--------------")

#Remove any invalid numbers from list when sum is above 90
def update_added_numbers():
    i = 0 
    while (True):
        if i < 11: 
            if (added_numbers[len(added_numbers)- 1] + sum) > 100:
                added_numbers.pop()
        else:
            break
        i += 1

#Check if any players win
def winner(player):
    if sum == 100:
        return True

#main game
def main_game():
    sum_review()
    while (True):
        update_added_numbers()
        print(added_numbers)
        get_input("First")
        if (winner("First")):
            print("First Player Win.")
            break

        update_added_numbers()
        print(added_numbers)        
        get_input("Second")
        if (winner("Second")):
            print("Second player Win.")
            break
    
main_game()

