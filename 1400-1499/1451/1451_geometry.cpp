#include <cmath>
#include <cstdio>

const int CORNERS = 3;
const double PI = acos(-1.0);
const double WIDE = 2 * PI / 3; // 120 degrees

int main() {
    double x[CORNERS], y[CORNERS], angle[CORNERS], side[CORNERS];
    for (int i = 0; i < CORNERS; i++)
        scanf("%lf %lf", &x[i], &y[i]);
    for (int i = 0; i < CORNERS; i++) {
        int b = (i + 1) % CORNERS, c = (i + 2) % CORNERS;
        double ux = x[b] - x[i], uy = y[b] - y[i], wx = x[c] - x[i], wy = y[c] - y[i];
        angle[i] = atan2(fabs(ux * wy - uy * wx), ux * wx + uy * wy);
        side[i] = hypot(x[c] - x[b], y[c] - y[b]);
    }
    for (int i = 0; i < CORNERS; i++)
        if (angle[i] >= WIDE) {
            // a corner of at least 120 degrees is the best place itself
            printf("%.8f %.8f\n", x[i], y[i]);
            return 0;
        }
    // otherwise the Fermat point: every side is seen at 120 degrees, and its
    // barycentric weights are a / sin(A + 60 degrees) and so on
    double total = 0, fx = 0, fy = 0;
    for (int i = 0; i < CORNERS; i++) {
        double w = side[i] / sin(angle[i] + PI / CORNERS);
        total += w;
        fx += w * x[i];
        fy += w * y[i];
    }
    printf("%.8f %.8f\n", fx / total, fy / total);
}
