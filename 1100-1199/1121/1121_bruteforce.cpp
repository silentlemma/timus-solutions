#include <cstdio>
#include <cstdlib>
#include <string>
#include <utility>
#include <vector>

const int REACH = 5;

int main() {
    int h, w;
    if (scanf("%d %d", &h, &w) != 2)
        return 0;
    std::vector<std::vector<int>> grid(h, std::vector<int>(w));
    for (auto &row : grid)
        for (auto &v : row)
            scanf("%d", &v);
    // the cells at each distance 1..5, as offsets around a crossing
    std::vector<std::vector<std::pair<int, int>>> rings(REACH + 1);
    for (int dr = -REACH; dr <= REACH; dr++)
        for (int dc = -REACH; dc <= REACH; dc++) {
            int d = std::abs(dr) + std::abs(dc);
            if (d >= 1 && d <= REACH)
                rings[d].push_back({dr, dc});
        }
    std::string out;
    for (int r = 0; r < h; r++) {
        for (int c = 0; c < w; c++) {
            int found = -1;
            if (grid[r][c] == 0) {
                found = 0;
                for (int d = 1; d <= REACH && !found; d++)
                    for (auto [dr, dc] : rings[d]) {
                        int rr = r + dr, cc = c + dc;
                        // each type counts once however many branches share it
                        if (rr >= 0 && rr < h && cc >= 0 && cc < w)
                            found |= grid[rr][cc];
                    }
            }
            out += std::to_string(found) + (c + 1 < w ? " " : "\n");
        }
    }
    fputs(out.c_str(), stdout);
}
