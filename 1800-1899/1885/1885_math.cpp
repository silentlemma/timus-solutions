#include <algorithm>
#include <cstdio>

int main() {
    double h, t, v, x;
    if (scanf("%lf %lf %lf %lf", &h, &t, &v, &x) == EOF) return 0;
    // the least time climbs at x as long as possible and at full speed in
    // the remaining seconds; the most climbs just faster than x, or during
    // all t seconds when that is too slow to reach h
    double least = std::max(0.0, h - t * x) / (v - x);
    double most = std::min(t, h / x);
    printf("%.6f %.6f\n", least, most);
    return 0;
}
