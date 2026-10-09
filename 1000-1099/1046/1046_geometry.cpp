#include <cmath>
#include <complex>
#include <cstdio>
#include <vector>

typedef std::complex<double> point;

const double HALF_TURN = 180, ROUNDING = 0.005;

// a value that prints as -0.00 is printed as 0.00
double clean(double v) { return std::fabs(v) < ROUNDING ? 0 : v; }

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<point> apex(n), turn(n);
    for (auto &m : apex) {
        double x, y;
        if (scanf("%lf %lf", &x, &y) != 2)
            return 0;
        m = point(x, y);
    }
    const double pi = std::acos(-1.0);
    for (auto &w : turn) {
        double degrees;
        if (scanf("%lf", &degrees) != 1)
            return 0;
        w = std::polar(1.0, degrees * pi / HALF_TURN);
    }
    // a step turns z around M[i] by its angle, z -> w z + (1 - w) M[i], and going
    // around the polygon composes the steps into z -> a z + b that fixes A[0]
    point a = 1, b = 0;
    for (int i = 0; i < n; i++) {
        a = turn[i] * a;
        b = turn[i] * b + (1.0 - turn[i]) * apex[i];
    }
    // the angles never add up to a multiple of 360, so a != 1
    point z = b / (1.0 - a);
    for (int i = 0; i < n; i++) {
        printf("%.2f %.2f\n", clean(z.real()), clean(z.imag()));
        z = apex[i] + turn[i] * (z - apex[i]);
    }
}
