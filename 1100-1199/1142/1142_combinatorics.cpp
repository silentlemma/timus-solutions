#include <cstdio>

// inputs are at most this
const int LARGEST = 10;

int main() {
    // a(n) counts weak orders of n objects: the k objects tied for the
    // smallest place are any k of them, followed by a weak order of the rest
    long long binom[LARGEST + 1][LARGEST + 1] = {}, a[LARGEST + 1] = {1};
    for (int n = 0; n <= LARGEST; n++) {
        binom[n][0] = binom[n][n] = 1;
        for (int k = 1; k < n; k++)
            binom[n][k] = binom[n - 1][k - 1] + binom[n - 1][k];
    }
    for (int n = 1; n <= LARGEST; n++)
        for (int k = 1; k <= n; k++)
            a[n] += binom[n][k] * a[n - k];
    int n;
    while (scanf("%d", &n) == 1 && n >= 0)
        printf("%lld\n", a[n]);
}
