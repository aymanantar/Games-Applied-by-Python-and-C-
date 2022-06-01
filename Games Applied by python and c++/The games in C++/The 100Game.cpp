#include <iostream>
using namespace std;

extern int sum = 0;
extern int move;

//Function Decleration
void sum_review();
void updated_addtion_number();
void get_input(string player);
bool winner(string player);
//Main game
int main()
{
    sum_review();
    while (true){
        updated_addtion_number();
        get_input("First");
        if (winner("First")){
            cout << "First player Win ! " << endl;
            break;
        };
        updated_addtion_number();
        get_input("Second");
        if (winner("Second")){
            cout << "Second player Win !" << endl;
            break;
        };
    };
    
    return 0;
}

// Display game status 
void sum_review(){
    cout << "Sum = " << sum << endl;
    cout << "-----------------"<<endl;
};

// Remove any invalid numbers from list if sum is above 90
void updated_addtion_number(){
    if(sum > 90){
        cout << "{";
        for(int i=1; i<= 9-(sum-90); i++){
            cout << i <<", ";
        }
        cout << (100-sum)<<"}" << endl;
    }
    else{
        cout << "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"<<endl;
    };

};

// Get input from both player
void get_input(string player)
{
    int move;
    while(true){
        cout << player << " player turn: ";
        cin >> move;

        if (move > 0 && move <= 10 && (sum + move) <= 100){
            sum += move;
            sum_review();
            break;
        }
        else{
            cout << "Invalid number... TRY AGAIN. " << endl;
            cout << "-----------------" << endl;
        };
    };
};

// Check who is the winner 
bool winner(string player)
{
    if(sum == 100)
        return true;
    else    
        return false;
};