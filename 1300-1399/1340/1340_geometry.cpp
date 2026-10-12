#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

const double PI = std::acos(-1.0);
const double TURN = 2 * PI;
const double HALF_TURN = 180.0;
const double FULL_TURN_DEGREES = 360.0;
const double ROUND_OFF = 1e-15;
const int FIELDS = 6;

// an arc angle in [0, 2 pi)
double ahead(double angle) {
    angle = std::fmod(angle, TURN);
    if (angle < 0)
        angle += TURN;
    return angle;
}

// the second-circle centers, using power = d squared minus r squared
// to test whether the circles meet
std::vector<std::pair<double, double>> circleCross(double r, double cy, double kx, double ky,
                                                   double power) {
    if (power < 0 || power > 8 * r * r)
        return {};
    double d = std::hypot(kx, ky - cy);
    double along = (4 * r * r + power) / (2 * d);
    double side = std::sqrt(std::max(0.0, power * (8 * r * r - power))) / (2 * d);
    double ux = kx / d, uy = (ky - cy) / d, mx = ux * along, my = cy + uy * along;
    return {{mx - uy * side, my + ux * side}, {mx + uy * side, my - ux * side}};
}

double shortest(double x, double y, double heading, double r, double kx, double ky) {
    double dx = kx - x, dy = ky - y;
    if (r * r == 0 || (dx == 0 && dy == 0))
        return std::hypot(dx, dy);
    heading = std::fmod(heading, FULL_TURN_DEGREES);
    if (heading < 0)
        heading += FULL_TURN_DEGREES;
    int quadrant = static_cast<int>(std::floor(heading / 90 + 0.5));
    heading = (heading - quadrant * 90) * PI / HALF_TURN;
    kx = dx * std::cos(heading) + dy * std::sin(heading);
    ky = -dx * std::sin(heading) + dy * std::cos(heading);
    for (int i = 0; i < quadrant % 4; ++i) {
        double old = kx;
        kx = ky;
        ky = -old;
    }
    double best = HUGE_VAL;
    // sign 1 turns left (counter-clockwise), sign -1 turns right
    for (int sign : {1, -1}) {
        double cy = sign * r;
        double power = dx * dx + dy * dy - 2 * cy * ky;
        if (power < 0 && power >= -ROUND_OFF * (dx * dx + dy * dy))
            power = 0.0;
        // an arc, then straight along the tangent to the crumb
        if (power >= 0) {
            double run = std::sqrt(power);
            double leave = std::atan2(kx, r - sign * ky) - std::atan2(run, r);
            best = std::min(best, r * ahead(leave) + run);
        }
        // an arc, then an arc the other way around a circle 2r further out
        // that passes through the crumb
        for (auto &o : circleCross(r, cy, kx, ky, power)) {
            double first = ahead(std::atan2(o.first, r - sign * o.second));
            double vx = -o.first, vy = cy - o.second; // the switch radius, doubled
            double ex = kx - o.first, ey = ky - o.second;
            double last = std::atan2(-sign * (vx * ey - vy * ex), vx * ex + vy * ey);
            best = std::min(best, r * (first + ahead(last)));
        }
    }
    return best;
}

int main() {
    double x = 0, y = 0, a = 0, r = 0, kx = 0, ky = 0;
    if (scanf("%lf %lf %lf %lf %lf %lf", &x, &y, &a, &r, &kx, &ky) != FIELDS)
        return 0;
    printf("%.4f\n", shortest(x, y, a, std::fabs(r), kx, ky));
    return 0;
}
