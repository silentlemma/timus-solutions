#include <cstdio>
#include <vector>

// answers above this are reported as 0
const int LIMIT = 10000;
// the input is M, N and K
const int FIELDS = 3;

int main() {
    int m, n, k;
    if (scanf("%d %d %d", &m, &n, &k) != FIELDS)
        return 0;
    // x tiles make one rectangle per divisor pair a * b = x with a <= b, that
    // is half the number of divisors, rounded up
    std::vector<int> divisors(LIMIT + 1, 0);
    for (int d = 1; d <= LIMIT; d++)
        for (int x = d; x <= LIMIT; x += d)
            divisors[x]++;
    auto shapes = [&](int x) { return (divisors[x] + 1) / 2; };
    for (int t = k + 1; t <= LIMIT; t++)
        if (shapes(t) == n && shapes(t - k) == m) {
            printf("%d\n", t);
            return 0;
        }
    puts("0");
}
