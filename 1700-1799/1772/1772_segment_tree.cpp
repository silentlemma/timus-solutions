#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>

typedef long long ll;

const ll FAR = 1LL << 40;

int n, s, size;
std::vector<int> latest;
std::vector<ll> leftPart, rightPart;

// the cost of a lane comes from the latest obstacle covering it, as
// min(left[t] + x, right[t] - x), or from the start as |x - s| if none
ll cost(int x) {
    int t = 0;
    for (int node = x + size; node; node >>= 1) t = std::max(t, latest[node]);
    if (t == 0) return std::abs(x - s);
    return std::min(leftPart[t] + x, rightPart[t] - x);
}

int main() {
    int k;
    if (scanf("%d %d %d", &n, &s, &k) < 1) return 0;
    size = 1;
    while (size <= n) size *= 2;
    // latest[node]: the last obstacle whose lanes cover the node's whole range
    latest.assign(2 * size, 0);
    leftPart.assign(k + 1, 0);
    rightPart.assign(k + 1, 0);
    for (int t = 1; t <= k; t++) {
        int lo, hi;
        scanf("%d %d", &lo, &hi);
        // the cost stays one per lane apart, so going round the obstacle
        // only needs the lanes just beside it
        ll below = lo > 1 ? cost(lo - 1) : FAR, above = hi < n ? cost(hi + 1) : FAR;
        leftPart[t] = below - (lo - 1);
        rightPart[t] = above + hi + 1;
        for (int a = lo + size, b = hi + size + 1; a < b; a >>= 1, b >>= 1) {
            if (a & 1) latest[a++] = t;
            if (b & 1) latest[--b] = t;
        }
    }
    ll best = FAR;
    for (int x = 1; x <= n; x++) best = std::min(best, cost(x));
    printf("%lld\n", best);
    return 0;
}
