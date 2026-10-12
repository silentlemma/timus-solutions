#include <cstdio>

int main() {
    long long n = 0;
    if (scanf("%lld", &n) != 1)
        return 0;
    // modulo n^2 + 1 the first number is -1 and the second is n, so the sum
    // of their squares is 1 + n^2, a multiple of n^2 + 1
    printf("%lld %lld %lld\n", n * n, n * n + n + 1, n * n + 1);
    return 0;
}
