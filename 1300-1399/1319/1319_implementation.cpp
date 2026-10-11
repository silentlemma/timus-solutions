#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> grid(n, std::vector<int>(n));
    int number = 1;
    // diagonals by column minus row, from the top right corner down
    for (int shift = n - 1; shift > -n; shift--) {
        for (int row = std::max(0, -shift); row < std::min(n, n - shift); row++)
            grid[row][row + shift] = number++;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf(j + 1 < n ? "%d " : "%d\n", grid[i][j]);
    }
    return 0;
}
