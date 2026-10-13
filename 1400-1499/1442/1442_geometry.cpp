#include <cmath>
#include <cstdio>

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int DEPTH = 50;
const double CONE = 1.0 / 3;                          // a cone holds a third of its cylinder
const double SIMPSON[] = {1.0 / 6, 4.0 / 6, 1.0 / 6}; // weights of the ends and the middle
const double RICHARDSON = 15; // error estimate of the Simpson rule on halves

double r, d, h, k;

// the powder lost in the slice at x, parallel to the slit x = d: the cone
// surface k (r - rho) drops to k |x - d| wherever rho < a = r - |x - d|
double lost(double x) {
    double a = r - fabs(x - d);
    if (a <= fabs(x))
        return 0;
    double y = sqrt(a * a - x * x);
    double tail = x != 0 ? x * x * log((a + y) / fabs(x)) : 0;
    return k * (a * y - tail);
}

double rule(double lo, double hi, double flo, double fmid, double fhi) {
    return (hi - lo) * (SIMPSON[0] * flo + SIMPSON[1] * fmid + SIMPSON[2] * fhi);
}

double adaptive(double lo, double hi, double flo, double fmid, double fhi, double whole, double eps,
                int depth) {
    double mid = (lo + hi) / 2;
    double fl = lost((lo + mid) / 2), fr = lost((mid + hi) / 2);
    double left = rule(lo, mid, flo, fl, fmid), right = rule(mid, hi, fmid, fr, fhi);
    double delta = left + right - whole;
    if (depth == 0 || fabs(delta) <= RICHARDSON * eps)
        return left + right + delta / RICHARDSON;
    return adaptive(lo, mid, flo, fl, fmid, left, eps / 2, depth - 1) +
           adaptive(mid, hi, fmid, fr, fhi, right, eps / 2, depth - 1);
}

double integral(double lo, double hi) {
    if (hi <= lo)
        return 0;
    double flo = lost(lo), fmid = lost((lo + hi) / 2), fhi = lost(hi);
    return adaptive(lo, hi, flo, fmid, fhi, rule(lo, hi, flo, fmid, fhi), EPS, DEPTH);
}

int main() {
    scanf("%lf %lf %lf", &r, &d, &h);
    k = h / r; // the slope of the powder
    double volume = PI * r * r * h * CONE;
    if (d < r) // the slit cuts the base between (d - r) / 2 and (d + r) / 2, kinks at 0 and d
        volume -= integral((d - r) / 2, 0) + integral(0, d) + integral(d, (d + r) / 2);
    printf("%.6f\n", volume);
}
