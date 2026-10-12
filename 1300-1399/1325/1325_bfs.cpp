#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

const char WALL = '0';

int main() {
    std::ios::sync_with_stdio(false);
    int n = 0, m = 0, sr = 0, sc = 0, tr = 0, tc = 0;
    std::cin >> n >> m >> sr >> sc >> tr >> tc;
    int width = m + 2;
    // the plan with a frame of walls, as one flat array
    std::string grid(width, WALL);
    for (int r = 0; r < n; r++) {
        std::string row;
        std::cin >> row;
        row.resize(m, WALL);
        grid += WALL + row + WALL;
    }
    grid += std::string(width, WALL);
    std::vector<int> steps(grid.size(), -1);
    std::vector<int> seeded(grid.size(), -1); // the layer that last took the cell as a seed
    std::vector<int> moves;
    for (int dr = -1; dr <= 1; dr++) {
        for (int dc = -1; dc <= 1; dc++) {
            if (dr != 0 || dc != 0)
                moves.push_back(dr * width + dc);
        }
    }
    int start = sr * width + sc, target = tr * width + tc;
    // layer c holds the cells first reached after c changes of shoes, all of
    // the same kind; seeds come in sorted by the number of steps
    char kind = grid[start];
    int changes = 0;
    std::vector<std::pair<int, int>> seeds = {{0, start}}, later;
    std::vector<int> current, following;
    while (!seeds.empty() && steps[target] < 0) {
        later.clear();
        current.clear();
        size_t i = 0;
        int level = seeds[0].first;
        while ((i < seeds.size() || !current.empty()) && steps[target] < 0) {
            if (current.empty() && seeds[i].first > level)
                level = seeds[i].first;
            for (; i < seeds.size() && seeds[i].first == level; i++) {
                int cell = seeds[i].second;
                if (steps[cell] < 0) {
                    steps[cell] = level;
                    current.push_back(cell);
                }
            }
            following.clear();
            for (int cell : current) {
                for (int move : moves) {
                    int near = cell + move;
                    if (steps[near] >= 0 || grid[near] == WALL)
                        continue;
                    if (grid[near] == kind) {
                        steps[near] = level + 1;
                        following.push_back(near);
                    } else if (seeded[near] != changes) {
                        seeded[near] = changes;
                        later.push_back({level + 1, near});
                    }
                }
            }
            current.swap(following);
            level++;
        }
        if (steps[target] < 0) {
            if (!later.empty())
                kind = grid[later[0].second];
            changes++;
            seeds.swap(later);
        }
    }
    if (steps[target] < 0)
        printf("0 0\n");
    else
        printf("%d %d\n", steps[target] + 1, changes);
    return 0;
}
