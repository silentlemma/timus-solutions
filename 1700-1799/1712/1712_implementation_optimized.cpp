#include <cstdio>

const int SIZE = 4;

// the squares are read and the password written character by character with
// getchar and putchar
int nextCharacter() {
    int ch;
    do {
        ch = std::getchar();
    } while (ch != EOF && ch <= ' ');
    return ch;
}

int main() {
    char grille[SIZE][SIZE], square[SIZE][SIZE];
    for (auto &row : grille) {
        for (char &cell : row)
            cell = static_cast<char>(nextCharacter());
    }
    for (auto &row : square) {
        for (char &cell : row)
            cell = static_cast<char>(nextCharacter());
    }
    // read the windows row by row, then turn the grille clockwise:
    // the cell (r, c) of the turned grille is (SIZE - 1 - c, r) of the old one
    for (int turn = 0; turn < SIZE; turn++) {
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                if (grille[r][c] == 'X')
                    std::putchar(square[r][c]);
            }
        }
        char turned[SIZE][SIZE];
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++)
                turned[r][c] = grille[SIZE - 1 - c][r];
        }
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++)
                grille[r][c] = turned[r][c];
        }
    }
    std::putchar('\n');
}
