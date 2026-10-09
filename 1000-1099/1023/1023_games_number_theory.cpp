#include <cstdio>

const long long SMALLEST = 3;

int main() {
    long long k;
    if (scanf("%lld", &k) != 1)
        return 1;
    // the second player wins exactly when L + 1 divides K: find the smallest
    // divisor of K that is at least 3
    for (long long d = SMALLEST; d * d <= k; d++)
        if (k % d == 0) {
            printf("%lld\n", d - 1);
            return 0;
        }
    // no such divisor up to sqrt(K): above it the candidates are K / 2 and K
    long long d = k % 2 == 0 && k / 2 >= SMALLEST ? k / 2 : k;
    printf("%lld\n", d - 1);
}
