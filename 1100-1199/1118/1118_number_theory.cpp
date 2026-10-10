#include <cstdio>

// the sum of all divisors of n by trial division
long long divisor_sum(long long n) {
    long long total = 0;
    for (long long d = 1; d * d <= n; d++)
        if (n % d == 0)
            total += d * d == n ? d : d + n / d;
    return total;
}

int main() {
    long long lo, hi;
    if (scanf("%lld %lld", &lo, &hi) != 2)
        return 0;
    // 1 has no proper divisors at all
    if (lo == 1) {
        printf("1\n");
        return 0;
    }
    // a prime p has the ratio 1/p, and the largest prime in range beats every
    // composite there (it is above hi / 2 by Bertrand's postulate), so only a
    // range without primes, at most 113 numbers here, needs comparing
    for (long long n = hi; n >= lo; n--)
        if (divisor_sum(n) == n + 1) {
            printf("%lld\n", n);
            return 0;
        }
    long long best = lo;
    for (long long n = lo + 1; n <= hi; n++)
        // sigma(n) / n < sigma(best) / best, the smaller number winning a tie
        if (divisor_sum(n) * best < divisor_sum(best) * n)
            best = n;
    printf("%lld\n", best);
}
