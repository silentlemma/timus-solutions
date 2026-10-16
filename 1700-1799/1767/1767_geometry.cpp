#include <algorithm>
#include <cstdio>

typedef long long ll;

int sign(ll v) { return (v > 0) - (v < 0); }

// the length of the overlap of the ranges between p and q and between r and
// s, negative when they are apart
ll overlap(ll p, ll q, ll r, ll s) {
    return std::min(std::max(p, q), std::max(r, s)) - std::max(std::min(p, q), std::min(r, s));
}

int main() {
    ll ax, ay, bx, by, cx, cy, dx, dy;
    if (scanf("%lld %lld %lld %lld", &ax, &ay, &bx, &by) < 1) return 0;
    if (scanf("%lld %lld %lld %lld", &cx, &cy, &dx, &dy) < 1) return 0;
    // both walks stay in the boxes of their ends, so the shared part lies in
    // the overlap of the two boxes
    ll width = overlap(ax, bx, cx, dx), height = overlap(ay, by, cy, dy);
    if (width < 0 || height < 0) {
        printf("0\n");
        return 0;
    }
    // walks rising the same way can share a staircase across the overlap, while
    // one rising and one falling share only one straight piece
    int first = sign(bx - ax) * sign(by - ay), second = sign(dx - cx) * sign(dy - cy);
    printf("%lld\n", first * second < 0 ? std::max(width, height) : width + height);
    return 0;
}
