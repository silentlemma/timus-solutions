#include <cstdio>
#include <sstream>
#include <vector>

typedef long long ll;
typedef std::vector<ll> Poly;

const ll MOD = 1000000009;
// with six sectors the jumps forward and back by three land on the same
// sector, so that table is counted on its own
const ll SIX = 6, SIX_WAYS = 12;
// from seven sectors on the counts follow a linear recurrence of order 19,
// found with the Berlekamp-Massey method from counts made by a search over
// the sectors and checked on every table up to 200 sectors
const ll FIRST_SECTORS = 7;
const char *STEP_TEXT = "1 2 -1 1 -2 -1 -2 -3 3 -1 5 2 2 1 -2 0 -3 0 -1";
const char *FIRST_TEXT =
    "46 144 110 312 290 670 706 1538 1732 3504 4288 8098 "
    "10568 19044 26042 45222 64220 108382 158324";

Poly steps, first;

Poly parse(const char *text) {
    std::istringstream in(text);
    Poly values;
    for (ll v; in >> v;) values.push_back(v);
    return values;
}

// the product of two polynomials modulo the recurrence's characteristic
// polynomial x^k - sum of steps[j] x^(k-1-j)
Poly times(const Poly &p, const Poly &q) {
    int k = steps.size();
    Poly full(2 * k - 1, 0);
    for (int i = 0; i < k; i++) {
        if (!p[i]) continue;
        for (int j = 0; j < k; j++) full[i + j] = (full[i + j] + p[i] * q[j]) % MOD;
    }
    for (int i = 2 * k - 2; i >= k; i--) {
        if (!full[i]) continue;
        for (int j = 0; j < k; j++) {
            full[i - 1 - j] = ((full[i - 1 - j] + full[i] * steps[j]) % MOD + MOD) % MOD;
        }
    }
    full.resize(k);
    return full;
}

int main() {
    ll n;
    if (scanf("%lld", &n) != 1) return 0;
    if (n == SIX) {
        printf("%lld\n", SIX_WAYS);
        return 0;
    }
    steps = parse(STEP_TEXT);
    first = parse(FIRST_TEXT);
    int k = steps.size();
    // x^(n - 7) reduced by the recurrence gives the count as a mix of the
    // first k counts
    Poly power(k, 0), base(k, 0);
    power[0] = 1;
    base[1] = 1;
    for (ll e = n - FIRST_SECTORS; e > 0; e >>= 1) {
        if (e & 1) power = times(power, base);
        base = times(base, base);
    }
    ll answer = 0;
    for (int i = 0; i < k; i++) answer = (answer + power[i] * first[i]) % MOD;
    printf("%lld\n", answer);
    return 0;
}
