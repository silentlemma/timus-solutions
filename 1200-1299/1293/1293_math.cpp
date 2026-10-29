#include <cstdio>

int main() {
    long long n, a, b;
    scanf("%lld %lld %lld", &n, &a, &b);
    // each panel has two sides of A * B square metres
    printf("%lld\n", 2 * n * a * b);
}
