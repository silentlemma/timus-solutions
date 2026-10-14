#include <cstdio>
#include <numeric>

int main() {
    long long n;
    if (scanf("%lld", &n) != 1)
        return 0;
    // the chance that the row ends with two cards: (n^2 + 3n - 2) / (2n (2n - 1))
    long long num = n * (n + 2) + n - 2;
    long long den = 2 * n * (2 * n - 1);
    long long g = std::gcd(num, den);
    printf("%lld/%lld\n", num / g, den / g);
}
