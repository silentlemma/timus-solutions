#include <iostream>
#include <vector>

std::vector<std::vector<int>> buildSchedule(int cannons) {
    const int size = 2 * cannons + 1;
    std::vector<std::vector<int>> schedule(size, std::vector<int>(size));
    for (int row = 0; row < size; ++row) {
        for (int column = 0; column < size; ++column) {
            if (row != column) {
                schedule[row][column] = (row + column + size - 1) % size + 1;
            }
        }
    }
    return schedule;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int cannons;
    std::cin >> cannons;
    for (const auto &row : buildSchedule(cannons)) {
        for (int column = 0; column < static_cast<int>(row.size()); ++column) {
            if (column > 0) {
                std::cout << ' ';
            }
            std::cout << row[column];
        }
        std::cout << '\n';
    }
    return 0;
}
