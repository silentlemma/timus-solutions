#include <cstdio>

int main() {
    long long n, k;
    if (scanf("%lld %lld", &n, &k) != 2)
        return 1;
    // numbers of valid prefixes ending with a zero and with another digit,
    // where the first digit is not zero
    long long zero = 0, other = k - 1;
    for (long long i = 1; i < n; i++) {
        long long nextZero = other;
        other = (zero + other) * (k - 1);
        zero = nextZero;
    }
    printf("%lld\n", zero + other);
}
