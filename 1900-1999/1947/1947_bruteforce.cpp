#include <array>
#include <iostream>
#include <string>
#include <utility>

constexpr int SIDE = 5;
constexpr int PORT_COUNT = 4;
constexpr int CELLS = SIDE * SIDE;
constexpr int MIN_TILES = 3;
enum Port { TOP, RIGHT, BOTTOM, LEFT };
constexpr int ROW_STEP[] = {-1, 0, 1, 0};
constexpr int COLUMN_STEP[] = {0, 1, 0, -1};
constexpr int OPPOSITE[] = {BOTTOM, LEFT, TOP, RIGHT};
constexpr int CONNECTIONS[][PORT_COUNT] = {{LEFT, BOTTOM, RIGHT, TOP}, {RIGHT, TOP, LEFT, BOTTOM}};
constexpr char DIRECTIONS[] = {'L', 'R', 'U', 'D'};
constexpr int HOLE_ROW[] = {0, 0, 1, -1};
constexpr int HOLE_COLUMN[] = {1, -1, 0, 0};

bool winning(const std::string &board) {
    for (int side = 0; side < PORT_COUNT; ++side) {
        for (int offset = 0; offset < SIDE; ++offset) {
            int row = side == TOP ? 0 : (side == BOTTOM ? SIDE - 1 : offset);
            int column = side == LEFT ? 0 : (side == RIGHT ? SIDE - 1 : offset);
            int incoming = side, count = 0;
            std::array<bool, CELLS * PORT_COUNT> visited{};
            std::array<bool, CELLS> tiles{};
            while (true) {
                const int index = row * SIDE + column, state = index * PORT_COUNT + incoming;
                if (board[index] == '*' || visited[state])
                    break;
                visited[state] = true;
                if (!tiles[index]) {
                    tiles[index] = true;
                    ++count;
                }
                const int outgoing = CONNECTIONS[board[index] == '/' ? 0 : 1][incoming];
                row += ROW_STEP[outgoing];
                column += COLUMN_STEP[outgoing];
                if (row < 0 || row >= SIDE || column < 0 || column >= SIDE) {
                    if (outgoing != side && count >= MIN_TILES)
                        return true;
                    break;
                }
                incoming = OPPOSITE[outgoing];
            }
        }
    }
    return false;
}

std::string solve(const std::string &board) {
    if (winning(board))
        return "WIN";
    const int empty = static_cast<int>(board.find('*'));
    const int row = empty / SIDE, column = empty % SIDE;
    for (int motion = 0; motion < PORT_COUNT; ++motion) {
        for (int amount = 1; amount < SIDE; ++amount) {
            const int endRow = row + HOLE_ROW[motion] * amount;
            const int endColumn = column + HOLE_COLUMN[motion] * amount;
            if (endRow < 0 || endRow >= SIDE || endColumn < 0 || endColumn >= SIDE)
                continue;
            std::string changed = board;
            int hole = empty;
            for (int step = 0; step < amount; ++step) {
                const int following = hole + HOLE_ROW[motion] * SIDE + HOLE_COLUMN[motion];
                std::swap(changed[hole], changed[following]);
                hole = following;
            }
            if (winning(changed))
                return std::string(1, DIRECTIONS[motion]) + std::to_string(amount);
        }
    }
    return "FAIL";
}

int main() {
    std::string board, row;
    for (int index = 0; index < SIDE; ++index) {
        std::cin >> row;
        board += row;
    }
    std::cout << solve(board) << '\n';
    return 0;
}
