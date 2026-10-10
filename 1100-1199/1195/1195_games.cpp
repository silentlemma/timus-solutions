#include <algorithm>
#include <iostream>
#include <string>

const int LINES[8][3] = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6},
                         {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}};
// outcomes for the side to move: win, draw, loss
const int WIN = 1, DRAW = 0, LOSS = -1;

std::string board;

bool won(char mark) {
    for (auto &line : LINES) {
        if (board[line[0]] == mark && board[line[1]] == mark && board[line[2]] == mark) {
            return true;
        }
    }
    return false;
}

// the best outcome for the side about to move with mark
int play(char mark, char other) {
    int best = LOSS;
    bool moved = false;
    for (size_t i = 0; i < board.size(); i++) {
        if (board[i] == '#') {
            moved = true;
            board[i] = mark;
            best = std::max(best, won(mark) ? WIN : -play(other, mark));
            board[i] = '#';
        }
    }
    return moved ? best : DRAW;
}

int main() {
    for (std::string row; std::cin >> row;) {
        board += row;
    }
    // three moves each have been made, so crosses move now
    int result = play('X', 'O');
    std::cout << (result == WIN ? "Crosses win" : result == DRAW ? "Draw" : "Ouths win") << "\n";
}
