#include <cstdio>
#include <set>
#include <string>

int main() {
    const long long BASE = 10, ELEVEN = 11;
    long long n;
    scanf("%lld", &n);
    std::set<long long> found;
    // strike digit d at place k from x = (a * 10 + d) * 10^k + b, b < 10^k:
    // then y = a * 10^k + b and x + y = (11a + d) * 10^k + 2b
    for (long long power = 1; power <= n; power *= BASE) {
        for (long long carry = 0; carry < 2; carry++) {
            long long twice = n % power + carry * power;
            if (twice % 2 == 0 && twice / 2 < power) {
                long long b = twice / 2, q = (n - twice) / power;
                long long a = q / ELEVEN, d = q % ELEVEN;
                long long x = (a * BASE + d) * power + b;
                // x has at least two digits and starts with a nonzero digit
                if (d < BASE && x >= BASE && (a > 0 || d > 0)) {
                    found.insert(x);
                }
            }
        }
    }
    printf("%d\n", (int)found.size());
    for (long long x : found) {
        int width = std::to_string(x).size() - 1;
        printf("%lld + %0*lld = %lld\n", x, width, n - x, n);
    }
}
