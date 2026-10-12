#include <cctype>
#include <cstdio>
#include <cstdlib>

const int SIZE = 8;
const int MOVES = 32;
const int DC[] = {1, 1, -1, -1};
const int DR[] = {1, -1, 1, -1};
const int DIRECTIONS = sizeof DC / sizeof DC[0];
const int LONGEST = 16; // room for a move like h8

int board[SIZE][SIZE]; // 0 empty, 1 white, 2 black

bool inside(int c, int r) { return c >= 0 && c < SIZE && r >= 0 && r < SIZE; }

// some checker has a checker of the other color next to it on a diagonal
// and a free square right behind that one
bool canCapture() {
    for (int c = 0; c < SIZE; c++) {
        for (int r = 0; r < SIZE; r++) {
            if (board[c][r] == 0)
                continue;
            for (int d = 0; d < DIRECTIONS; d++) {
                int oc = c + DC[d], orow = r + DR[d], lc = c + 2 * DC[d], lr = r + 2 * DR[d];
                if (inside(lc, lr) && board[oc][orow] != 0 && board[oc][orow] != board[c][r] &&
                    board[lc][lr] == 0)
                    return true;
            }
        }
    }
    return false;
}

int main() {
    char move[LONGEST];
    for (int number = 1; number <= MOVES && scanf("%15s", move) == 1; number++) {
        int c = std::tolower(move[0]) - 'a', r = std::atoi(move + 1) - 1;
        board[c][r] = number % 2 == 1 ? 1 : 2; // white moves on the odd lines
        if (canCapture()) {
            printf("%d\n", number);
            return 0;
        }
    }
    printf("Draw\n");
    return 0;
}
