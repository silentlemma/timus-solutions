#include <cmath>
#include <cstdio>

constexpr int INPUT_FIELDS = 7;

int main() {
    long long ax, ay, bx, by, cx, cy;
    double rope;
    if (scanf("%lld%lld%lld%lld%lld%lld%lf", &ax, &ay, &bx, &by, &cx, &cy, &rope) != INPUT_FIELDS)
        return 0;
    const long long dx = bx - ax, dy = by - ay;
    const long long square = dx * dx + dy * dy;
    double t = square == 0 ? 0 : double((cx - ax) * dx + (cy - ay) * dy) / square;
    if (t < 0)
        t = 0;
    if (t > 1)
        t = 1;
    const double nearest = std::hypot(ax + t * dx - cx, ay + t * dy - cy);
    const double a = std::hypot(double(ax - cx), double(ay - cy));
    const double b = std::hypot(double(bx - cx), double(by - cy));
    const double farthest = a > b ? a : b;
    printf("%.2f\n%.2f\n", nearest > rope ? nearest - rope : 0,
           farthest > rope ? farthest - rope : 0);
}
