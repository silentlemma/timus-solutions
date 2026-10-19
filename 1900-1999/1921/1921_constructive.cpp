#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> constructBoard(int rows, int columns, int palette, int level) {
    int target = level - 1;
    int longest = std::max(rows, columns);
    int rowColors = std::min(rows, 2);
    int columnColors = std::min(columns, 2);
    if (longest < target || (palette == 1 && longest != target) ||
        (palette > 1 && target == 1 && palette < rowColors * columnColors)) {
        return {};
    }
    std::vector<std::string> board(rows, std::string(columns, 'A'));
    for (int row = 0; row < rows; ++row) {
        for (int column = 0; column < columns; ++column) {
            int color = 0;
            if (palette > 1) {
                if (target == 1) {
                    color = (row % 2) * columnColors + column % 2;
                } else if (columns >= target) {
                    color = (row + column / target) % 2;
                } else {
                    color = (column + row / target) % 2;
                }
            }
            board[row][column] = static_cast<char>('A' + color);
        }
    }
    return board;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int rows, columns, palette, level;
    std::cin >> rows >> columns >> palette >> level;
    auto board = constructBoard(rows, columns, palette, level);
    if (board.empty()) {
        std::cout << "NO\n";
    } else {
        std::cout << "YES\n";
        for (const auto &row : board) {
            std::cout << row << '\n';
        }
    }
    return 0;
}
