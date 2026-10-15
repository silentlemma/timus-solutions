#include <algorithm>
#include <cstdio>

typedef long long ll;

// numbers 1 .. t that are sums of contests: k contests give [kx, ky],
// once k (y - x) >= x - 1 the next interval touches this one, so from
// the first such k on everything is covered, and before it they are apart
ll covered(ll t, ll x, ll y) {
    if (t < x) {
        return 0;
    }
    if (y == x) {
        return t / x;
    }
    ll joined = std::max(1LL, (x - 1 + (y - x) - 1) / (y - x));
    ll full = std::min(joined - 1, t / y);  // the intervals that end by t
    ll count = (y - x) * (full * (full + 1) / 2) + full;
    ll k = full + 1;
    if (k <= joined - 1 && k <= t / x) {
        count += t - k * x + 1;
    }
    if (joined <= t / x) {
        count += t - joined * x + 1;
    }
    return count;
}

int main() {
    ll x, y, low, high;
    scanf("%lld %lld %lld %lld", &x, &y, &low, &high);
    printf("%lld\n", covered(high, x, y) - covered(low - 1, x, y));
}
