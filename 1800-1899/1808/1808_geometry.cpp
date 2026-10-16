#include <algorithm>
#include <cmath>
#include <cstdio>

const double EPS = 1e-9;

struct Point {
    double x, y;
};

double cross(Point a, Point b) { return a.x * b.y - a.y * b.x; }

// where the refracted line of sight enters the planet and where it would
// leave it again
void chord(double r, double eta, double x, double y, double dx, double dy, Point &enter,
           Point &leave) {
    // the first crossing of the line of sight with the circle
    double a = dx * dx + dy * dy, halfB = x * dx + y * dy, c = x * x + y * y - r * r;
    double t = (-halfB - std::sqrt(std::max(0.0, halfB * halfB - a * c))) / a;
    enter = {x + dx * t, y + dy * t};
    double length = std::hypot(dx, dy), ux = dx / length, uy = dy / length;
    // split the direction into the inward normal and the tangent; Snell's
    // law shrinks the tangent part by eta
    double nx = -enter.x / r, ny = -enter.y / r, along = ux * nx + uy * ny;
    double tx = (ux - along * nx) / eta, ty = (uy - along * ny) / eta;
    double inward = std::sqrt(std::max(0.0, 1 - tx * tx - ty * ty));
    double vx = inward * nx + tx, vy = inward * ny + ty;
    // the chord from the entry point along v has length -2 (e . v)
    double span = -2 * (enter.x * vx + enter.y * vy);
    leave = {enter.x + vx * span, enter.y + vy * span};
}

int main() {
    double r, eta, ax, ay, adx, ady, bx, by, bdx, bdy;
    if (scanf("%lf %lf", &r, &eta) != 2) return 0;
    if (scanf("%lf %lf %lf %lf", &ax, &ay, &adx, &ady) < 1) return 0;
    if (scanf("%lf %lf %lf %lf", &bx, &by, &bdx, &bdy) < 1) return 0;
    Point p1, q1, p2, q2;
    chord(r, eta, ax, ay, adx, ady, p1, q1);
    chord(r, eta, bx, by, bdx, bdy, p2, q2);
    Point d1 = {q1.x - p1.x, q1.y - p1.y}, d2 = {q2.x - p2.x, q2.y - p2.y};
    Point w = {p2.x - p1.x, p2.y - p1.y};
    double den = cross(d1, d2);
    bool seen;
    if (std::fabs(den) < EPS) {
        // parallel chords meet only if they lie on one line
        seen = std::fabs(cross(w, d1)) < EPS * std::max(1.0, std::hypot(d1.x, d1.y));
    } else {
        double s = cross(w, d2) / den, t = cross(w, d1) / den;
        seen = EPS < s && s < 1 - EPS && EPS < t && t < 1 - EPS;
    }
    puts(seen ? "Yes" : "No");
    return 0;
}
