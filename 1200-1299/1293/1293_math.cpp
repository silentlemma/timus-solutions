#include <cstdio>

const int FIELDS = 3;

int main() {
    long long n = 0, a = 0, b = 0;
    if (scanf("%lld %lld %lld", &n, &a, &b) != FIELDS)
        return 0;
    // each panel has two sides of A * B square metres
    printf("%lld\n", 2 * n * a * b);
    return 0;
}
