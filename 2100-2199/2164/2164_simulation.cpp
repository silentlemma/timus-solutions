#include <array>
#include <cstdint>
#include <iostream>
#include <string>

constexpr int ROWS = 7;
constexpr int COLUMNS = 9;
constexpr int CONNECT = 4;
constexpr int MAX_MOVES = ROWS * COLUMNS;
constexpr int FIRST_WIN = 2 * (CONNECT - 1);
constexpr std::array<int, CONNECT> ROW_STEP = {1, 0, 1, -1};
constexpr std::array<int, CONNECT> COLUMN_STEP = {0, 1, 1, 1};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string moves;
    std::cin >> moves;
    std::array<int, CONNECT> shifts{};
    std::array<std::uint64_t, CONNECT> masks{};
    for (int direction = 0; direction < CONNECT; ++direction) {
        shifts[direction] = COLUMN_STEP[direction] * ROWS + ROW_STEP[direction];
        for (int column = 0; column < COLUMNS; ++column) {
            for (int row = 0; row < ROWS; ++row) {
                const int end_row = row + (CONNECT - 1) * ROW_STEP[direction];
                const int end_column = column + (CONNECT - 1) * COLUMN_STEP[direction];
                if (0 <= end_row && end_row < ROWS && end_column < COLUMNS) {
                    masks[direction] |= std::uint64_t{1} << (column * ROWS + row);
                }
            }
        }
    }

    int wins = 0;
    int draws = 0;
    const int size = static_cast<int>(moves.size());
    for (int start = 0; start < size; ++start) {
        std::array<int, COLUMNS> heights{};
        std::array<std::uint64_t, 2> boards{};
        int placed = 0;
        for (int turn = 0; turn < MAX_MOVES && start + turn < size; ++turn) {
            const int column = moves[start + turn] - '1';
            if (heights[column] == ROWS) {
                continue;
            }
            const int player = turn % 2;
            boards[player] |= std::uint64_t{1} << (column * ROWS + heights[column]);
            ++heights[column];
            ++placed;
            bool won = false;
            if (turn >= FIRST_WIN) {
                for (int direction = 0; direction < CONNECT; ++direction) {
                    const int shift = shifts[direction];
                    const std::uint64_t pairs = boards[player] & (boards[player] >> shift);
                    // Masks prevent a shifted run from crossing a column boundary.
                    if ((pairs & (pairs >> (2 * shift)) & masks[direction]) != 0) {
                        won = true;
                        break;
                    }
                }
            }
            if (won) {
                ++wins;
                break;
            }
            if (placed == MAX_MOVES) {
                ++draws;
            }
        }
    }
    std::cout << wins << ' ' << draws << '\n';
}
