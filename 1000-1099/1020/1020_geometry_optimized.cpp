#include <cmath>
#include <cstdio>

const double PI = std::acos(-1.0);

int main() {
    int n;
    double r, firstX, firstY;
    if (scanf("%d %lf", &n, &r) != 2 || scanf("%lf %lf", &firstX, &firstY) != 2)
        return 1;
    // the straight parts are the sides of the polygon, the arcs around the
    // nails turn by 2*pi in total: one full circle of radius r
    double length = 2 * PI * r;
    // the polygon is walked while reading, so the nails are never stored
    double previousX = firstX, previousY = firstY;
    for (int i = 1; i < n; ++i) {
        double x, y;
        if (scanf("%lf %lf", &x, &y) != 2)
            return 1;
        length += std::hypot(x - previousX, y - previousY);
        previousX = x;
        previousY = y;
    }
    length += std::hypot(firstX - previousX, firstY - previousY);
    printf("%.2f\n", length);
}
