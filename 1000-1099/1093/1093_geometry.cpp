#include <algorithm>
#include <cmath>
#include <iostream>

const double HALF_G = 5.0;
// coefficients this small count as zero
const double TINY = 1e-12;
// tolerance for times and for being strictly inside the rim
const double EPS = 1e-9;

double cx, cy, cz, nx, ny, nz, r, sx, sy, sz, vx, vy, vz;

// the dart at time t, if that time has come, is strictly inside the rim
bool inside(double t) {
    if (t < -EPS)
        return false;
    t = std::max(t, 0.0);
    double px = sx - cx + vx * t, py = sy - cy + vy * t, pz = sz - cz + vz * t - HALF_G * t * t;
    return px * px + py * py + pz * pz < r * r - EPS;
}

int main() {
    if (!(std::cin >> cx >> cy >> cz >> nx >> ny >> nz >> r >> sx >> sy >> sz >> vx >> vy >> vz))
        return 0;
    // the distance to the plane, times |N|, is a t^2 + 2 h t + c; a flight that
    // never crosses the plane, even one lying in it, misses
    double a = -HALF_G * nz, h = (nx * vx + ny * vy + nz * vz) / 2;
    double c = nx * (sx - cx) + ny * (sy - cy) + nz * (sz - cz);
    bool hit = false;
    if (std::fabs(a) < TINY) {
        hit = std::fabs(h) >= TINY && inside(-c / (2 * h));
    } else {
        double d = h * h - a * c;
        if (d >= -TINY) {
            double root = std::sqrt(std::max(d, 0.0));
            hit = inside((-h - root) / a) || inside((-h + root) / a);
        }
    }
    std::cout << (hit ? "HIT" : "MISSED") << "\n";
}
