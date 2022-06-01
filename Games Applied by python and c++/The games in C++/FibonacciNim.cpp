#include <iostream>
#include <random>

// Picking a random number for the pile
std::random_device rd;
std::mt19937 generator(rd());
std::uniform_int_distribution<> range(1, 50);
int starting_coins = range(generator), remaining_coins = starting_coins;
bool game_on = true;

// Displays game status (how many coins left in the pile)
void game_status(int n)
{
    remaining_coins -= n;
    std::cout << "The pile now has " << remaining_coins << " coins." << '\n';
}

// Checks if any player is the winner
void is_winner()
{
    if (remaining_coins == 0)
    {
        game_on = false;
        std::cout << "Congratulations! You win.";
    }
}

// Main game
int main() {
    std::cout << "The pile now has " << starting_coins << " coin(s)." << '\n';
    int player1, player2;
    std::cout << "Player 1 may remove any number from 1 to " << starting_coins - 1 << "." << '\n';
    std::cin >> player1;
    while(player1 < 1 || player1 > starting_coins - 1)
    {
        std::cout << "Please enter a valid number: ";
        std::cin >> player1;
    }
    game_status(player1);
    while (game_on)
    {
        std::cout << "Player2, you're allowed to pick a number from 1 to " << 2 * player1 << " to remove. \n";
        std::cin >> player2;
        while((player2 < 1 || player2 > remaining_coins) || player2 > player1 * 2)
        {
            std::cout << "Please enter a number that can be removed from the remaining coins in the pile: ";
            std::cin >> player2;
        }
        game_status(player2);
        is_winner();
        if (not game_on)
            break;
        std::cout << "Player1, you're allowed to pick a number from 1 to " << 2 * player2 << " to remove. \n";
        std::cin >> player1;
        while((player1 < 1 || player1 > remaining_coins) || player1 > player2 * 2)
        {
            std::cout << "Please enter a number that can be removed from the remaining coins in the pile: ";
            std::cin >> player1;
        }
        game_status(player1);
        is_winner();
        if (not game_on)
            break;
    }


    return 0;
}
