#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

typedef pair<double, double> Point;

const int CORNERS = 3;
const int ROUNDS = 200;  // bisection steps, far beyond double precision

Point pts[CORNERS];
double sides[CORNERS], perimeter;
vector<pair<double, Point>> corners;  // arc positions of the corners, twice round

double shoelace(const vector<Point> &poly) {
    double twice = 0;
    for (size_t i = 0; i < poly.size(); i++) {
        const Point &a = poly[(i + poly.size() - 1) % poly.size()], &b = poly[i];
        twice += a.first * b.second - b.first * a.second;
    }
    return fabs(twice) / 2;
}

// the coast point at arc length s from the first corner
Point point(double s) {
    s = fmod(s, perimeter);
    for (int i = 0; i < CORNERS; i++) {
        if (s <= sides[i] || i == CORNERS - 1) {
            double t = min(s / sides[i], 1.0);
            const Point &a = pts[i], &b = pts[(i + 1) % CORNERS];
            return {a.first + (b.first - a.first) * t, a.second + (b.second - a.second) * t};
        }
        s -= sides[i];
    }
    return pts[0];
}

// area cut off by the coast from s to t (s < t) and the chord
double area(double s, double t) {
    vector<Point> poly = {point(s)};
    for (const auto &c : corners)
        if (s < c.first && c.first < t)
            poly.push_back(c.second);
    poly.push_back(point(t));
    return shoelace(poly);
}

int main() {
    for (Point &p : pts)
        if (scanf("%lf %lf", &p.first, &p.second) != 2)
            return 0;
    for (int i = 0; i < CORNERS; i++) {
        const Point &a = pts[i], &b = pts[(i + 1) % CORNERS];
        sides[i] = hypot(b.first - a.first, b.second - a.second);
        perimeter += sides[i];
    }
    double pos = 0;
    for (int lap = 0; lap < 2; lap++)
        for (int i = 0; i < CORNERS; i++) {
            corners.push_back({pos, pts[i]});
            pos += sides[i];
        }
    double half = perimeter / 2, total = shoelace(vector<Point>(pts, pts + CORNERS));
    auto excess = [&](double s) { return area(s, s + half) - total / 2; };
    // the excess changes sign over half a turn, as the other part is the
    // complement, so a chord splitting both evenly always exists
    double lo = 0, hi = half;
    bool low = excess(lo) > 0;
    for (int r = 0; r < ROUNDS; r++) {
        double mid = (lo + hi) / 2;
        if ((excess(mid) > 0) == low)
            lo = mid;
        else
            hi = mid;
    }
    double s = (lo + hi) / 2;
    Point a = point(s), b = point(s + half);
    printf("YES\n%.12f %.12f\n%.12f %.12f\n", a.first, a.second, b.first, b.second);
}
