#include <algorithm>
#include <cstdio>

const int MAX_POINTS = 200;

int main() {
    int n, x[MAX_POINTS], y[MAX_POINTS];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d%d", &x[i], &y[i]);
    int best = 2;
    // Every line through two input points is tried; cross products are exact.
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int dx = x[j] - x[i], dy = y[j] - y[i], count = 0;
            for (int k = 0; k < n; k++)
                if ((x[k] - x[i]) * dy == (y[k] - y[i]) * dx)
                    count++;
            best = std::max(best, count);
            if (best == n) {
                printf("%d\n", best);
                return 0;
            }
        }
    }
    printf("%d\n", best);
}
