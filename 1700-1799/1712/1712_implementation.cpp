#include <iostream>
#include <string>

const int SIZE = 4;

int main() {
    std::string grille[SIZE], square[SIZE];
    for (std::string &row : grille) {
        std::cin >> row;
    }
    for (std::string &row : square) {
        std::cin >> row;
    }
    std::string password;
    // read the windows row by row, then turn the grille clockwise:
    // the cell (r, c) of the turned grille is (SIZE - 1 - c, r) of the old one
    for (int turn = 0; turn < SIZE; turn++) {
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                if (grille[r][c] == 'X') {
                    password += square[r][c];
                }
            }
        }
        std::string turned[SIZE];
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                turned[r] += grille[SIZE - 1 - c][r];
            }
        }
        for (int r = 0; r < SIZE; r++) {
            grille[r] = turned[r];
        }
    }
    std::cout << password << "\n";
}
