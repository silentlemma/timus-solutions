#include <cmath>
#include <cstdio>
#include <vector>

typedef long long ll;
const ll MOD = 1000000007;

struct Matrix {
    ll a, b, c, d;  // rows first: a b / c d
};

Matrix mul(const Matrix &x, const Matrix &y) {
    return {(x.a * y.a + x.b * y.c) % MOD, (x.a * y.b + x.b * y.d) % MOD,
            (x.c * y.a + x.d * y.c) % MOD, (x.c * y.b + x.d * y.d) % MOD};
}

// [p_k p_(k-1); q_k q_(k-1)] grows by the factor [a 1; 1 0]
Matrix term(ll a) { return {a % MOD, 1, 1, 0}; }

int main() {
    ll x, k;
    if (scanf("%lld %lld", &x, &k) != 2) return 0;
    ll a0 = (ll)std::sqrt((double)x);
    while (a0 * a0 > x) a0--;
    while ((a0 + 1) * (a0 + 1) <= x) a0++;
    // the partial quotients of sqrt(x) repeat with a period that ends at
    // the first term equal to 2 a0
    std::vector<ll> period;
    ll m = 0, d = 1, a = a0;
    while (a != 2 * a0) {
        m = d * a - m;
        d = (x - m * m) / d;
        a = (a0 + m) / d;
        period.push_back(a);
    }
    Matrix cycle = {1, 0, 0, 1};
    for (ll v : period) cycle = mul(cycle, term(v));
    Matrix result = term(a0), power = cycle;
    ll len = period.size();
    for (ll full = k / len; full; full >>= 1) {
        if (full & 1) result = mul(result, power);
        power = mul(power, power);
    }
    for (ll i = 0; i < k % len; i++) result = mul(result, term(period[i]));
    // convergents are always in lowest terms
    printf("%lld/%lld\n", result.a, result.c);
    return 0;
}
