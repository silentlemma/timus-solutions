#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>

const int STEPS = 70;   // golden-section steps: the bracket shrinks by 0.618 each
const int SAMPLES = 24; // first look along circle B, before refining
const double GOLD = (std::sqrt(5.0) - 1) / 2;
const double PI = std::acos(-1.0);

// the least value of a function with one minimum on [lo, hi]
double golden(const std::function<double(double)> &f, double lo, double hi) {
    double a = hi - GOLD * (hi - lo), b = lo + GOLD * (hi - lo), fa = f(a), fb = f(b);
    for (int i = 0; i < STEPS; i++) {
        if (fa < fb) {
            hi = b, b = a, fb = fa;
            a = hi - GOLD * (hi - lo);
            fa = f(a);
        } else {
            lo = a, a = b, fa = fb;
            b = lo + GOLD * (hi - lo);
            fb = f(b);
        }
    }
    return std::min(fa, fb);
}

int main() {
    double r1, r2, r3, r;
    scanf("%lf %lf %lf %lf", &r1, &r2, &r3, &r);
    // a dog is fed from the house itself: then the tour goes to the other
    // dog's circle and back, and nothing shorter exists
    if (std::min(r1, r2) <= r) {
        printf("%.3f\n", 2 * std::max(std::max(r1, r2) - r, 0.0));
        return 0;
    }
    // posts at (0, 0) and (r3, 0), the house above them
    double hx = r3 > 0 ? (r1 * r1 - r2 * r2 + r3 * r3) / (2 * r3) : r1;
    double hy = std::sqrt(std::max(r1 * r1 - hx * hx, 0.0)), bx = r3;
    // the shortest way from P to the circle of dog B and on home
    auto toB = [&](double px, double py) {
        double dx = hx - px, dy = hy - py, length = std::hypot(dx, dy);
        double t =
            length > 0 ? std::clamp(((bx - px) * dx - py * dy) / (length * length), 0.0, 1.0) : 0.0;
        if (std::hypot(px + t * dx - bx, py + t * dy) <= r)
            return length;
        auto via = [&](double phi) {
            double qx = bx + r * std::cos(phi), qy = r * std::sin(phi);
            return std::hypot(qx - px, qy - py) + std::hypot(hx - qx, hy - qy);
        };
        double step = 2 * PI / SAMPLES;
        int best = 0;
        for (int k = 1; k < SAMPLES; k++)
            if (via(k * step) < via(best * step))
                best = k;
        return golden(via, (best - 1) * step, (best + 1) * step);
    };
    // the tour length is convex in P inside dog A's circle, so a golden
    // search over x of golden searches over y finds its least value
    auto column = [&](double px) {
        double half = std::sqrt(std::max(r * r - px * px, 0.0));
        return golden([&](double py) { return std::hypot(hx - px, hy - py) + toB(px, py); }, -half,
                      half);
    };
    printf("%.3f\n", golden(column, -r, r));
}
