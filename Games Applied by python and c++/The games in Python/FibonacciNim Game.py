
starting_coins = int(input("Please enter the number of coins you want to start the pile with: "))
remaining_coins = starting_coins
game_on = True


# Displays game status
def game_status(n):
    global remaining_coins
    remaining_coins -= n
    print(f"The pile now has {remaining_coins} coins.")


# Checks if any player wins
def is_winner():
    global remaining_coins, game_on
    if remaining_coins == 0:
        game_on = False
        print("Congratulations! You win.")


# Main game
def main():
    print(f"The pile now has {starting_coins} coin(s).")
    while True:
        player1 = input(f"Player 1 may remove any number from 1 to {starting_coins - 1}.")
        try:
            player1 = int(player1)
            break
        except ValueError:
            print("input a NUMBER please")
    while player1 not in range(1, starting_coins):
        player1 = int(input("Please enter a valid number: "))
    game_status(player1)
    while game_on:
        while True:
            player2 = input(f"Player2, you're allowed to pick a number from 1 to {2 * player1} to remove.")
            try:
                player2 = int(player2)
                break
            except ValueError:
                print("input a NUMBER please")
        while player2 not in range(1, min(remaining_coins + 1, player1 * 2 + 1)):
            player2 = int(input("Please enter a number that can be removed from the remaining coins in the pile: "))
        game_status(player2)
        is_winner()
        if not game_on:
            break
        while True:
            player1 = input(f"Player1, you're allowed to pick a number from 1 to {2 * player2} to remove.")
            try:
                player1 = int(player1)
                break
            except ValueError:
                print("input a NUMBER please")
        while player1 not in range(1, min(remaining_coins + 1, player2 * 2 + 1)):
            player1 = int(input("Please enter a number that can be removed from the remaining coins in the pile: "))
        game_status(player1)
        is_winner()
        if not game_on:
            break


main()

