#include <cstdio>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int stops = 2 * n;
    for (int k = 0; k < n; k++) {
        // k, k + 1, k - 1, k + 2, k - 2, ..., k + n around the circle of stops:
        // its neighbouring pairs are exactly those with sum 2k or 2k + 1
        printf("%d", k + 1);
        for (int j = 1; j <= n; j++) {
            printf(" %d", (k + j) % stops + 1);
            if (j < n)
                printf(" %d", (k - j + stops) % stops + 1);
        }
        printf("\n");
    }
}
