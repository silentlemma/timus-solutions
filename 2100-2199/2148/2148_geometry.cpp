#include <cmath>
#include <cstdio>

int main() {
    long long cx, cy, r, ax, ay, bx, by;
    scanf("%lld %lld %lld %lld %lld %lld %lld", &cx, &cy, &r, &ax, &ay, &bx, &by);
    // The players are equally far from the centre, so the mirror point lies on
    // the bisector of the angle between them, in the direction w = A + B - 2C.
    long long wx = ax + bx - 2 * cx, wy = ay + by - 2 * cy;
    // Both shots stay outside the tank exactly when each player is strictly
    // beyond the tangent line at that point: (A - C) . w > r |w|.
    long long dot = (ax - cx) * wx + (ay - cy) * wy;
    long long norm = wx * wx + wy * wy;
    if (dot <= 0 || dot * dot <= r * r * norm) {
        puts("No way");
        return 0;
    }
    double scale = r / std::sqrt((double)norm);
    printf("%.9f %.9f\n", cx + wx * scale, cy + wy * scale);
    return 0;
}
