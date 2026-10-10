#include <cstdio>
#include <numeric>

int main() {
    long long n, m;
    if (scanf("%lld %lld", &n, &m) != 2)
        return 0;
    // an a by b grid: the diagonal crosses a + b - 2 inner lines, two at once
    // at each of the gcd(a, b) - 1 inner corners; it starts in one block and
    // every crossing enters a new one
    long long a = n - 1, b = m - 1;
    printf("%lld\n", a + b - std::gcd(a, b));
}
