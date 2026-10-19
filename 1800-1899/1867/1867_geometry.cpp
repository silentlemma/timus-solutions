#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;

int n;
vector<vector<ll>> d;
vector<ll> xs, ys;

ll isqrt(ll v) {
    ll r = (ll)sqrtl((long double)v);
    while (r * r > v) r--;
    while ((r + 1) * (r + 1) <= v) r++;
    return r;
}

// atom 0 at the origin, atom p at (a, b); every other atom follows from its
// distances to these two up to a reflection in the line through them, and
// the first atom off that line picks the side by flip
bool place(int p, ll a, ll b, bool flip) {
    ll big = a * a + b * b;
    int first = flip ? -1 : 1;
    xs.assign(n, 0);
    ys.assign(n, 0);
    for (int i = 1; i < n; i++) {
        ll twice = d[0][i] - d[p][i] + big;  // twice the dot product with (a, b)
        if (twice % 2) return false;
        ll dot = twice / 2;
        ll square = big * d[0][i] - dot * dot;  // the cross product, squared
        if (square < 0) return false;
        ll cross = isqrt(square);
        if (cross * cross != square) return false;
        bool done = false;
        for (int sign : {first, -first}) {
            ll nx = a * dot + b * sign * cross, ny = b * dot - a * sign * cross;
            if (nx % big || ny % big) continue;
            ll x = nx / big, y = ny / big;
            bool fits = true;
            for (int j = 0; j < i && fits; j++) {
                fits = (x - xs[j]) * (x - xs[j]) + (y - ys[j]) * (y - ys[j]) == d[i][j];
            }
            if (fits) {
                xs[i] = x;
                ys[i] = y;
                done = true;
                break;
            }
        }
        if (!done) return false;
    }
    return true;
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    d.assign(n, vector<ll>(n));
    for (auto& row : d)
        for (ll& v : row) scanf("%lld", &v);
    int p = 0;
    for (int i = 1; i < n && !p; i++)
        if (d[0][i]) p = i;
    if (p == 0) {
        // everything sits at the origin
        bool fine = true;
        for (auto& row : d)
            for (ll v : row) fine = fine && v == 0;
        if (!fine) {
            puts("Impossible");
            return 0;
        }
        for (int i = 0; i < n; i++) puts("0 0");
        return 0;
    }
    ll big = d[0][p];
    // the symmetries of the grid bring atom p to (a, b) with 0 <= a <= b
    for (ll a = 0; 2 * a * a <= big; a++) {
        ll b = isqrt(big - a * a);
        if (a * a + b * b != big) continue;
        for (bool flip : {false, true}) {
            if (place(p, a, b, flip)) {
                for (int i = 0; i < n; i++) printf("%lld %lld\n", xs[i], ys[i]);
                return 0;
            }
        }
    }
    puts("Impossible");
    return 0;
}
