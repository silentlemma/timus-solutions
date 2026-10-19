#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

// the length of the trace while the source a and the receiver b move along
// the directions ua and ub for the time span
static double stretch(double ax, double ay, double bx, double by, double uax, double uay,
                      double ubx, double uby, double span) {
    double dx = bx - ax, dy = by - ay, vx = ubx - uax, vy = uby - uay;
    double a = vx * vx + vy * vy;
    double m = dx * vy - dy * vx;  // constant cross product of d(t) = b - a and v
    if (a == 0 || m <= 0) return 0;
    // the trace point is a + lam(t) d(t), lam linear; its speed is
    // |r(t)| / sqrt(q(t)) for q(t) = |d(t)|^2 and a quadratic r(t)
    double lam0 = (uax * dy - uay * dx) / m, lam1 = (uax * vy - uay * vx) / m;
    double h = dx * vx + dy * vy, c = dx * dx + dy * dy, b = 2 * h;
    double r2 = 2 * lam1 * a;
    double r1 = uax * vx + uay * vy + lam1 * (b + h) + lam0 * a;
    double r0 = uax * dx + uay * dy + lam1 * c + lam0 * h;
    // r = alpha q + beta q' + gamma, integrated term by term
    double alpha = 2 * lam1, beta = (r1 - alpha * b) / (2 * a), gamma = r0 - alpha * c - beta * b;
    double rootA = std::sqrt(a), tail = alpha * m * m / (2 * a) + gamma;
    auto primitive = [&](double t) {
        double q = std::max(a * t * t + b * t + c, 0.0), slope = 2 * a * t + b;
        return (lam1 * slope / (2 * a) + 2 * beta) * std::sqrt(q) +
               tail * std::asinh(slope / (2 * m)) / rootA;
    };
    // the speed changes sign at the roots of r: the trace has a cusp there
    std::vector<double> roots, cuts = {0};
    if (r2 != 0) {
        double half = r1 / 2, disc = half * half - r2 * r0;
        if (disc > 0) {
            double s = std::sqrt(disc);
            roots = {(-half - s) / r2, (-half + s) / r2};
            std::sort(roots.begin(), roots.end());
        }
    } else if (r1 != 0) {
        roots = {-r0 / r1};
    }
    for (double t : roots) {
        if (t > 0 && t < span) cuts.push_back(t);
    }
    cuts.push_back(span);
    double total = 0;
    for (size_t k = 0; k + 1 < cuts.size(); k++) {
        double lo = cuts[k], hi = cuts[k + 1], mid = (lo + hi) / 2;
        double part = primitive(hi) - primitive(lo);
        total += r2 * mid * mid + r1 * mid + r0 >= 0 ? part : -part;
    }
    return total;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<double> xs(n), ys(n), size(n), ux(n), uy(n);
    for (int i = 0; i < n; i++) scanf("%lf %lf", &xs[i], &ys[i]);
    double d;
    scanf("%lf", &d);
    for (int i = 0; i < n; i++) {
        int k = (i + 1) % n;
        size[i] = std::hypot(xs[k] - xs[i], ys[k] - ys[i]);
        ux[i] = (xs[k] - xs[i]) / size[i];
        uy[i] = (ys[k] - ys[i]) / size[i];
    }
    // the source starts at vertex 0; the receiver d further along the border
    int j = 0;
    double left = d;
    while (left >= size[j]) left -= size[j++];
    double bx = xs[j] + ux[j] * left, by = ys[j] + uy[j] * left;
    double ahead = size[j] - left;  // what is left of the receiver's edge
    int i = 0;
    double ax = xs[0], ay = ys[0], behind = size[0], total = 0;
    // walk from one corner event to the next, one of the two at a vertex
    while (i < n) {
        double span = std::min(behind, ahead);
        total += stretch(ax, ay, bx, by, ux[i], uy[i], ux[j], uy[j], span);
        if (behind <= ahead) {
            ahead -= behind;
            bx += ux[j] * behind;
            by += uy[j] * behind;
            if (++i < n) {
                ax = xs[i];
                ay = ys[i];
                behind = size[i];
            }
            if (ahead <= 0) {
                j = (j + 1) % n;
                bx = xs[j];
                by = ys[j];
                ahead = size[j];
            }
        } else {
            behind -= ahead;
            ax += ux[i] * ahead;
            ay += uy[i] * ahead;
            j = (j + 1) % n;
            bx = xs[j];
            by = ys[j];
            ahead = size[j];
        }
    }
    printf("%.10f\n", total);
    return 0;
}
