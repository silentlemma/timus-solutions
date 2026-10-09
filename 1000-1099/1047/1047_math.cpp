#include <cmath>
#include <cstdio>
#include <cstdlib>

const int CENTS = 100;

// the input numbers in hundredths
long long read_cents() {
    double v;
    if (scanf("%lf", &v) != 1)
        return 0;
    return std::llround(v * CENTS);
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    long long first = read_cents(), last = read_cents();
    // with d[i] = a[i] - a[i-1] the relation reads d[i+1] = d[i] + 2 c[i], so
    // a[N+1] - a[0] = (N + 1) d[1] + 2 sum (N + 1 - i) c[i]
    long long weighted = 0;
    for (int i = 1; i <= n; i++)
        weighted += (long long)(n + 1 - i) * read_cents();
    long long num = (long long)n * first + last - 2 * weighted, den = n + 1;
    // the answer has two decimals; rounding only guards against bad input
    long long q = (2 * std::llabs(num) + den) / (2 * den);
    printf("%s%lld.%02lld\n", num < 0 && q > 0 ? "-" : "", q / CENTS, q % CENTS);
}
