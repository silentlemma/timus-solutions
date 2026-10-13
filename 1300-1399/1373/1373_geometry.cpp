#include <algorithm>
#include <climits>
#include <cstdio>

const int STROKE = 4; // numbers per stroke

int main() {
    long long lowX = LLONG_MAX, highX = LLONG_MIN, lowY = LLONG_MAX, highY = LLONG_MIN;
    long long ax = 0, ay = 0, bx = 0, by = 0;
    bool any = false;
    while (scanf("%lld %lld %lld %lld", &ax, &ay, &bx, &by) == STROKE) {
        long long dx = bx - ax, dy = by - ay;
        // go (p, q), then turn clockwise and go (q, -p): p + q = dx and
        // q - p = dy give the corner a + ((dx - dy) / 2, (dx + dy) / 2), and
        // doubled coordinates keep the halves whole
        long long xs[] = {2 * ax, 2 * bx, 2 * ax + dx - dy};
        long long ys[] = {2 * ay, 2 * by, 2 * ay + dx + dy};
        for (long long x : xs) {
            lowX = std::min(lowX, x);
            highX = std::max(highX, x);
        }
        for (long long y : ys) {
            lowY = std::min(lowY, y);
            highY = std::max(highY, y);
        }
        any = true;
    }
    if (!any)
        lowX = highX = lowY = highY = 0;
    printf("%.4f %.4f\n", (highX - lowX) / 2.0, (highY - lowY) / 2.0);
    return 0;
}
