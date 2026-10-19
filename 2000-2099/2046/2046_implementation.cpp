#include <algorithm>
#include <array>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

constexpr int WIDTH = 10;
constexpr int ROWS = 4;
constexpr int COLUMNS = 3;
const std::array<std::string, COLUMNS> DAYS = {"Tuesday", "Thursday", "Saturday"};
using Cell = std::vector<std::string>;

Cell wrap(const std::string &name) {
    Cell lines(1);
    std::istringstream words(name);
    std::string word;
    while (words >> word) {
        if (lines.back().empty())
            lines.back() = word;
        else if (lines.back().size() + 1 + word.size() <= WIDTH)
            lines.back() += " " + word;
        else
            lines.push_back(word);
    }
    return lines;
}

int main() {
    int n;
    std::cin >> n;
    std::string name, day, discarded;
    std::getline(std::cin, discarded);
    std::array<std::array<Cell, DAYS.size()>, ROWS> grid{};
    for (int course = 0; course < n; ++course) {
        std::getline(std::cin, name);
        int lesson;
        std::cin >> day >> lesson;
        std::getline(std::cin, discarded);
        auto column = std::find(DAYS.begin(), DAYS.end(), day) - DAYS.begin();
        grid[lesson - 1][column] = wrap(name);
    }
    std::string border = "+";
    for (std::size_t column = 0; column < DAYS.size(); ++column)
        border += std::string(WIDTH, '-') + "+";
    std::cout << border << '\n';
    for (const auto &row : grid) {
        std::size_t height = 1;
        for (const auto &cell : row)
            height = std::max(height, cell.size());
        for (std::size_t level = 0; level < height; ++level) {
            std::cout << '|';
            for (const auto &cell : row) {
                std::string line = level < cell.size() ? cell[level] : "";
                std::cout << line << std::string(WIDTH - line.size(), ' ') << '|';
            }
            std::cout << '\n';
        }
        std::cout << border << '\n';
    }
}
