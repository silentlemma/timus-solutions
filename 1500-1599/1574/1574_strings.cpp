#include <iostream>
#include <string>
using namespace std;

int main() {
    string line;
    cin >> line;
    // the balance after each prefix; a shift that starts right after a prefix
    // of the lowest balance never goes below zero, any other shift does
    int balance = 0, lowest = 0, count = 0;
    for (size_t i = 0; i < line.size(); i++) {
        balance += line[i] == '(' ? 1 : -1;
        if (i == 0 || balance < lowest)
            lowest = balance, count = 1;
        else if (balance == lowest)
            count++;
    }
    cout << (balance == 0 ? count : 0) << endl;
}
