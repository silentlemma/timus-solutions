#include <algorithm>
#include <cmath>
#include <cstdio>

const int CITIES = 3;
const double EPS = 1e-9;  // a tie at the edge gives the same cost either way

double x[CITIES], y[CITIES], w[CITIES];

double cost(double mx, double my) {
    double total = 0;
    for (int i = 0; i < CITIES; i++) total += w[i] * std::hypot(x[i] - mx, y[i] - my);
    return total;
}

double solve() {
    // a city is the best place when the pull of the others, the weighted
    // unit vectors towards them, is no stronger than the weight standing on
    // that very spot
    for (int v = 0; v < CITIES; v++) {
        double here = 0, px = 0, py = 0;
        for (int i = 0; i < CITIES; i++) {
            double d = std::hypot(x[i] - x[v], y[i] - y[v]);
            if (d == 0) {
                here += w[i];
            } else {
                px += w[i] * (x[i] - x[v]) / d;
                py += w[i] * (y[i] - y[v]) / d;
            }
        }
        if (std::hypot(px, py) <= here + EPS) return cost(x[v], y[v]);
    }
    // otherwise the best point is inside: by Ptolemy's inequality
    // w2 |MB| + w3 |MC| >= w1 |MQ| for the point Q beyond BC with
    // |BQ| : |CQ| : |BC| = w3 : w2 : w1, so the answer is w1 |AQ|
    double base = std::hypot(x[2] - x[1], y[2] - y[1]);
    double fromB = base * w[2] / w[0], fromC = base * w[1] / w[0];
    double along = (fromB * fromB - fromC * fromC + base * base) / (2 * base);
    double height = std::sqrt(std::max(0.0, fromB * fromB - along * along));
    double ex = (x[2] - x[1]) / base, ey = (y[2] - y[1]) / base, nx = -ey, ny = ex;
    // Q lies on the other side of BC from A
    if ((x[0] - x[1]) * nx + (y[0] - y[1]) * ny > 0) {
        nx = -nx;
        ny = -ny;
    }
    double qx = x[1] + along * ex + height * nx, qy = y[1] + along * ey + height * ny;
    return w[0] * std::hypot(x[0] - qx, y[0] - qy);
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        for (int i = 0; i < CITIES; i++) scanf("%lf %lf", &x[i], &y[i]);
        for (int i = 0; i < CITIES; i++) scanf("%lf", &w[i]);
        printf("%.10f\n", solve());
    }
    return 0;
}
