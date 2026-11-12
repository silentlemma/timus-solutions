#include <cstdio>
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <string>
#include <utility>
#include <vector>

const char WALL = '0';
using Distance = std::pair<int, int>; // shoe changes, then steps
using Visit = std::pair<Distance, int>;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m, startRow, startCol, targetRow, targetCol;
    if (!(std::cin >> n >> m >> startRow >> startCol >> targetRow >> targetCol))
        return 0;

    const int width = m + 2;
    std::string grid(width, WALL);
    for (int r = 0; r < n; ++r) {
        std::string row;
        std::cin >> row;
        grid += WALL + row + WALL;
    }
    grid += std::string(width, WALL);
    const int start = startRow * width + startCol;
    const int target = targetRow * width + targetCol;
    const int moves[] = {-width - 1, -width, -width + 1, -1, 1, width - 1, width, width + 1};

    const int infinity = std::numeric_limits<int>::max();
    std::vector<Distance> best(grid.size(), {infinity, infinity});
    std::priority_queue<Visit, std::vector<Visit>, std::greater<Visit>> pending;
    best[start] = {0, 0};
    pending.emplace(best[start], start);
    while (!pending.empty()) {
        const auto [distance, cell] = pending.top();
        pending.pop();
        if (distance != best[cell])
            continue;
        if (cell == target) {
            std::printf("%d %d\n", distance.second + 1, distance.first);
            return 0;
        }
        for (int move : moves) {
            const int next = cell + move;
            if (grid[next] == WALL)
                continue;
            const Distance candidate{distance.first + (grid[next] != grid[cell]),
                                     distance.second + 1};
            if (candidate < best[next]) {
                best[next] = candidate;
                pending.emplace(candidate, next);
            }
        }
    }
    std::puts("0 0");
}
