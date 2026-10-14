#include <cmath>
#include <cstdio>
#include <iostream>

const double NODE = sqrt(0.6); // the outer nodes of three-point Gauss-Legendre on [-1, 1]
const double OUTER = 5, MIDDLE = 8, TOTAL = 9; // its weights, as 5/9 and 8/9
const double TOLERANCE = 1e-13;
const int DEPTH = 50;
const double LIMIT = 20; // sinh(20) is about 2.4e8, beyond which the tails are negligible

double a0, a1, a2, a3, a4;

// x = sinh t, dx = cosh t dt: the infinite line becomes a finite range
double f(double t) {
    double x = sinh(t);
    return cosh(t) / ((((a4 * x + a3) * x + a2) * x + a1) * x + a0);
}

double gauss(double lo, double hi) {
    double mid = (lo + hi) / 2, half = (hi - lo) / 2;
    return half * (OUTER * f(mid - half * NODE) + MIDDLE * f(mid) + OUTER * f(mid + half * NODE)) /
           TOTAL;
}

// adaptive: split while the halves disagree with the whole
double integrate(double lo, double hi, double whole, int depth) {
    double mid = (lo + hi) / 2;
    double left = gauss(lo, mid), right = gauss(mid, hi), both = left + right;
    if (depth == 0 || fabs(both - whole) <= TOLERANCE * (1 + fabs(both)))
        return both;
    return integrate(lo, mid, left, depth - 1) + integrate(mid, hi, right, depth - 1);
}

int main() {
    if (!(std::cin >> a0 >> a1 >> a2 >> a3 >> a4))
        return 0;
    printf("%.10f\n", integrate(-LIMIT, LIMIT, gauss(-LIMIT, LIMIT), DEPTH));
}
