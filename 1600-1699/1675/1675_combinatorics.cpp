#include <algorithm>
#include <cstdio>
#include <vector>

typedef long long ll;
const ll MOD = 1000000007;

ll power(ll base, ll exp) {
    ll result = 1;
    for (base %= MOD; exp > 0; exp >>= 1, base = base * base % MOD) {
        if (exp & 1) {
            result = result * base % MOD;
        }
    }
    return result;
}

int main() {
    int m, n, k, l;
    scanf("%d %d %d %d", &m, &n, &k, &l);
    int top = std::max(m, n);
    std::vector<ll> fact(top + 1, 1), inv(top + 1, 1);
    for (int i = 1; i <= top; i++) {
        fact[i] = fact[i - 1] * i % MOD;
    }
    inv[top] = power(fact[top], MOD - 2);
    for (int i = top; i > 0; i--) {
        inv[i - 1] = inv[i] * i % MOD;
    }
    auto choose = [&](int a, int b) { return fact[a] * inv[b] % MOD * inv[a - b] % MOD; };
    // the other a x b cells must leave no row and no column empty. With j of
    // the b columns forced empty, each of the a rows is any nonzero pattern
    // on the rest; inclusion-exclusion over j, along the shorter side
    int a = std::min(m - k, n - l), b = std::max(m - k, n - l);
    ll rest = 0;
    for (int j = 0; j <= a; j++) {
        ll term = choose(a, j) * power((power(2, a - j) - 1 + MOD) % MOD, b) % MOD;
        rest = (rest + (j % 2 ? MOD - term : term)) % MOD;
    }
    printf("%lld\n", choose(m, k) * choose(n, l) % MOD * rest % MOD);
}
