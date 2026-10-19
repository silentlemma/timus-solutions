#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

const double PI = std::acos(-1.0);

// area common to discs of radii a and b with centres d apart
double lens(long long d, long long a, long long b) {
    if (d >= a + b) return 0.0;
    if (d <= std::llabs(a - b)) return PI * std::min(a, b) * std::min(a, b);
    // half-angles seen from each centre, by the law of cosines
    double alpha = std::acos(double(d * d + a * a - b * b) / (2.0 * d * a));
    double beta = std::acos(double(d * d + b * b - a * a) / (2.0 * d * b));
    // the kite between both centres and the two crossing points
    double kite =
        std::sqrt(double(-d + a + b) * (d + a - b) * (d - a + b) * (d + a + b)) / 2;
    return a * a * alpha + b * b * beta - kite;
}

int main() {
    long long d, r1, big1, r2, big2;
    if (scanf("%lld %lld %lld %lld %lld", &d, &r1, &big1, &r2, &big2) < 1) return 0;
    double ring1 = PI * (big1 * big1 - r1 * r1), ring2 = PI * (big2 * big2 - r2 * r2);
    // a ring is a disc minus a smaller one, so their overlap follows by
    // inclusion and exclusion over the four pairs of discs
    double common =
        lens(d, big1, big2) - lens(d, r1, big2) - lens(d, big1, r2) + lens(d, r1, r2);
    printf("%.6f\n", ring1 + ring2 - common);
    return 0;
}
