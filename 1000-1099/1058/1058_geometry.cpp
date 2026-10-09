#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

// samples per smooth piece and golden-section steps around the best samples
const int SAMPLES = 64, STEPS = 60;
const double EPS = 1e-12;

int n;
std::vector<double> vx, vy, pre;
double half;

struct Point {
    double x, y;
    int edge;
};

Point at(double u) {
    int i = (int)u;
    double t = u - i;
    return {vx[i] + t * (vx[i + 1] - vx[i]), vy[i] + t * (vy[i + 1] - vy[i]), i};
}

// the position w in (u, u + n) of the other end of the halving cut from u
double partner(double u) {
    Point p = at(u);
    int i = p.edge;
    // twice the area of P, V[i+1], ..., V[j]
    auto fan = [&](int j) {
        return p.x * vy[i + 1] - vx[i + 1] * p.y + pre[j] - pre[i + 1] + vx[j] * p.y - p.x * vy[j];
    };
    int lo = i + 1, hi = i + n;
    while (hi - lo > 1) {
        int mid = (lo + hi) / 2;
        if (fan(mid) <= half)
            lo = mid;
        else
            hi = mid;
    }
    int j = lo;
    // on the edge V[j] -> V[j+1] the area grows linearly with the position
    double ex = vx[j + 1] - vx[j], ey = vy[j + 1] - vy[j];
    double slope = vx[j] * ey - ex * vy[j] + ex * p.y - p.x * ey;
    double s = slope > 0 ? (half - fan(j)) / slope : 0;
    return j + std::min(std::max(s, 0.0), 1.0);
}

double length(double u) {
    Point p = at(u), q = at(partner(u));
    return std::hypot(q.x - p.x, q.y - p.y);
}

int main() {
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<double> xs(n), ys(n);
    for (int i = 0; i < n; i++)
        if (scanf("%lf %lf", &xs[i], &ys[i]) != 2)
            return 0;
    // the walk below needs counterclockwise order, whatever order is given
    double twice = 0;
    for (int i = 0; i < n; i++)
        twice += xs[(i + n - 1) % n] * ys[i] - xs[i] * ys[(i + n - 1) % n];
    if (twice < 0) {
        std::reverse(xs.begin(), xs.end());
        std::reverse(ys.begin(), ys.end());
    }
    // vertices repeated twice so that a walk along the boundary never wraps
    for (int k = 0; k <= 2 * n; k++) {
        vx.push_back(xs[k % n]);
        vy.push_back(ys[k % n]);
    }
    // pre[k]: twice the signed area swept by the edges 0 .. k-1 from the origin
    pre.push_back(0);
    for (int k = 0; k < 2 * n; k++)
        pre.push_back(pre.back() + vx[k] * vy[k + 1] - vx[k + 1] * vy[k]);
    half = pre[n] / 2;
    // the cut length is smooth between the vertices and the partners of the
    // vertices; sample every piece and refine around its local minima
    std::vector<double> breaks;
    for (int k = 0; k <= n; k++) {
        breaks.push_back(k);
        if (k < n)
            breaks.push_back(std::fmod(partner(k), n));
    }
    std::sort(breaks.begin(), breaks.end());
    const double golden = (std::sqrt(5.0) - 1) / 2;
    double best = length(0);
    for (size_t b = 0; b + 1 < breaks.size(); b++) {
        double from = breaks[b], to = breaks[b + 1];
        if (to - from < EPS)
            continue;
        std::vector<double> us(SAMPLES + 1), vals(SAMPLES + 1);
        for (int k = 0; k <= SAMPLES; k++) {
            us[k] = from + (to - from) * k / SAMPLES;
            vals[k] = length(us[k]);
            best = std::min(best, vals[k]);
        }
        for (int k = 0; k <= SAMPLES; k++) {
            // a local minimum among the samples, the piece ends included
            int left = std::max(k - 1, 0), right = std::min(k + 1, SAMPLES);
            if (vals[k] > vals[left] || vals[k] > vals[right])
                continue;
            double lo = us[left], hi = us[right];
            for (int step = 0; step < STEPS; step++) {
                double m1 = hi - golden * (hi - lo), m2 = lo + golden * (hi - lo);
                if (length(m1) < length(m2))
                    hi = m2;
                else
                    lo = m1;
            }
            best = std::min(best, length((lo + hi) / 2));
        }
    }
    printf("%.6f\n", best);
}
