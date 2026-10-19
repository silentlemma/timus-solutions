#include <array>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

std::pair<int, int> territorySizes(const std::vector<std::string> &board,
                                   const std::vector<int> &moves) {
    int rows = static_cast<int>(board.size());
    int columns = static_cast<int>(board[0].size());
    int cells = rows * columns;
    std::string colors;
    for (const auto &row : board) {
        colors += row;
    }
    std::vector<std::vector<int>> neighbors(cells);
    for (int row = 0; row < rows; ++row) {
        for (int column = 0; column < columns; ++column) {
            int cell = row * columns + column;
            if (row > 0)
                neighbors[cell].push_back(cell - columns);
            if (row + 1 < rows)
                neighbors[cell].push_back(cell + columns);
            if (column > 0)
                neighbors[cell].push_back(cell - 1);
            if (column + 1 < columns)
                neighbors[cell].push_back(cell + 1);
        }
    }
    std::vector<int> owners(cells, -1);
    std::array<std::vector<int>, 2> territories;
    auto expand = [&](int player, char color) {
        for (std::size_t cursor = 0; cursor < territories[player].size(); ++cursor) {
            int cell = territories[player][cursor];
            for (int adjacent : neighbors[cell]) {
                if (owners[adjacent] == -1 && colors[adjacent] == color) {
                    owners[adjacent] = player;
                    territories[player].push_back(adjacent);
                }
            }
        }
    };
    std::array<int, 2> seeds = {cells - columns, columns - 1};
    for (int player = 0; player < 2; ++player) {
        owners[seeds[player]] = player;
        territories[player].push_back(seeds[player]);
        expand(player, colors[seeds[player]]);
    }
    for (std::size_t turn = 0; turn < moves.size(); ++turn) {
        expand(turn % 2, static_cast<char>('0' + moves[turn]));
    }
    return {static_cast<int>(territories[0].size()), static_cast<int>(territories[1].size())};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int rows, columns;
    std::cin >> rows >> columns;
    std::vector<std::string> board(rows);
    for (auto &row : board)
        std::cin >> row;
    int count;
    std::cin >> count;
    std::vector<int> moves(count);
    for (int &color : moves)
        std::cin >> color;
    auto result = territorySizes(board, moves);
    std::cout << result.first << '\n' << result.second << '\n';
    return 0;
}
