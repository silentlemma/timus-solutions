#include <cmath>
#include <complex>
#include <cstdio>
#include <vector>

typedef std::complex<double> Point;

// a wrong set must move by 1e-5 to become right, so one turn misses by more
// than 1e-5 / n, while right sets given to 1e-10 miss by far less
const double EPS = 1e-8;
const double PI = std::acos(-1.0);

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<Point> z(n);
    Point centre = 0;
    for (int i = 0; i < n; i++) {
        double x, y;
        scanf("%lf %lf", &x, &y);
        z[i] = Point(x, y);
        centre += z[i];
    }
    centre /= (double)n;
    for (Point &p : z) p -= centre;
    // the vertices of a regular polygon in order turn into each other by a
    // rotation of 2 pi / n about the centre, one way or the other
    bool ok = false;
    if (std::abs(z[0]) > EPS) {
        for (int way = -1; way <= 1; way += 2) {
            Point turn = std::polar(1.0, way * 2 * PI / n);
            bool all = true;
            for (int i = 0; i < n; i++) {
                if (std::abs(z[(i + 1) % n] - turn * z[i]) > EPS) all = false;
            }
            if (all) ok = true;
        }
    }
    puts(ok ? "YES" : "NO");
    return 0;
}
