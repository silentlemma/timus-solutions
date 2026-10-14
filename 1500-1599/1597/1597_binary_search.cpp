#include <cstdio>

typedef long long ll;
const ll MOST_DROPS = 2000000000; // two eggs already cover 10^18 floors with this many

// floors that t drops with k eggs can settle, the sum of C(t, i) over
// i = 1..k, or n + 1 if that is more
ll covered(ll t, ll k, ll n) {
    ll total = 0, term = 1;
    for (ll i = 1; i <= k && i <= t; i++) {
        // term * (t - i + 1) / i without overflow: split term by i
        ll q = term / i, r = term % i, f = t - i + 1;
        if (q > n / f)
            return n + 1;
        term = q * f + r * f / i;
        total += term;
        if (total > n)
            return n + 1;
    }
    return total;
}

ll drops(ll k, ll n) {
    if (k == 1)
        return n;
    ll lo = 1, hi = MOST_DROPS;
    while (lo < hi) {
        ll mid = (lo + hi) / 2;
        if (covered(mid, k, n) >= n)
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
}

int main() {
    ll k, n;
    while (scanf("%lld %lld", &k, &n) == 2 && (k != 0 || n != 0))
        printf("%lld\n", drops(k, n));
}
