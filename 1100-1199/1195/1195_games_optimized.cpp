#include <cstdio>

const int SIDE = 3, CELLS = SIDE * SIDE, LINE_COUNT = 2 * SIDE + 2;
const int LINES[LINE_COUNT][SIDE] = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6},
                                     {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}};
const int WIN = 1, DRAW = 0, LOSS = -1;
char board[CELLS];

bool won(char mark) {
    for (const auto &line : LINES)
        if (board[line[0]] == mark && board[line[1]] == mark && board[line[2]] == mark)
            return true;
    return false;
}

int play(char mark, char other) {
    int best = LOSS;
    bool moved = false;
    for (int cell = 0; cell < CELLS; cell++)
        if (board[cell] == '#') {
            moved = true;
            board[cell] = mark;
            int result = won(mark) ? WIN : -play(other, mark);
            board[cell] = '#';
            if (result == WIN)
                return WIN;
            if (result > best)
                best = result;
        }
    return moved ? best : DRAW;
}

int main() {
    for (char &cell : board)
        if (scanf(" %c", &cell) != 1)
            return 0;
    int result = play('X', 'O');
    puts(result == WIN ? "Crosses win" : result == DRAW ? "Draw" : "Ouths win");
}
