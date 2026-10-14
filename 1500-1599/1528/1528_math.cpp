#include <cstdio>

int main() {
    // g(n) = n by induction, so f(n) = 1 + sum of i f(i) = n f(n - 1) = n!
    long long n, p;
    while (scanf("%lld %lld", &n, &p) == 2 && (n != 0 || p != 0)) {
        long long r = n >= p ? 0 : 1; // when n >= p, p itself is a factor of n!
        for (long long i = 2; i <= n && r != 0; i++)
            r = r * i % p;
        printf("%lld\n", r);
    }
}
