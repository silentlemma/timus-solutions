#include <cmath>
#include <cstdio>

int main() {
    long long s;
    if (scanf("%lld", &s) != 1)
        return 0;
    // s = n*a + n(n-1)/2 with a >= 1 needs n(n+1)/2 <= s; try the longest first
    long long n = (long long)std::sqrt(2.0 * s);
    while (n * (n + 1) / 2 > s)
        n--;
    while ((s - n * (n - 1) / 2) % n != 0)
        n--;
    printf("%lld %lld\n", (s - n * (n - 1) / 2) / n, n);
}
