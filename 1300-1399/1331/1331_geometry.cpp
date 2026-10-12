#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>

const double HALF_TURN = 180.0;
const double MOST = 4.0; // the longest squared chord, between opposite points
const int LINE = 64;
const int FIELDS = 3;

struct Point {
    double x, y, z;
};

// the point on the unit sphere
Point unit(double latitude, double longitude) {
    double a = latitude * std::acos(-1.0) / HALF_TURN, b = longitude * std::acos(-1.0) / HALF_TURN;
    return {std::cos(a) * std::cos(b), std::cos(a) * std::sin(b), std::sin(a)};
}

int main() {
    int n = 0, m = 0;
    double r = 0;
    if (scanf("%d %d %lf", &n, &m, &r) != FIELDS)
        return 0;
    std::vector<Point> pads(m);
    for (auto &p : pads) {
        double w = 0, l = 0;
        if (scanf("%lf %lf", &w, &l) != 2)
            return 0;
        p = unit(w, l);
    }
    std::string out;
    char line[LINE];
    for (int i = 0; i < n; i++) {
        double w = 0, l = 0;
        if (scanf("%lf %lf", &w, &l) != 2)
            return 0;
        Point q = unit(w, l);
        // the nearest pad has the shortest chord through the planet
        double best = MOST;
        for (const Point &p : pads) {
            double dx = q.x - p.x, dy = q.y - p.y, dz = q.z - p.z;
            best = std::min(best, dx * dx + dy * dy + dz * dz);
        }
        double half = std::min(1.0, std::sqrt(best) / 2);
        snprintf(line, sizeof line, "%.2f\n", 2 * r * std::asin(half));
        out += line;
    }
    fputs(out.c_str(), stdout);
    return 0;
}
