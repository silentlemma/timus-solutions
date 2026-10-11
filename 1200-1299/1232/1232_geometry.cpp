#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const double EPS = 1e-9;

struct Point {
    double x, z;
};

double h, d, tg, sn, cs;

// the smallest drop of one move from a point on the cone wall at depth t
// below the station: the move goes across to the opposite wall, or is
// almost level once the cone there is at least d wide
double minDrop(double t) {
    double w = 2 * t * tg;
    if (w >= d)
        return 0;
    return (std::sqrt(d * d * (1 + tg * tg) - w * w) - w * tg) / (1 + tg * tg);
}

// n moves in the plane y = 0: first slides moves down the wall, then
// crossings of the cone at full tilt, and as soon as one move can drop
// exactly the extra height, that move and then straight down
bool path(int n, int slides, std::vector<Point> &pts) {
    pts.clear();
    double t = 0, x = 0, side = 1;
    for (int left = n; left >= 1; left--) {
        double extra = h - t - (left - 1) * d;
        double drop = minDrop(t);
        if (extra >= drop - EPS) {
            x += side * std::sqrt(std::max(0.0, d * d - extra * extra));
            t += extra;
            pts.push_back({x, h - t});
            for (int k = left - 1; k >= 1; k--)
                pts.push_back({x, (k - 1) * d});
            pts.back().z = 0;
            return true;
        }
        if (left == 1)
            return false;
        if (n - left < slides) {
            x -= side * d * sn;
            t += d * cs;
        } else {
            t += drop;
            x = side * t * tg;
            side = -side;
        }
        pts.push_back({x, h - t});
    }
    return false;
}

int main() {
    double alpha;
    scanf("%lf %lf %lf", &h, &d, &alpha);
    tg = std::tan(alpha / 2), sn = std::sin(alpha / 2), cs = std::cos(alpha / 2);
    int n = (int)std::ceil(h / d - EPS);
    std::vector<Point> pts;
    for (int slides = 0; slides <= n; slides++) {
        if (path(n, slides, pts)) {
            printf("%d\n", n);
            for (const Point &p : pts)
                printf("%.6f 0 %.6f\n", p.x, p.z);
            return 0;
        }
    }
    printf("-1\n");
}
