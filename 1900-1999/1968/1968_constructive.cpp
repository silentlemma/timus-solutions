#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

constexpr int kBlockSide = 2;
using Layers = std::vector<std::vector<std::string>>;

Layers reconstruct(const std::vector<std::vector<int>> &photo) {
    int rows = static_cast<int>(photo.size()), columns = static_cast<int>(photo[0].size());
    std::vector<std::vector<int>> counts(rows, std::vector<int>(columns));
    for (int row = 0; row < rows; ++row) {
        for (int column = 0; column < columns; ++column) {
            int value = photo[row][column];
            if (row)
                value -= counts[row - 1][column];
            if (column)
                value -= counts[row][column - 1];
            if (row && column)
                value -= counts[row - 1][column - 1];
            counts[row][column] = value;
        }
    }
    Layers layers;
    for (int level = 0; level < std::min(rows, columns) / kBlockSide; ++level) {
        std::vector<std::string> layer;
        for (int row = 0; row < rows / kBlockSide - level; ++row) {
            std::string line;
            for (int column = 0; column < columns / kBlockSide - level; ++column) {
                int x = level + kBlockSide * row, y = level + kBlockSide * column;
                line.push_back(counts[x][y] > level / kBlockSide ? 'R' : 'W');
            }
            layer.push_back(line);
        }
        layers.push_back(layer);
    }
    return layers;
}

int main() {
    int rows, columns;
    std::cin >> rows >> columns;
    std::vector<std::vector<int>> photo(rows, std::vector<int>(columns));
    for (auto &line : photo) {
        for (int &value : line)
            std::cin >> value;
    }
    auto layers = reconstruct(photo);
    bool first = true;
    for (const auto &layer : layers) {
        if (!first)
            std::cout << '\n';
        first = false;
        for (const auto &line : layer)
            std::cout << line << '\n';
    }
}
