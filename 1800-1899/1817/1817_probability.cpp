#include <cstdio>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    for (int k = 0; k < n; k++) {
        // kids take the first free horse at or after a random one: linear
        // probing on a circle of n slots with k taken. By Knuth's analysis
        // the wait is (Q - 1)/2 with Q = sum (j + 1) k!/(k - j)! / n^j
        double q = 0, term = 1;
        for (int j = 0; j <= k; j++) {
            q += (j + 1) * term;
            term *= (double)(k - j) / n;
        }
        printf("%.9f\n", (q - 1) / 2);
    }
    return 0;
}
