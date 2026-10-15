#include <cmath>
#include <cstdio>

typedef long long ll;

const ll SMALL = 100;  // below this the first candidates are simply tried in turn

ll isqrt(ll v) {
    ll root = (ll)std::sqrt((double)v);
    while (root * root > v) {
        root--;
    }
    while ((root + 1) * (root + 1) <= v) {
        root++;
    }
    return root;
}

ll ceil_sqrt(ll v) {
    ll root = isqrt(v);
    return root * root == v ? root : root + 1;
}

bool fits(ll n, ll k) {
    return n / k == n / (k + 1);
}

ll least(ll n) {
    // the shares agree exactly when n mod k >= n div k, which needs k > s,
    // s = isqrt(n); with k = s + x and e = n - s^2 the quotient is s - x or
    // s - x + 1, and each case gives the least x in closed form
    if (n < SMALL) {
        ll k = 1;
        while (!fits(n, k)) {
            k++;
        }
        return k;
    }
    ll s = isqrt(n);
    ll e = n - s * s;
    ll xs[2];
    int count = 0;
    ll gap = s - e;
    if (gap >= 1) {
        // quotient s - x: the least x with x^2 + x >= gap (then x^2 - x < gap)
        ll x = isqrt(gap);
        while (x * x + x < gap) {
            x++;
        }
        while (x > 1 && (x - 1) * (x - 1) + (x - 1) >= gap) {
            x--;
        }
        xs[count++] = x;
    }
    // quotient s - x + 1: x^2 >= 2s - e + 1 > (x - 1)^2
    xs[count++] = ceil_sqrt(2 * s - e + 1);
    ll best = -1;
    for (int i = 0; i < count; i++) {
        for (ll d = -1; d <= 1; d++) {
            ll k = s + xs[i] + d;
            if (xs[i] + d >= 1 && fits(n, k) && (best < 0 || k < best)) {
                best = k;
            }
        }
    }
    return best;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        ll n;
        scanf("%lld", &n);
        printf("%lld\n", least(n));
    }
}
