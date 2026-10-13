#include <cstdio>

// how many primes multiply to n, counted with repetition
int primeFactors(long long n) {
    int count = 0;
    for (long long d = 2; d * d <= n; d++)
        while (n % d == 0) {
            n /= d;
            count++;
        }
    return count + (n > 1 ? 1 : 0);
}

int main() {
    int t = 0;
    if (scanf("%d", &t) != 1)
        return 0;
    for (int i = 0; i < t; i++) {
        long long a = 0, b = 0;
        if (scanf("%lld %lld", &a, &b) != 2)
            return 0;
        // every step multiplies the number by at least one prime
        printf("%d\n", b % a == 0 ? 1 + primeFactors(b / a) : 0);
    }
    return 0;
}
