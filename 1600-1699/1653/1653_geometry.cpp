#include <algorithm>
#include <array>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
using namespace std;

const int DIM = 3;
typedef array<double, DIM> Vec;
typedef array<Vec, DIM> Mat;  // rows

const double PHI = (1 + sqrt(5.0)) / 2;
const double TINY = 1e-14;
const double SAME = 1e-7;  // equal edge lengths up to rounding

double dot(const Vec &a, const Vec &b) {
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

Vec unit(const Vec &v) {
    double n = sqrt(dot(v, v));
    return {v[0] / n, v[1] / n, v[2] / n};
}

Vec cross(const Vec &a, const Vec &b) {
    return {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
}

double dist(const Vec &a, const Vec &b) {
    Vec d = {a[0] - b[0], a[1] - b[1], a[2] - b[2]};
    return sqrt(dot(d, d));
}

Vec turned(const Mat &m, const Vec &v) {
    return {dot(m[0], v), dot(m[1], v), dot(m[2], v)};
}

Mat compose(const Mat &a, const Mat &b) {
    Mat r{};
    for (int i = 0; i < DIM; i++)
        for (int j = 0; j < DIM; j++)
            for (int k = 0; k < DIM; k++)
                r[i][j] += a[i][k] * b[k][j];
    return r;
}

// rotation by angle around axis, right-handed
Mat rotation(const Vec &axis, double angle) {
    Vec u = unit(axis);
    double x = u[0], y = u[1], z = u[2], c = cos(angle), s = sin(angle), t = 1 - c;
    return {{{t * x * x + c, t * x * y - s * z, t * x * z + s * y},
             {t * x * y + s * z, t * y * y + c, t * y * z - s * x},
             {t * x * z - s * y, t * y * z + s * x, t * z * z + c}}};
}

vector<Vec> solid(const string &name) {
    const double signs[] = {-1, 1};
    vector<Vec> pts;
    if (name == "tetrahedron") {
        pts = {{1, 1, 1}, {1, -1, -1}, {-1, 1, -1}, {-1, -1, 1}};
    } else if (name == "octahedron") {
        pts = {{1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1}};
    } else if (name == "icosahedron") {
        for (double a : signs)
            for (double b : signs) {
                pts.push_back({0, a, b * PHI});
                pts.push_back({a, b * PHI, 0});
                pts.push_back({b * PHI, 0, a});
            }
    } else {
        for (double x : signs)
            for (double y : signs)
                for (double z : signs)
                    pts.push_back({x, y, z});
        if (name == "dodecahedron")
            for (double a : signs)
                for (double b : signs) {
                    pts.push_back({0, a / PHI, b * PHI});
                    pts.push_back({a / PHI, b * PHI, 0});
                    pts.push_back({b * PHI, 0, a / PHI});
                }
    }
    for (Vec &p : pts)
        p = unit(p);
    return pts;
}

int main() {
    string word;
    int n;
    if (!(cin >> word >> n))
        return 0;
    vector<Vec> guns = solid(word);
    double edge = numeric_limits<double>::max();
    for (const Vec &a : guns)
        for (const Vec &b : guns)
            if (dist(a, b) > SAME)
                edge = min(edge, dist(a, b));
    // turn the solid so that one gun points along z and a neighbour lies in
    // the half-plane x >= 0 of Oxz; any choice is the same up to symmetry
    Vec z = guns[0], near = guns[0];
    for (const Vec &g : guns)
        if (fabs(dist(g, z) - edge) < SAME) {
            near = g;
            break;
        }
    double along = dot(near, z);
    Vec x = unit({near[0] - along * z[0], near[1] - along * z[1], near[2] - along * z[2]});
    Vec y = cross(z, x);
    for (Vec &g : guns)
        g = unit({dot(g, x), dot(g, y), dot(g, z)});
    Mat turn = {{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}};
    double total = 0;
    for (int i = 0; i < n; i++) {
        Vec v;
        for (double &c : v)
            cin >> c;
        Vec target = unit({-v[0], -v[1], -v[2]});  // the ship comes from there
        Vec gun = turned(turn, guns[0]);
        for (const Vec &g : guns)
            if (dot(turned(turn, g), target) > dot(gun, target))
                gun = turned(turn, g);
        double angle = acos(max(-1.0, min(1.0, dot(gun, target))));
        total += angle;
        Vec axis = cross(gun, target);
        if (angle > TINY && sqrt(dot(axis, axis)) > TINY)
            // the shortest turn: around the axis normal to both directions
            turn = compose(rotation(axis, angle), turn);
    }
    printf("%.5f\n", total);
}
