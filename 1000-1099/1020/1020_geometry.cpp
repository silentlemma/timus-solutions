#include <cmath>
#include <cstdio>
#include <vector>

const double PI = std::acos(-1.0);

int main() {
    int n;
    double r;
    if (scanf("%d %lf", &n, &r) != 2)
        return 1;
    std::vector<double> x(n), y(n);
    for (int i = 0; i < n; i++)
        if (scanf("%lf %lf", &x[i], &y[i]) != 2)
            return 1;
    // the straight parts are the sides of the polygon, the arcs around the
    // nails turn by 2*pi in total: one full circle of radius r
    double length = 2 * PI * r;
    for (int i = 0; n > 1 && i < n; i++)
        length += std::hypot(x[(i + 1) % n] - x[i], y[(i + 1) % n] - y[i]);
    printf("%.2f\n", length);
}
