#include <algorithm>
#include <cstdio>

typedef long long ll;

ll big, small;

ll pairs(ll k) { return k * (k - 1) / 2; }

ll gcd(ll x, ll y) { return y ? gcd(y, x % y) : x; }

// pairs among the first m sleepers on one page of both notebooks: walk the
// pages of the larger size, each cut by the smaller pages into a head,
// whole pages and a tail
ll shared(ll m) {
    ll total = 0;
    for (ll start = 0; start < m; start += big) {
        ll end = std::min(start + big, m);
        ll cut = (start / small + 1) * small;
        if (cut >= end) {
            total += pairs(end - start);
        } else {
            ll whole = (end - cut) / small, tail = (end - cut) % small;
            total += pairs(cut - start) + whole * pairs(small) + pairs(tail);
        }
    }
    return total;
}

int main() {
    ll a, b, n;
    if (scanf("%lld %lld %lld", &a, &b, &n) < 1) return 0;
    big = std::max(a, b);
    small = std::min(a, b);
    // both page breaks repeat every lcm(a, b) sleepers, and so do the pairs
    ll period = a / gcd(a, b) * b;
    ll both = period <= n ? n / period * shared(period) + shared(n % period) : shared(n);
    ll vasily = n / a * pairs(a) + pairs(n % a);
    printf("%lld\n", vasily - both);
    return 0;
}
