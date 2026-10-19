#include <array>
#include <iostream>

int main() {
    constexpr int HEIGHT = 6;
    constexpr int WIDTH = 11;
    const std::array<const char *, HEIGHT> grid{">?v........", ".>>.......v", "..@A+AB+B-<",
                                                "..B........", "..-........", ".^@A!#....."};
    std::cout << HEIGHT << ' ' << WIDTH << '\n';
    for (const char *row : grid)
        std::cout << row << '\n';
    return 0;
}
