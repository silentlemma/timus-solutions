#include <algorithm>
#include <climits>
#include <cstdio>
#include <vector>

typedef long long ll;

// the smallest whole x with x * t >= need, also for a negative need
ll ceilDiv(ll need, ll t) { return need >= 0 ? (need + t - 1) / t : -(-need / t); }

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;
    std::vector<ll> plan(n + m - 1);
    for (ll &v : plan) scanf("%lld", &v);
    ll stock = 0;
    for (int i = 0; i < n; i++) {
        // after t months of the same change x the stock is stock + t x, which
        // must reach the plan of that month
        ll x = LLONG_MIN;
        for (int t = 1; t <= m; t++) x = std::max(x, ceilDiv(plan[i + t - 1] - stock, t));
        printf(i ? " %lld" : "%lld", x);
        stock += x;
    }
    printf("\n");
    return 0;
}
