#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

const double PI = acos(-1.0);

double angle(double px, double ax, double ay, double bx, double by) {
    double ux = ax - px, uy = ay, vx = bx - px, vy = by;
    return atan2(fabs(ux * vy - uy * vx), ux * vx + uy * vy);
}

int main() {
    long long x1, y1, x2, y2;
    scanf("%lld %lld %lld %lld", &x1, &y1, &x2, &y2);
    double best;
    if (y1 * y2 < 0 || (y1 * y2 == 0 && x1 != x2)) {
        best = PI; // stand on the billboard itself
    } else if (y1 * y2 == 0) {
        best = PI / 2; // a vertical billboard standing on the road
    } else {
        y1 = llabs(y1), y2 = llabs(y2);
        vector<double> spots;
        if (y1 == y2) {
            spots.push_back((x1 + x2) / 2.0);
        } else {
            // the best spot is where a circle through both ends touches the road:
            // its distance from where the billboard's line meets the road is sqrt(QA * QB)
            double qx = x1 - (double)y1 * (x2 - x1) / (y2 - y1);
            double reach = sqrt(hypot(x1 - qx, (double)y1) * hypot(x2 - qx, (double)y2));
            spots = {qx - reach, qx + reach};
        }
        best = 0;
        for (double p : spots)
            best = max(best, angle(p, x1, y1, x2, y2));
    }
    printf("%.6f\n", best);
}
