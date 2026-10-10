#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> grid(n, std::vector<int>(n));
    for (auto &row : grid)
        for (auto &v : row)
            if (scanf("%d", &v) != 1)
                return 0;
    int best = grid[0][0];
    for (int top = 0; top < n; top++) {
        // column sums of the rows from top to bottom, then the best run of
        // neighbouring columns by Kadane's scan
        std::vector<int> cols(n, 0);
        for (int bottom = top; bottom < n; bottom++) {
            int run = 0;
            for (int c = 0; c < n; c++) {
                cols[c] += grid[bottom][c];
                run = run < 0 ? cols[c] : run + cols[c];
                best = std::max(best, run);
            }
        }
    }
    printf("%d\n", best);
}
