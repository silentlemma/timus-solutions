#include <cstdio>

const int DIGITS = 10;

int main() {
    long long n;
    if (scanf("%lld", &n) != 1)
        return 0;
    long long count[DIGITS] = {};
    for (long long p = 1; p <= n; p *= DIGITS) {
        // at this position the numbers up to n split into the part above, the
        // digit itself and the part below; every smaller upper part repeats
        // each digit p times here
        long long high = n / (p * DIGITS), cur = n / p % DIGITS, low = n % p;
        for (int d = 1; d < DIGITS; d++)
            count[d] += high * p + (d < cur ? p : d == cur ? low + 1 : 0);
        // a zero needs a nonzero digit above it, so the upper part 0 is skipped
        if (high)
            count[0] += (high - 1) * p + (cur ? p : low + 1);
    }
    for (long long c : count)
        printf("%lld\n", c);
}
