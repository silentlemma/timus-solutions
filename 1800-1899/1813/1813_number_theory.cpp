#include <cstdio>

const long long FOUR = 4;

int main() {
    long long m;
    while (scanf("%lld", &m) == 1) {
        // by the Hull-Dobell theorem the full cycles come from a - 1
        // divisible by every prime of m, and by 4 when 4 divides m, with
        // any b coprime to m; so a runs over 1, 1 + c, ..., below m
        long long c = 1, rest = m;
        for (long long p = 2; p * p <= rest; p++) {
            if (rest % p == 0) {
                c *= p;
                while (rest % p == 0) rest /= p;
            }
        }
        if (rest > 1) c *= rest;
        if (m % FOUR == 0) c *= 2;
        printf("%lld\n", (m - c + 2) / 2);
    }
    return 0;
}
