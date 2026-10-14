#include <cmath>
#include <cstdio>

int main() {
    long long n;
    if (scanf("%lld", &n) != 1)
        return 0;
    // x_n = 2/3 - (-1)^n (2/3) 2^-n: an even n leaves k sixes while
    // 10^k <= 2^n, an odd n while 2 10^k < 2^n, that is 10^k <= 2^(n-1)
    long long m = n % 2 == 0 ? n : n - 1;
    printf("%lld\n", (long long)floor(m * log10(2.0)));
}
