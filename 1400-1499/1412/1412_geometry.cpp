#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

const double PI = acos(-1.0);
const double TURN = 2 * PI;
const int SIDES = 4;

// signed area of the unit disk at the origin inside the triangle (origin, a, b)
double cut(double ax, double ay, double bx, double by) {
    double dx = bx - ax, dy = by - ay;
    double qa = dx * dx + dy * dy, qb = ax * dx + ay * dy, qc = ax * ax + ay * ay - 1;
    vector<double> marks = {0.0, 1.0};
    double disc = qb * qb - qa * qc;
    if (disc > 0) {
        double root = sqrt(disc);
        for (double t : {(-qb - root) / qa, (-qb + root) / qa})
            if (t > 0 && t < 1)
                marks.push_back(t);
    }
    sort(marks.begin(), marks.end());
    double area = 0;
    for (size_t i = 0; i + 1 < marks.size(); i++) {
        double s = marks[i], t = marks[i + 1];
        double px = ax + dx * s, py = ay + dy * s, qx = ax + dx * t, qy = ay + dy * t;
        double mx = (px + qx) / 2, my = (py + qy) / 2;
        double cross = px * qy - py * qx;
        // a piece inside the disk adds its triangle, one outside adds its sector
        area += mx * mx + my * my < 1 ? cross / 2 : atan2(cross, px * qx + py * qy) / 2;
    }
    return area;
}

// water that one umbrella moves off or onto the field
double change(double x, double y, double width, double length) {
    double cx[] = {-x, length - x, length - x, -x};
    double cy[] = {-y, -y, width - y, width - y};
    double covered = 0;
    for (int i = 0, j = SIDES - 1; i < SIDES; j = i++)
        covered += cut(cx[j], cy[j], cx[i], cy[i]);
    // the rim splits into arcs at the field's border lines
    vector<double> angles = {0.0, TURN};
    for (double d : {-x, length - x})
        if (fabs(d) <= 1) {
            angles.push_back(acos(d));
            angles.push_back(TURN - acos(d));
        }
    for (double d : {-y, width - y})
        if (fabs(d) <= 1) {
            angles.push_back(fmod(asin(d) + TURN, TURN));
            angles.push_back(PI - asin(d));
        }
    sort(angles.begin(), angles.end());
    double inside = 0;
    for (size_t i = 0; i + 1 < angles.size(); i++) {
        double m = (angles[i] + angles[i + 1]) / 2;
        double px = x + cos(m), py = y + sin(m);
        if (px >= 0 && px <= length && py >= 0 && py <= width)
            inside += angles[i + 1] - angles[i];
    }
    // rain caught over the whole disk leaves from the rim evenly by angle
    return PI * inside / TURN - covered;
}

int main() {
    int width, length, n;
    scanf("%d %d %d", &width, &length, &n);
    double total = (double)width * length;
    for (int i = 0; i < n; i++) {
        double x, y;
        scanf("%lf %lf", &x, &y);
        total += change(x, y, width, length);
    }
    printf("%.3f\n", total);
}
