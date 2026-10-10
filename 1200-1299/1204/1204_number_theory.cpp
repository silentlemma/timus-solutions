#include <algorithm>
#include <cstdio>
#include <vector>

const int ROOT = 31623;

// The inverse of a modulo m by the extended Euclidean algorithm.
long long inverse(long long a, long long m) {
    long long r0 = m, r1 = a % m, s0 = 0, s1 = 1;
    while (r1 != 0) {
        long long t = r0 / r1;
        std::swap(r0 -= t * r1, r1);
        std::swap(s0 -= t * s1, s1);
    }
    return (s0 % m + m) % m;
}

int main() {
    std::vector<bool> composite(ROOT + 1, false);
    std::vector<int> primes;
    for (int i = 2; i <= ROOT; i++) {
        if (!composite[i]) {
            primes.push_back(i);
            for (long long j = (long long)i * i; j <= ROOT; j += i) {
                composite[j] = true;
            }
        }
    }
    int k;
    scanf("%d", &k);
    while (k--) {
        long long n, p = 0;
        scanf("%lld", &n);
        for (int d : primes) {
            if (n % d == 0) {
                p = d;
                break;
            }
        }
        long long q = n / p;
        // x = 1 (mod p) and x = 0 (mod q); the other root is n + 1 - x
        long long x = q * inverse(q, p) % n, y = n + 1 - x;
        printf("0 1 %lld %lld\n", std::min(x, y), std::max(x, y));
    }
}
