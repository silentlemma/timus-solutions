#include <cstdio>
#include <cstdlib>
#include <vector>

int n;
std::vector<std::vector<int>> grid, black; // black[i][j]: black cells among the first j of row i

// Black cells of row i in columns lo..hi.
static int ones(int i, int lo, int hi) { return black[i][hi + 1] - black[i][lo]; }

static bool fits(int ci, int cj, int r) {
    // row ci + d: |d| black cells, a white run of 2(r - |d|) + 1, |d| black
    for (int d = -r; d <= r; d++) {
        int i = ci + d, side = std::abs(d), inner = r - side;
        if (ones(i, cj - r, cj - inner - 1) != side || ones(i, cj + inner + 1, cj + r) != side) {
            return false;
        }
        if (ones(i, cj - inner, cj + inner) != 0) {
            return false;
        }
    }
    return true;
}

static int largest() {
    // the white square needs a cell on every side of the centre, so r >= 1
    for (int r = (n - 1) / 2; r >= 1; r--) {
        for (int ci = r; ci < n - r; ci++) {
            for (int cj = r; cj < n - r; cj++) {
                // quick tests first: a white centre and tip, a black corner
                if (grid[ci][cj] || grid[ci - r][cj] || !grid[ci - r][cj - r]) {
                    continue;
                }
                if (fits(ci, cj, r)) {
                    return 2 * r + 1;
                }
            }
        }
    }
    return 0;
}

// The next 0 or 1 of the painting; the cells may come with or without spaces.
static int readCell() {
    int c = getchar();
    while (c != '0' && c != '1') {
        c = getchar();
    }
    return c - '0';
}

int main() {
    while (scanf("%d", &n) == 1 && n != 0) {
        grid.assign(n, std::vector<int>(n));
        black.assign(n, std::vector<int>(n + 1, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = readCell();
                black[i][j + 1] = black[i][j] + grid[i][j];
            }
        }
        int best = largest();
        if (best) {
            printf("%d\n", best);
        } else {
            puts("No solution");
        }
    }
}
