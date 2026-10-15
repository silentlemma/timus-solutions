#include <cstdio>

typedef long long ll;

// whether one side of some inscribed square passes through both points:
// a side lies on a line at distance R / sqrt(2) from the centre, and the
// disc cuts exactly the side out of that line
bool sameSide(ll r, ll x1, ll y1, ll x2, ll y2) {
    if (x1 == x2 && y1 == y2) {
        return 2 * (x1 * x1 + y1 * y1) >= r * r;
    }
    ll cross = x1 * y2 - y1 * x2;
    ll dx = x1 - x2, dy = y1 - y2;
    return 2 * cross * cross == r * r * (dx * dx + dy * dy);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        ll r, x1, y1, x2, y2;
        scanf("%lld %lld %lld %lld %lld", &r, &x1, &y1, &x2, &y2);
        // the second point on the same, the opposite or an adjacent side:
        // turning it by 0, 180, 90 or -90 degrees brings it onto the first one's side
        bool ok = sameSide(r, x1, y1, x2, y2) || sameSide(r, x1, y1, -x2, -y2) ||
                  sameSide(r, x1, y1, -y2, x2) || sameSide(r, x1, y1, y2, -x2);
        puts(ok ? "YES" : "NO");
    }
}
