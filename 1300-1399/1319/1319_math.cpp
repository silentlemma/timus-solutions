#include <cstdio>

// no table: each number is computed from the length of its diagonal,
// counted from the start above the main diagonal and from the end below it
int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < n; ++col) {
            // the diagonal of this cell has n - |col - row| cells
            int length = n - (col >= row ? col - row : row - col);
            // the cells of the earlier diagonals, then the place in this one
            int value = col >= row ? length * (length - 1) / 2 + row + 1
                                   : n * n - length * (length + 1) / 2 + col + 1;
            printf(col + 1 < n ? "%d " : "%d\n", value);
        }
    }
}
