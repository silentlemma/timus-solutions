#include <cstdio>

int main() {
    long long n, k;
    if (scanf("%lld %lld", &n, &k) != 2)
        return 1;
    // z zeros, no two adjacent, among the n - 1 places after the first digit:
    // C(n - z, z) ways; the other n - z digits are nonzero
    long long total = 0;
    for (long long z = 0; 2 * z <= n; z++) {
        long long ways = 1;
        for (long long i = 1; i <= z; i++)
            ways = ways * (n - z - i + 1) / i;
        for (long long i = 0; i < n - z; i++)
            ways *= k - 1;
        total += ways;
    }
    printf("%lld\n", total);
}
