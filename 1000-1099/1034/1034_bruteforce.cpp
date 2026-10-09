#include <cstdio>
#include <vector>

const int MOVED = 3;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // col[r] is the column of the queen in row r; sum[r + c] and diff[r - c + n]
    // count the queens on each diagonal
    std::vector<int> col(n), sum(2 * n), diff(2 * n);
    for (int i = 0; i < n; i++) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2)
            return 0;
        col[x - 1] = y - 1;
    }
    for (int r = 0; r < n; r++) {
        sum[r + col[r]]++;
        diff[r - col[r] + n]++;
    }
    long long count = 0;
    for (int a = 0; a < n; a++)
        for (int b = a + 1; b < n; b++)
            for (int c = b + 1; c < n; c++) {
                int rows[MOVED] = {a, b, c};
                for (int r : rows) {
                    sum[r + col[r]]--;
                    diff[r - col[r] + n]--;
                }
                // all three queens move only when the columns are shifted cyclically
                for (int shift = 1; shift < MOVED; shift++) {
                    int placed = 0;
                    for (; placed < MOVED; placed++) {
                        int r = rows[placed], cl = col[rows[(placed + shift) % MOVED]];
                        if (sum[r + cl] || diff[r - cl + n])
                            break;
                        sum[r + cl]++;
                        diff[r - cl + n]++;
                    }
                    if (placed == MOVED)
                        count++;
                    while (placed-- > 0) {
                        int r = rows[placed], cl = col[rows[(placed + shift) % MOVED]];
                        sum[r + cl]--;
                        diff[r - cl + n]--;
                    }
                }
                for (int r : rows) {
                    sum[r + col[r]]++;
                    diff[r - col[r] + n]++;
                }
            }
    printf("%lld\n", count);
}
