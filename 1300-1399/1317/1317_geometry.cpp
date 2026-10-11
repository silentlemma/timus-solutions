#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const double EPS = 1e-9;
const int FIELDS = 3; // d and the place of the laser

struct Side {
    double nx, ny, c; // inside the lot nx x + ny y <= c
};

int main() {
    int n = 0;
    double h = 0;
    if (scanf("%d %lf", &n, &h) != 2)
        return 0;
    std::vector<double> xs(n), ys(n);
    for (int i = 0; i < n; i++) {
        if (scanf("%lf %lf", &xs[i], &ys[i]) != 2)
            return 0;
    }
    double d = 0, lx = 0, ly = 0;
    if (scanf("%lf %lf %lf", &d, &lx, &ly) != FIELDS)
        return 0;
    double area = 0;
    for (int i = 0; i < n; i++)
        area += xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i];
    if (area < 0) {
        std::reverse(xs.begin(), xs.end());
        std::reverse(ys.begin(), ys.end());
    }
    // each side as an outward normal and an offset
    std::vector<Side> sides;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        double nx = ys[j] - ys[i], ny = xs[i] - xs[j];
        sides.push_back({nx, ny, nx * xs[i] + ny * ys[i]});
    }
    int k = 0, shot = 0;
    if (scanf("%d", &k) != 1)
        return 0;
    for (int s = 0; s < k; s++) {
        double px = 0, py = 0;
        if (scanf("%lf %lf", &px, &py) != 2)
            return 0;
        double r = std::hypot(px - lx, py - ly);
        bool inside = true;
        for (const Side &e : sides) {
            if (e.nx * px + e.ny * py > e.c + EPS * std::hypot(e.nx, e.ny) * (r + 1))
                inside = false;
        }
        if (inside) {
            shot++; // over the lot the laser always reaches it in time
            continue;
        }
        // the beam leaves the lot at horizontal distance a and must clear
        // the fence there, so it meets the stone no lower than h r / a
        double ux = (px - lx) / r, uy = (py - ly) / r, a = INFINITY;
        for (const Side &e : sides) {
            double toward = e.nx * ux + e.ny * uy;
            if (toward > 0)
                a = std::min(a, (e.c - e.nx * lx - e.ny * ly) / toward);
        }
        if (r * r * (a * a + h * h) <= d * d * a * a * (1 + EPS))
            shot++;
    }
    printf("%d\n", shot);
    return 0;
}
