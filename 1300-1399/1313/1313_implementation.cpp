#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> grid(n, std::vector<int>(n));
    for (auto &row : grid)
        for (int &v : row)
            if (scanf("%d", &v) != 1)
                return 0;
    // diagonal s holds the cells with row + column = s; each is read from
    // its lowest row up
    bool first = true;
    for (int s = 0; s <= 2 * n - 2; s++) {
        for (int i = std::min(s, n - 1); i >= std::max(0, s - n + 1); i--) {
            printf(first ? "%d" : " %d", grid[i][s - i]);
            first = false;
        }
    }
    printf("\n");
    return 0;
}
