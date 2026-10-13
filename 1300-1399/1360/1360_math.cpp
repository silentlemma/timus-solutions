#include <algorithm>
#include <cmath>
#include <cstdio>

const double TURN = 2 * std::acos(-1.0);
const int FIELDS = 3;

int main() {
    double x0 = 0, y0 = 0, eps = 0;
    if (scanf("%lf %lf %lf", &x0, &y0, &eps) != FIELDS)
        return 0;
    double across = std::asin(std::max(-1.0, std::min(1.0, x0)));
    double up = std::acos(std::max(-1.0, std::min(1.0, y0)));
    // take sqrt(t) = s0 with sin(s0) = x0 and s0 > 2 pi / eps; within pi of
    // t0 = s0^2 some t has cos(t) = y0, and sqrt(t) moves by less than eps / 4
    double s0 = across + TURN * (std::ceil(1 / eps) + 1);
    double t0 = s0 * s0;
    double t = up + TURN * std::round((t0 - up) / TURN);
    printf("%.6f\n", t);
    return 0;
}
