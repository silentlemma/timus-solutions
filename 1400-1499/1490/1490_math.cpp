#include <cmath>
#include <cstdio>

typedef long long ll;
const ll QUARTERS = 4;

ll isqrt(ll n) {
    ll s = (ll)sqrtl((long double)n);
    while (s * s > n)
        s--;
    while ((s + 1) * (s + 1) <= n)
        s++;
    return s;
}

int main() {
    ll r;
    scanf("%lld", &r);
    // a tile shares more than one point with the disc exactly when its
    // corner nearest to the centre lies strictly inside: in one quarter,
    // tiles (i, j) with i^2 + j^2 < r^2, that is j <= isqrt(r^2 - i^2 - 1)
    ll total = 0;
    for (ll i = 0; i < r; i++)
        total += isqrt(r * r - i * i - 1) + 1;
    printf("%lld\n", QUARTERS * total);
}
