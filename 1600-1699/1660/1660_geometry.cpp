#include <algorithm>
#include <cmath>
#include <cstdio>

const double SLACK = 1e-9;  // lets a chain that closes exactly keep its last circle
const double PI = acos(-1.0);

struct Circle {
    double x, y, r;
};

// the image under inversion in the unit circle around the origin
Circle invert(Circle c) {
    double den = c.x * c.x + c.y * c.y - c.r * c.r;
    return {c.x / den, c.y / den, c.r / fabs(den)};
}

int main() {
    int big, small, d;
    scanf("%d %d %d", &big, &small, &d);
    // the limit point inside the small circle (the common centre if d = 0):
    // inverting there makes both circles concentric
    double b = (double)big * big + (double)d * d - (double)small * small;
    double twice = 2.0 * d * big;
    double p = twice * big / (b + sqrt(std::max(0.0, b * b - twice * twice)));
    Circle outer = invert({-p, 0, (double)big});
    Circle inner = invert({d - p, 0, (double)small});
    double centre = (outer.x + inner.x) / 2;
    double mid = (outer.r + inner.r) / 2;
    double half = fabs(outer.r - inner.r) / 2;
    // there every chain circle has radius half and turns by step around the
    // centre; the chain stops once one more would overlap the first
    double step = 2 * asin(half / mid);
    int count = (int)(2 * PI / step + SLACK);
    double span = (count - 1) * step;
    auto gap = [&](double theta) {
        Circle a = invert({centre + mid * cos(theta), mid * sin(theta), half});
        Circle z = invert({centre + mid * cos(theta + span), mid * sin(theta + span), half});
        return hypot(a.x - z.x, a.y - z.y) - a.r - z.r;
    };
    // the best chain is symmetric about the line through the centres
    double best = std::min(gap(-span / 2), gap(PI - span / 2));
    printf("%.10f\n", std::max(0.0, best));
}
