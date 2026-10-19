#include <cstdio>

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    // n - k + 1 zeros, then 1, -1, 2, -2, ...: k distinct values and only k
    // distinct segment sums, the least possible
    for (int i = 0; i < n - k + 1; ++i) printf(i ? " 0" : "0");
    for (int i = 1; i < k; ++i) printf(" %d", i % 2 ? (i + 1) / 2 : -(i / 2));
    printf("\n");
}
