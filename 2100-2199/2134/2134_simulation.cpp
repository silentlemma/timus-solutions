#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int height, width, limit;
    std::cin >> height >> width >> limit;
    int stamp_height, stamp_width;
    std::cin >> stamp_height >> stamp_width;

    std::vector<int> black;
    for (int row = 0; row < stamp_height; ++row) {
        std::string pattern;
        std::cin >> pattern;
        for (int column = 0; column < stamp_width; ++column) {
            if (pattern[column] == '#') {
                black.push_back(row * width + column);
            }
        }
    }

    std::vector<unsigned char> board(height * width, 0);
    std::vector<unsigned char> uses(height * width, 0);
    int repainted = 0;
    int operation_count;
    std::cin >> operation_count;
    for (int operation = 1; operation <= operation_count; ++operation) {
        int row, column;
        std::cin >> row >> column;
        int origin = (row - 1) * width + column - 1;
        if (black.empty() || uses[origin] == 2) {
            continue;
        }
        ++uses[origin];
        // A third use of one placement cannot change any cell state.
        for (int offset : black) {
            unsigned char &cell = board[origin + offset];
            if (cell == 0) {
                cell = 1;
            } else if (cell == 1) {
                cell = 2;
                ++repainted;
                if (repainted == limit) {
                    std::cout << "Wasted after stamp #" << operation << '\n';
                    return 0;
                }
            }
        }
    }

    std::string output;
    output.reserve(height * (width + 1));
    for (int row = 0; row < height; ++row) {
        for (int column = 0; column < width; ++column) {
            output += board[row * width + column] == 0 ? '.' : '#';
        }
        output += '\n';
    }
    std::cout << output;
}
