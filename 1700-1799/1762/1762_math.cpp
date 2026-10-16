#include <cstdio>

typedef long long ll;

ll gcd(ll x, ll y) { return y ? gcd(y, x % y) : x; }

int main() {
    ll n, m;
    if (scanf("%lld %lld", &n, &m) != 2) return 0;
    ll a = n - 1, b = m - 1, g = gcd(a, b);
    // the walk takes lcm(a, b) steps and turns every tile it passes over, so
    // a tile passed twice ends up white again; in units of g the crossings
    // are the inner points (x, y) with x and y both odd or both even
    ll steps = a / g * b;
    ll wide = a / g, tall = b / g;
    ll crossings = (wide / 2) * (tall / 2) + ((wide - 1) / 2) * ((tall - 1) / 2);
    printf("%lld\n", steps + 1 - 2 * crossings);
    return 0;
}
