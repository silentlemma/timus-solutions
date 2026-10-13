#include <cmath>
#include <cstdio>
#include <string>

using namespace std;

typedef long long ll;
const ll SCALE = 100; // coordinates come with two decimals: work in hundredths
const int TEXT = 32;

ll hundredths(const char *s) {
    string t = s;
    size_t dot = t.find('.');
    string whole = t.substr(0, dot), part = dot == string::npos ? "" : t.substr(dot + 1);
    part = (part + "00").substr(0, 2);
    ll w = stoll(whole), p = stoll(part);
    return w * SCALE + (t[0] == '-' ? -p : p);
}

struct Point {
    ll x, y, z;
};

// The face A x B in the middle of the column lies at z = 0 with its
// corner (c, b + c) at the origin; every other face folds up from it.
Point fold(ll a, ll b, ll c, ll x, ll y) {
    if (x < c)
        return {0, y - b - c, c - x};
    if (x > c + a)
        return {a, y - b - c, x - c - a};
    if (y < b)
        return {x - c, b - y, c};
    if (y < b + c)
        return {x - c, 0, b + c - y};
    if (y <= 2 * b + c)
        return {x - c, y - b - c, 0};
    return {x - c, b, y - 2 * b - c};
}

int main() {
    ll a, b, c;
    char x1[TEXT], y1[TEXT], x2[TEXT], y2[TEXT];
    scanf("%lld %lld %lld %s %s %s %s", &a, &b, &c, x1, y1, x2, y2);
    a *= SCALE, b *= SCALE, c *= SCALE;
    Point p = fold(a, b, c, hundredths(x1), hundredths(y1));
    Point q = fold(a, b, c, hundredths(x2), hundredths(y2));
    ll dx = p.x - q.x, dy = p.y - q.y, dz = p.z - q.z;
    printf("%.10f\n", sqrt((double)(dx * dx + dy * dy + dz * dz)) / SCALE);
}
