#include <cmath>
#include <cstdio>

const long long FIRST_ODD_PRIME = 3;  // n is odd

// the integer square root, corrected after the floating-point guess
static long long isqrt(long long n) {
    long long r = std::sqrt((double)n);
    while (r * r > n) r--;
    while ((r + 1) * (r + 1) <= n) r++;
    return r;
}

int main() {
    long long n;
    if (scanf("%lld", &n) != 1) return 0;
    // the gods number a square divisor of n: a number has an odd count of
    // divisors exactly when it is a square
    long long best = 1;
    for (long long p = FIRST_ODD_PRIME; p * p * p <= n; p += 2) {
        int power = 0;
        while (n % p == 0) {
            n /= p;
            power++;
        }
        for (int k = 0; k < power / 2; k++) best *= p * p;
    }
    // what is left has no prime factor up to its cube root, so at most two
    // prime factors: it is a square only as the square of one prime
    long long r = isqrt(n);
    if (r * r == n) best *= n;
    printf("%lld\n", best);
    return 0;
}
