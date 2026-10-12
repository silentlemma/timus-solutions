#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

const double PI = std::acos(-1.0);
const double TURN = 2 * PI;
const double EPS = 1e-9;
const double HALF_TURN = 180.0;
const int FIELDS = 6;

// an arc angle in [0, 2 pi), with angles a hair below a full turn taken
// as no turn at all
double ahead(double angle) {
    angle = std::fmod(angle, TURN);
    if (angle < 0)
        angle += TURN;
    return angle > TURN - EPS ? 0.0 : angle;
}

// the points where the circles around a and b of radii ra and rb meet
std::vector<std::pair<double, double>> circleCross(double ax, double ay, double ra, double bx,
                                                   double by, double rb) {
    double d = std::hypot(bx - ax, by - ay);
    if (d == 0 || d > ra + rb + EPS || d < std::fabs(ra - rb) - EPS)
        return {};
    double along = (ra * ra - rb * rb + d * d) / (2 * d);
    double side = std::sqrt(std::max(0.0, ra * ra - along * along));
    double ux = (bx - ax) / d, uy = (by - ay) / d, mx = ax + ux * along, my = ay + uy * along;
    return {{mx - uy * side, my + ux * side}, {mx + uy * side, my - ux * side}};
}

double shortest(double x, double y, double heading, double r, double kx, double ky) {
    if (r == 0)
        return std::hypot(kx - x, ky - y);
    double best = HUGE_VAL;
    // sign 1 turns left (counter-clockwise), sign -1 turns right
    for (int sign : {1, -1}) {
        double cx = x - sign * r * std::sin(heading), cy = y + sign * r * std::cos(heading);
        double start = std::atan2(y - cy, x - cx); // where the cockroach is on the circle
        // an arc, then straight along the tangent to the crumb
        double d = std::hypot(kx - cx, ky - cy);
        if (d >= r - EPS) {
            double run = std::sqrt(std::max(0.0, d * d - r * r));
            double leave = std::atan2(ky - cy, kx - cx) - sign * std::acos(std::min(1.0, r / d));
            best = std::min(best, r * ahead(sign * (leave - start)) + run);
        }
        // an arc, then an arc the other way around a circle 2r further out
        // that passes through the crumb
        for (auto &o : circleCross(cx, cy, 2 * r, kx, ky, r)) {
            double sw = std::atan2(o.second - cy, o.first - cx);
            double first = ahead(sign * (sw - start));
            double back = sw + PI; // the switch point seen from the new center
            double end = std::atan2(ky - o.second, kx - o.first);
            best = std::min(best, r * (first + ahead(-sign * (end - back))));
        }
    }
    return best;
}

int main() {
    double x = 0, y = 0, a = 0, r = 0, kx = 0, ky = 0;
    if (scanf("%lf %lf %lf %lf %lf %lf", &x, &y, &a, &r, &kx, &ky) != FIELDS)
        return 0;
    printf("%.4f\n", shortest(x, y, a * PI / HALF_TURN, std::fabs(r), kx, ky));
    return 0;
}
