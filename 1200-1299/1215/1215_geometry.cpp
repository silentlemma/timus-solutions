#include <cmath>
#include <cstdio>
#include <vector>

static double segmentDistance(double px, double py, double ax, double ay, double bx, double by) {
    double dx = bx - ax, dy = by - ay;
    double t = (px - ax) * dx + (py - ay) * dy, length2 = dx * dx + dy * dy;
    if (t <= 0) {
        return std::hypot(px - ax, py - ay);
    }
    if (t >= length2) {
        return std::hypot(px - bx, py - by);
    }
    return std::fabs((px - ax) * dy - (py - ay) * dx) / std::sqrt(length2);
}

int main() {
    long long px, py;
    int n;
    scanf("%lld %lld %d", &px, &py, &n);
    std::vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &x[i], &y[i]);
    }
    bool inside = true;
    double best = INFINITY;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        // inside a counterclockwise polygon the point is left of every edge
        if ((x[j] - x[i]) * (py - y[i]) - (y[j] - y[i]) * (px - x[i]) < 0) {
            inside = false;
        }
        best = std::fmin(best, segmentDistance(px, py, x[i], y[i], x[j], y[j]));
    }
    printf("%.3f\n", inside ? 0.0 : 2 * best);
}
