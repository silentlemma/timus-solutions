#include <algorithm>
#include <cmath>
#include <cstdio>

const int FIELDS = 7;

int main() {
    long long ax = 0, ay = 0, bx = 0, by = 0, cx = 0, cy = 0, rope = 0;
    if (scanf("%lld %lld %lld %lld %lld %lld %lld", &ax, &ay, &bx, &by, &cx, &cy, &rope) != FIELDS)
        return 0;
    long long dx = bx - ax, dy = by - ay, length = dx * dx + dy * dy;
    // the nearest point of the bed: C projected onto AB, kept inside it
    double t = 0;
    if (length != 0)
        t = std::max(0.0, std::min(1.0, double((cx - ax) * dx + (cy - ay) * dy) / length));
    double nearest = std::hypot(ax + t * dx - cx, ay + t * dy - cy);
    double farthest = std::max(std::hypot(double(ax - cx), double(ay - cy)),
                               std::hypot(double(bx - cx), double(by - cy)));
    printf("%.2f\n%.2f\n", std::max(0.0, nearest - rope), std::max(0.0, farthest - rope));
    return 0;
}
