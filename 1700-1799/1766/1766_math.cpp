#include <algorithm>
#include <cstdio>

const int SIDE = 8;

int main() {
    long long grid[SIDE][SIDE], score[SIDE][SIDE], total = 0;
    for (int r = 0; r < SIDE; r++)
        for (int c = 0; c < SIDE; c++)
            if (scanf("%lld", &grid[r][c]) != 1) return 0;
    // moving from u to a neighbour v with weight w(v) / W(u), where W(u) sums
    // the weights around u, the walk is balanced by w(u) W(u) in every cell,
    // and after so many steps it has settled into that distribution
    for (int r = 0; r < SIDE; r++) {
        for (int c = 0; c < SIDE; c++) {
            long long around = 0;
            for (int y = std::max(0, r - 1); y <= std::min(SIDE - 1, r + 1); y++)
                for (int x = std::max(0, c - 1); x <= std::min(SIDE - 1, c + 1); x++)
                    if (y != r || x != c) around += grid[y][x];
            score[r][c] = grid[r][c] * around;
            total += score[r][c];
        }
    }
    for (int r = 0; r < SIDE; r++) {
        for (int c = 0; c < SIDE; c++) printf(c ? " %.15f" : "%.15f", (double)score[r][c] / total);
        printf("\n");
    }
    return 0;
}
