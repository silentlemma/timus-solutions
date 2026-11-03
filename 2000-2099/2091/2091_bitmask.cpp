#include <algorithm>
#include <cstdint>
#include <cstdio>

const int MAX_COURSES = 100, WORD_BITS = 64, GROUPS = 4;

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    uint64_t low[MAX_COURSES] = {}, high[MAX_COURSES] = {};
    int counts[MAX_COURSES] = {};
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            int value;
            scanf("%d", &value);
            if (value) {
                counts[c]++;
                if (r < WORD_BITS)
                    low[c] |= uint64_t(1) << r;
                else
                    high[c] |= uint64_t(1) << (r - WORD_BITS);
            }
        }
    }
    int best = n + 1, first = 0, second = 1;
    for (int a = 0; a < m; a++) {
        for (int b = a + 1; b < m; b++) {
            // Both is the intersection; the other groups follow by subtraction.
            int both =
                __builtin_popcountll(low[a] & low[b]) + __builtin_popcountll(high[a] & high[b]);
            int score = std::max(
                {both, counts[a] - both, counts[b] - both, n - counts[a] - counts[b] + both});
            if (score < best) {
                best = score;
                first = a;
                second = b;
            }
            if (best == (n + GROUPS - 1) / GROUPS) {
                printf("%d\n%d %d\n", best, first + 1, second + 1);
                return 0;
            }
        }
    }
    printf("%d\n%d %d\n", best, first + 1, second + 1);
}
