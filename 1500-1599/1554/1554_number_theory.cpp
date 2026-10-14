#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const long long MOD = 2007;

// x^-1 modulo MOD by the extended Euclidean algorithm
long long inverse(long long x) {
    long long a = x % MOD, b = MOD, u = 1, v = 0;
    while (b) {
        long long q = a / b;
        a -= q * b;
        u -= q * v;
        swap(a, b);
        swap(u, v);
    }
    return (u % MOD + MOD) % MOD;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<long long> f(n + 1), g(n + 1), acc(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        if (scanf("%lld", &f[i]) != 1)
            return 0;
        f[i] %= MOD;
    }
    // (F * G)(n) sums F(n / d) G(d) over the divisors d of n and is 0 for n > 1,
    // so G(n) = -G(1) * (the sum over the proper divisors), with G(1) = 1 / F(1),
    // and a sieve adds G(d) times F to every multiple of d once G(d) is known
    long long first = inverse(f[1]);
    for (int d = 1; d <= n; d++) {
        g[d] = d == 1 ? first : (MOD - first * (acc[d] % MOD) % MOD) % MOD;
        for (int k = 2; d * k <= n; k++)
            acc[d * k] = (acc[d * k] + f[k] * g[d]) % MOD;
    }
    for (int i = 1; i <= n; i++)
        printf(i > 1 ? " %lld" : "%lld", g[i]);
    printf("\n");
}
