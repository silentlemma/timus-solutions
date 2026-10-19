#include <iostream>
#include <string>

using namespace std;

constexpr int PREMIUM_LAST = 2;
constexpr int BUSINESS_LAST = 20;

int main() {
    string seat;
    cin >> seat;
    int row = stoi(seat.substr(0, seat.size() - 1));
    char letter = seat.back();
    char right_window;
    string aisles;
    if (row <= PREMIUM_LAST) {
        right_window = 'D';
        aisles = "BC";
    } else if (row <= BUSINESS_LAST) {
        right_window = 'F';
        aisles = "BCDE";
    } else {
        right_window = 'K';
        aisles = "CDGH";
    }
    if (letter == 'A' || letter == right_window)
        cout << "window\n";
    else if (aisles.find(letter) != string::npos)
        cout << "aisle\n";
    else
        cout << "neither\n";
}
