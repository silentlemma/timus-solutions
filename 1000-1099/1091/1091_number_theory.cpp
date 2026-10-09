#include <algorithm>
#include <cstdio>
#include <vector>

const long long CAPACITY = 10000;

int main() {
    int k, s;
    if (scanf("%d %d", &k, &s) != 2)
        return 0;
    std::vector<std::vector<long long>> binom(s + 1, std::vector<long long>(s + 1, 0));
    for (int n = 0; n <= s; n++) {
        binom[n][0] = 1;
        for (int r = 1; r <= n; r++)
            binom[n][r] = binom[n - 1][r - 1] + (r < n ? binom[n - 1][r] : 0);
    }
    // Moebius function by a sieve: -1 per prime factor, 0 with a square factor
    std::vector<int> mu(s + 1, 1);
    std::vector<bool> prime(s + 1, true);
    for (int p = 2; p <= s; p++) {
        if (!prime[p])
            continue;
        for (int m = p; m <= s; m += p) {
            prime[m] = m == p;
            mu[m] = -mu[m];
        }
        for (int m = p * p; m <= s; m += p * p)
            mu[m] = 0;
    }
    // inclusion-exclusion: sets of multiples of d count with the sign -mu(d)
    long long total = 0;
    for (int d = 2; d <= s; d++)
        if (s / d >= k)
            total -= mu[d] * binom[s / d][k];
    printf("%lld\n", std::min(total, CAPACITY));
}
