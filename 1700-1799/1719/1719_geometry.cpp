#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const int BOSSES = 4;
// the three ways to split the four bosses into two shots
const int SPLITS[3][2][2] = {{{0, 1}, {2, 3}}, {{0, 2}, {1, 3}}, {{0, 3}, {1, 2}}};

double x[BOSSES], y[BOSSES];

// walk from the origin to a point P on the line a1 b1, shoot, then walk
// straight to the line a2 b2; along the first line P = a1 + t u and the
// length is sqrt((t - t0)^2 + h^2) + |k t + m|, convex in t
double walk(int a1, int b1, int a2, int b2) {
    double length = std::hypot(x[b1] - x[a1], y[b1] - y[a1]);
    double ux = (x[b1] - x[a1]) / length, uy = (y[b1] - y[a1]) / length;
    double t0 = -(x[a1] * ux + y[a1] * uy);
    double h = std::fabs(x[a1] * uy - y[a1] * ux);
    double norm = std::hypot(x[b2] - x[a2], y[b2] - y[a2]);
    double nx = -(y[b2] - y[a2]) / norm, ny = (x[b2] - x[a2]) / norm;
    double k = nx * ux + ny * uy;
    double m = nx * (x[a1] - x[a2]) + ny * (y[a1] - y[a2]);
    // the minimum is at the foot of the origin, where the lines cross, or
    // where the slope of the first term cancels the slope k of the second
    std::vector<double> candidates = {t0};
    if (k != 0) {
        candidates.push_back(-m / k);
    }
    if (std::fabs(k) < 1) {
        double shift = k * h / std::sqrt(1 - k * k);
        candidates.push_back(t0 + shift);
        candidates.push_back(t0 - shift);
    }
    double best = HUGE_VAL;
    for (double t : candidates) {
        best = std::min(best, std::hypot(t - t0, h) + std::fabs(k * t + m));
    }
    return best;
}

int main() {
    for (int i = 0; i < BOSSES; i++) {
        scanf("%lf %lf", &x[i], &y[i]);
    }
    double best = HUGE_VAL;
    for (const auto& s : SPLITS) {
        const int *p = s[0], *q = s[1];
        best = std::min({best, walk(p[0], p[1], q[0], q[1]), walk(q[0], q[1], p[0], p[1])});
    }
    printf("%.10f\n", best);
}
