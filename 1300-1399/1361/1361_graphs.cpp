#include <algorithm>
#include <cstdio>
#include <vector>

typedef long long ll;

// when the walk from start is at each node it reaches: the first moment
// (or -1 if never) and the period, 0 for a node passed only once
void visits(const std::vector<int> &step, int start, std::vector<ll> &first,
            std::vector<ll> &period) {
    int n = (int)step.size() - 1;
    first.assign(n + 1, -1);
    period.assign(n + 1, 0);
    std::vector<int> order;
    int v = start;
    while (first[v] < 0) {
        first[v] = (ll)order.size();
        order.push_back(v);
        v = step[v];
    }
    ll loopStart = first[v], len = (ll)order.size() - first[v];
    for (int u : order)
        if (first[u] >= loopStart)
            period[u] = len;
}

ll gcdOf(ll a, ll b) { return b ? gcdOf(b, a % b) : a; }

// x with a x = 1 (mod m), for a and m coprime
ll inverse(ll a, ll m) {
    ll g = m, x = 0, x1 = 1, a1 = a % m;
    while (a1) {
        ll q = g / a1, t = g - q * a1;
        g = a1;
        a1 = t;
        t = x - q * x1;
        x = x1;
        x1 = t;
    }
    return (x % m + m) % m;
}

// the least moment in both sets r + k L (k >= 0), or -1
ll firstCommon(ll ra, ll la, ll rb, ll lb) {
    if (la == 0 && lb == 0)
        return ra == rb ? ra : -1;
    if (la == 0) {
        std::swap(ra, rb);
        std::swap(la, lb);
    }
    if (lb == 0) // one moment rb against the moments ra, ra + la, ...
        return rb >= ra && (rb - ra) % la == 0 ? rb : -1;
    ll g = gcdOf(la, lb);
    if ((rb - ra) % g != 0)
        return -1;
    ll m = lb / g;
    ll diff = ((rb - ra) / g % m + m) % m;
    ll k = m > 1 ? diff * inverse(la / g % m, m) % m : 0;
    ll t = ra + la * k, whole = la / g * lb;
    if (t < rb)
        t += (rb - t + whole - 1) / whole * whole;
    return t;
}

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> left(n + 1), right(n + 1);
    for (int v = 1; v <= n; v++) {
        int x = 0, last = 0;
        if (scanf("%d", &x) != 1)
            return 0;
        left[v] = x;
        while (x != 0) {
            last = x;
            if (scanf("%d", &x) != 1)
                return 0;
        }
        right[v] = last;
    }
    int a = 0, b = 0;
    if (scanf("%d %d", &a, &b) != 2)
        return 0;
    // A always takes the leftmost road and B the rightmost
    std::vector<ll> firstA, periodA, firstB, periodB;
    visits(left, a, firstA, periodA);
    visits(right, b, firstB, periodB);
    ll best = -1;
    for (int v = 1; v <= n; v++) {
        if (firstA[v] < 0 || firstB[v] < 0)
            continue;
        ll t = firstCommon(firstA[v], periodA[v], firstB[v], periodB[v]);
        if (t >= 0 && (best < 0 || t < best))
            best = t;
    }
    printf("%lld\n", best);
    return 0;
}
