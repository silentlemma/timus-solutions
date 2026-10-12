#include <cstdio>

int main() {
    long long n = 0;
    if (scanf("%lld", &n) != 1)
        return 0;
    // (n^2)^2 = n^4 = n^3 * n
    printf("%lld\n%lld\n", n * n, n);
    return 0;
}
