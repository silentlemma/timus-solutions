#include <algorithm>
#include <array>
#include <cmath>
#include <cstdio>
#include <tuple>
#include <vector>

using namespace std;

typedef array<double, 2> Pt;

const int CORNERS = 3, PINS = 4;
const double PI = acos(-1.0);
const double WIDE = 2 * PI / 3; // 120 degrees
const double EPS = 1e-12;
const double ROOT3 = sqrt(3.0) / 2; // the height of a unit equilateral triangle
// the pairs that share an extra point, each way round
const int PAIRINGS[][PINS] = {{0, 1, 2, 3}, {0, 2, 1, 3}, {0, 3, 1, 2},
                              {2, 3, 0, 1}, {1, 3, 0, 2}, {1, 2, 0, 3}};

double dist(const Pt &p, const Pt &q) { return hypot(p[0] - q[0], p[1] - q[1]); }

// the point with the least total distance to three points (see 1451)
Pt fermat(const array<Pt, CORNERS> &p) {
    for (int i = 0; i < CORNERS; i++)
        for (int j = i + 1; j < CORNERS; j++)
            if (dist(p[i], p[j]) < EPS)
                return p[i];
    double angle[CORNERS], side[CORNERS];
    for (int i = 0; i < CORNERS; i++) {
        const Pt &a = p[i], &b = p[(i + 1) % CORNERS], &c = p[(i + 2) % CORNERS];
        double ux = b[0] - a[0], uy = b[1] - a[1], wx = c[0] - a[0], wy = c[1] - a[1];
        angle[i] = atan2(fabs(ux * wy - uy * wx), ux * wx + uy * wy);
        side[i] = dist(b, c);
    }
    for (int i = 0; i < CORNERS; i++)
        if (angle[i] >= WIDE)
            return p[i];
    double total = 0, x = 0, y = 0;
    for (int i = 0; i < CORNERS; i++) {
        double w = side[i] / sin(angle[i] + PI / CORNERS);
        total += w;
        x += w * p[i][0];
        y += w * p[i][1];
    }
    return {x / total, y / total};
}

double shortest(const array<Pt, PINS> &p) {
    // trees without extra points: the best spanning tree
    vector<tuple<double, int, int>> edges;
    for (int i = 0; i < PINS; i++)
        for (int j = i + 1; j < PINS; j++)
            edges.push_back({dist(p[i], p[j]), i, j});
    sort(edges.begin(), edges.end());
    int group[PINS];
    for (int i = 0; i < PINS; i++)
        group[i] = i;
    auto root = [&](int x) {
        while (group[x] != x)
            x = group[x];
        return x;
    };
    double best = 0;
    for (auto [length, i, j] : edges) {
        int a = root(i), b = root(j);
        if (a != b) {
            group[a] = b;
            best += length;
        }
    }
    // one extra point joining three pins, the fourth wired to one of the four
    for (int rest = 0; rest < PINS; rest++) {
        array<Pt, CORNERS> trio;
        int k = 0;
        for (int i = 0; i < PINS; i++)
            if (i != rest)
                trio[k++] = p[i];
        Pt s = fermat(trio);
        double star = 0, link = dist(p[rest], s);
        for (auto &q : trio) {
            star += dist(s, q);
            link = min(link, dist(p[rest], q));
        }
        best = min(best, star + link);
    }
    // two extra points, {a, b} on one and {c, d} on the other: the Melzak
    // construction gives both, and the real length of that tree is a candidate
    for (auto &pr : PAIRINGS) {
        const Pt &a = p[pr[0]], &b = p[pr[1]], &c = p[pr[2]], &d = p[pr[3]];
        double mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1];
        for (int side : {1, -1}) {
            Pt e = {mx - side * dy * ROOT3, my + side * dx * ROOT3};
            Pt s2 = fermat({e, c, d});
            Pt s1 = fermat({a, b, s2});
            best = min(best, dist(s1, a) + dist(s1, b) + dist(s1, s2) + dist(s2, c) + dist(s2, d));
        }
    }
    return best;
}

int main() {
    int tests;
    scanf("%d", &tests);
    while (tests--) {
        array<Pt, PINS> p;
        for (auto &q : p) {
            int x, y;
            scanf("%d %d", &x, &y);
            q = {(double)x, (double)y};
        }
        printf("%.6f\n", shortest(p));
    }
}
