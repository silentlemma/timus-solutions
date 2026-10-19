#include <array>
#include <iostream>
#include <string>
#include <vector>

std::string solve(const std::vector<std::string> &grid, const std::vector<int> &inputs) {
    constexpr int ALPHABET = 26;
    constexpr int VALUE_LIMIT = 100000;
    constexpr int TICKS = 1000000;
    constexpr int DIRECTIONS = 4;
    constexpr int UP = 3;
    const std::array<int, DIRECTIONS> dr{0, 1, 0, -1};
    const std::array<int, DIRECTIONS> dc{1, 0, -1, 0};
    std::array<int, ALPHABET> memory{};
    int row = 0, column = 0, direction = 0, current = 0;
    std::size_t cursor = 0;
    int height = static_cast<int>(grid.size());
    int width = static_cast<int>(grid[0].size());
    std::string output;
    for (int tick = 0; tick < TICKS; ++tick) {
        char op = grid[row][column];
        switch (op) {
        case '#':
            return output;
        case '>':
            direction = 0;
            break;
        case 'v':
            direction = 1;
            break;
        case '<':
            direction = 2;
            break;
        case '^':
            direction = UP;
            break;
        case '?':
            current = inputs[cursor];
            if (cursor + 1 < inputs.size())
                ++cursor;
            break;
        case '!':
            output += std::to_string(current) + '\n';
            current = 0;
            break;
        case '+':
            ++current;
            break;
        case '-':
            --current;
            break;
        case '@':
            direction = (direction + (current == 0 ? DIRECTIONS - 1 : 1)) % DIRECTIONS;
            break;
        default:
            if (op >= 'A' && op <= 'Z')
                std::swap(current, memory[op - 'A']);
        }
        if (current < -VALUE_LIMIT || current > VALUE_LIMIT)
            return output + "OVERFLOW ERROR\n";
        row += dr[direction];
        column += dc[direction];
        if (row < 0 || row >= height || column < 0 || column >= width)
            return output + "RUNTIME ERROR\n";
    }
    return output + "TIME LIMIT EXCEEDED\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int height, width;
    if (!(std::cin >> height >> width))
        return 0;
    std::vector<std::string> grid(height);
    for (auto &row : grid)
        std::cin >> row;
    int count;
    std::cin >> count;
    std::vector<int> inputs(count);
    for (int &value : inputs)
        std::cin >> value;
    std::cout << solve(grid, inputs);
    return 0;
}
