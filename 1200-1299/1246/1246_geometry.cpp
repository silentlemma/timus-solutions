#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    // twice the signed area by the shoelace formula: positive when the
    // runner goes counterclockwise, and the rope winds the same way
    long long x0, y0, px, py, twice = 0;
    scanf("%lld %lld", &x0, &y0);
    px = x0, py = y0;
    for (int i = 1; i < n; i++) {
        long long x, y;
        scanf("%lld %lld", &x, &y);
        twice += px * y - x * py;
        px = x, py = y;
    }
    twice += px * y0 - x0 * py;
    puts(twice > 0 ? "ccw" : "cw");
}
