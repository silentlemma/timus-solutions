#include <cstdio>
#include <vector>

constexpr long long MOD = 1000000007;

long long power(long long base, long long exponent) {
    long long result = 1;
    base %= MOD;
    while (exponent > 0) {
        if (exponent & 1) result = result * base % MOD;
        base = base * base % MOD;
        exponent >>= 1;
    }
    return result;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    std::vector<int> wishes(n);
    for (auto &s : wishes) scanf("%d", &s);
    std::vector<long long> fact(m + 1, 1), inv(m + 1, 1);
    for (int i = 1; i <= m; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[m] = power(fact[m], MOD - 2);
    for (int i = m; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;

    // ways[j]: the sponsors so far fill exactly j problems once; with t
    // mentions placed, (t - j) / 2 problems hold two sponsors and the rest none
    std::vector<long long> ways(m + 1, 0);
    ways[0] = 1;
    int placed = 0;
    for (int s : wishes) {
        std::vector<long long> next(m + 1, 0);
        for (int j = placed % 2; j <= m; j += 2) {
            if (ways[j] == 0) continue;
            int empty = m - j - (placed - j) / 2;
            // a of the new mentions go to problems with one sponsor, the
            // other s - a to empty problems
            long long base = ways[j] * fact[j] % MOD * fact[empty] % MOD;
            int from = s - empty > 0 ? s - empty : 0;
            int to = s < j ? s : j;
            for (int a = from; a <= to; a++) {
                int rest = s - a;
                long long term = base * inv[a] % MOD * inv[j - a] % MOD;
                term = term * inv[rest] % MOD * inv[empty - rest] % MOD;
                long long &target = next[j - a + rest];
                target = (target + term) % MOD;
            }
        }
        ways.swap(next);
        placed += s;
    }
    long long answer = 0;
    for (long long w : ways) answer = (answer + w) % MOD;
    printf("%lld\n", answer);
    return 0;
}
