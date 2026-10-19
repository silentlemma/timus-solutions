#include <cstdio>

typedef long long ll;
typedef __int128 big;  // the mixed product reaches 5 * 10^19
constexpr int DIM = 3;

struct Vec {
    ll x, y, z;
};

Vec sub(Vec u, Vec v) { return {u.x - v.x, u.y - v.y, u.z - v.z}; }
ll dot(Vec u, Vec v) { return u.x * v.x + u.y * v.y + u.z * v.z; }
Vec cross(Vec u, Vec v) {
    return {u.y * v.z - u.z * v.y, u.z * v.x - u.x * v.z, u.x * v.y - u.y * v.x};
}
big bigDot(Vec u, Vec v) { return (big)u.x * v.x + (big)u.y * v.y + (big)u.z * v.z; }

int main() {
    Vec p[DIM + 1];
    for (Vec& q : p) scanf("%lld %lld %lld", &q.x, &q.y, &q.z);
    Vec ab = sub(p[1], p[0]), cd = sub(p[DIM], p[2]), ac = sub(p[2], p[0]);
    // the turn is a right angle, the two lines meet, the turning point
    // P = A + t AB with t = (AC . AB) / |AB|^2 is not before B, and C is not
    // before P on the second line, (C - P) . CD = AC . CD >= 0
    bool ok = dot(ab, cd) == 0 && bigDot(ac, cross(ab, cd)) == 0 && dot(ac, ab) >= dot(ab, ab) &&
              dot(ac, cd) >= 0;
    puts(ok ? "Valid" : "Invalid");
}
