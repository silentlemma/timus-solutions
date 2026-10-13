#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

const double EPS = 1e-9;

struct Line {
    double a, b, c; // a x + b y + c, positive inside
};

struct Point {
    double x, y;
};

int n;
vector<Point> pts;

// distance from an inner point to the fence, or -1 outside
double distanceToFence(double px, double py) {
    bool inside = false;
    double best = HUGE_VAL;
    for (int i = 0; i < n; i++) {
        Point p = pts[i], q = pts[(i + 1) % n];
        if ((p.y > py) != (q.y > py) && px < p.x + (py - p.y) * (q.x - p.x) / (q.y - p.y))
            inside = !inside;
        double dx = q.x - p.x, dy = q.y - p.y;
        double t = ((px - p.x) * dx + (py - p.y) * dy) / (dx * dx + dy * dy);
        t = max(0.0, min(1.0, t));
        best = min(best, hypot(px - p.x - t * dx, py - p.y - t * dy));
    }
    return inside ? best : -1;
}

// points o + t u whose distance to v equals base + slope t
void onCircle(Point o, Point u, double base, double slope, Point v, vector<Point> &out) {
    // |o + t u - v|^2 = (base + slope t)^2, or qa t^2 + 2 hb t + qc = 0
    double wx = o.x - v.x, wy = o.y - v.y;
    double qa = u.x * u.x + u.y * u.y - slope * slope;
    double hb = wx * u.x + wy * u.y - base * slope;
    double qc = wx * wx + wy * wy - base * base;
    double disc = hb * hb - qa * qc;
    if (disc < -EPS * (hb * hb + fabs(qa * qc)))
        return;
    // the stable form of the roots, also when qa is next to zero
    double q = -(hb + copysign(sqrt(max(0.0, disc)), hb));
    if (fabs(qa) > EPS)
        out.push_back({o.x + q / qa * u.x, o.y + q / qa * u.y});
    if (fabs(q) > EPS)
        out.push_back({o.x + qc / q * u.x, o.y + qc / q * u.y});
}

int main() {
    scanf("%d", &n);
    pts.resize(n);
    for (auto &p : pts)
        scanf("%lf %lf", &p.x, &p.y);
    vector<Line> lines;
    for (int i = 0; i < n; i++) {
        Point p = pts[i], q = pts[(i + 1) % n];
        double length = hypot(q.x - p.x, q.y - p.y);
        double a = -(q.y - p.y) / length, b = (q.x - p.x) / length;
        lines.push_back({a, b, -(a * p.x + b * p.y)});
    }
    // only reflex vertices can be the nearest point of the fence from inside
    vector<Point> reflex;
    for (int i = 0; i < n; i++) {
        Point p = pts[(i + n - 1) % n], q = pts[i], r = pts[(i + 1) % n];
        if ((q.x - p.x) * (r.y - q.y) - (q.y - p.y) * (r.x - q.x) < 0)
            reflex.push_back(q);
    }
    int m = lines.size(), k = reflex.size();
    vector<Point> cand;
    // three lines: a_i x + b_i y + c_i = r for all three, by Cramer's rule
    for (int i = 0; i < m; i++)
        for (int j = i + 1; j < m; j++)
            for (int l = j + 1; l < m; l++) {
                Line p = lines[i], q = lines[j], s = lines[l];
                double det = p.a * (q.b - s.b) - p.b * (q.a - s.a) + (q.a * s.b - s.a * q.b);
                if (fabs(det) < EPS)
                    continue;
                double rx = -p.c * (q.b - s.b) - p.b * (s.c - q.c) + (s.c * q.b - q.c * s.b);
                double ry = p.a * (s.c - q.c) + p.c * (q.a - s.a) + (s.a * q.c - q.a * s.c);
                cand.push_back({rx / det, ry / det});
            }
    // two lines and a reflex vertex: on the bisector, as far from the vertex
    for (int i = 0; i < m; i++)
        for (int j = i + 1; j < m; j++) {
            Line p = lines[i], q = lines[j];
            double da = p.a - q.a, db = p.b - q.b, dc = p.c - q.c;
            double norm = da * da + db * db;
            if (norm < EPS)
                continue;
            Point o = {-dc * da / norm, -dc * db / norm}, u = {-db, da};
            for (Point v : reflex)
                onCircle(o, u, p.a * o.x + p.b * o.y + p.c, p.a * u.x + p.b * u.y, v, cand);
        }
    // a line and two reflex vertices: on their perpendicular bisector
    for (int i = 0; i < k; i++)
        for (int j = i + 1; j < k; j++) {
            Point v = reflex[i], w = reflex[j];
            Point o = {(v.x + w.x) / 2, (v.y + w.y) / 2}, u = {-(w.y - v.y), w.x - v.x};
            for (Line p : lines)
                onCircle(o, u, p.a * o.x + p.b * o.y + p.c, p.a * u.x + p.b * u.y, v, cand);
        }
    // three reflex vertices: the centre of their circle
    for (int i = 0; i < k; i++)
        for (int j = i + 1; j < k; j++)
            for (int l = j + 1; l < k; l++) {
                Point p = reflex[i], q = reflex[j], r = reflex[l];
                double d = 2 * (p.x * (q.y - r.y) + q.x * (r.y - p.y) + r.x * (p.y - q.y));
                if (fabs(d) < EPS)
                    continue;
                double s1 = p.x * p.x + p.y * p.y, s2 = q.x * q.x + q.y * q.y;
                double s3 = r.x * r.x + r.y * r.y;
                cand.push_back({(s1 * (q.y - r.y) + s2 * (r.y - p.y) + s3 * (p.y - q.y)) / d,
                                (s1 * (r.x - q.x) + s2 * (p.x - r.x) + s3 * (q.x - p.x)) / d});
            }
    double best = 0;
    for (Point c : cand)
        best = max(best, distanceToFence(c.x, c.y));
    printf("%.2f\n", best);
}
