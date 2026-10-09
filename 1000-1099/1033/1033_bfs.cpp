#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

const int SIDE_AREA = 9, DIRECTIONS = 4, ENTRANCE_SIDES = 4;
const int DI[DIRECTIONS] = {-1, 1, 0, 0}, DJ[DIRECTIONS] = {0, 0, -1, 1};

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> grid(n);
    for (auto &row : grid)
        std::cin >> row;
    // visit every empty cell reachable from either entrance; each side of
    // such a cell that faces a block or the outer wall is a visible wall
    std::vector<std::vector<bool>> seen(n, std::vector<bool>(n, false));
    std::vector<std::pair<int, int>> queue = {{0, 0}, {n - 1, n - 1}};
    seen[0][0] = seen[n - 1][n - 1] = true;
    int sides = 0;
    for (size_t head = 0; head < queue.size(); head++) {
        auto [i, j] = queue[head];
        for (int d = 0; d < DIRECTIONS; d++) {
            int a = i + DI[d], b = j + DJ[d];
            if (a < 0 || b < 0 || a >= n || b >= n || grid[a][b] == '#') {
                sides++;
            } else if (!seen[a][b]) {
                seen[a][b] = true;
                queue.push_back({a, b});
            }
        }
    }
    // the outer sides of the two entrance cells are openings, not walls
    printf("%d\n", (sides - ENTRANCE_SIDES) * SIDE_AREA);
}
