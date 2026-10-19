#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

std::string draw(const std::vector<std::pair<int, int>> &points) {
    int left = 0, right = 0, lower = 0, upper = 0;
    for (const auto &point : points) {
        left = std::min(left, point.first);
        right = std::max(right, point.first);
        lower = std::min(lower, point.second);
        upper = std::max(upper, point.second);
    }
    const int width = right - left + 1;
    std::vector<std::string> grid(upper - lower + 1, std::string(width, '.'));
    for (auto &row : grid)
        row[-left] = '|';
    grid[upper] = std::string(width, '-');
    grid[upper][-left] = '+';
    for (const auto &point : points)
        grid[upper - point.second][point.first - left] = '*';
    std::string output;
    for (const auto &row : grid)
        output += row + '\n';
    return output;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    std::cin >> size;
    std::vector<std::pair<int, int>> points(size);
    for (auto &point : points)
        std::cin >> point.first >> point.second;
    std::cout << draw(points);
    return 0;
}
