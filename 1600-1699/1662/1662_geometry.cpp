#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const double EPS = 1e-7;

struct Pt {
    double x, y;
};

struct Edge {
    double ax, ay, ex, ey, nx, ny, c;  // start, direction, outward unit normal, offset
};

// the common points of two circles
void circles(Pt a, double ra, Pt b, double rb, std::vector<Pt>& out) {
    double dx = b.x - a.x, dy = b.y - a.y, d2 = dx * dx + dy * dy;
    if (d2 == 0) {
        return;
    }
    double along = (d2 + ra * ra - rb * rb) / (2 * d2);
    double h2 = ra * ra / d2 - along * along;
    if (h2 < -EPS) {
        return;
    }
    double h = sqrt(std::max(0.0, h2)), x = a.x + dx * along, y = a.y + dy * along;
    out.push_back({x - dy * h, y + dx * h});
    out.push_back({x + dy * h, y - dx * h});
}

// the common points of the line nx * x + ny * y = c (unit normal) and a circle
void lineCircle(double nx, double ny, double c, Pt centre, double radius, std::vector<Pt>& out) {
    double off = nx * centre.x + ny * centre.y - c, h2 = radius * radius - off * off;
    if (h2 < -EPS) {
        return;
    }
    double h = sqrt(std::max(0.0, h2)), x = centre.x - nx * off, y = centre.y - ny * off;
    out.push_back({x - ny * h, y + nx * h});
    out.push_back({x + ny * h, y - nx * h});
}

int main() {
    int n;
    scanf("%d", &n);
    std::vector<Pt> pts(n);
    for (Pt& p : pts) {
        int x, y;
        scanf("%d %d", &x, &y);
        p = {(double)x, (double)y};
    }
    int small, big;
    scanf("%d %d", &small, &big);
    double turn = 0;
    for (int i = 0; i < n; i++) {
        Pt a = pts[(i + n - 1) % n], b = pts[i];
        turn += a.x * b.y - b.x * a.y;
    }
    int side = turn > 0 ? 1 : -1;
    std::vector<Edge> edges(n);
    for (int i = 0; i < n; i++) {
        Pt a = pts[(i + n - 1) % n], b = pts[i];
        double ex = b.x - a.x, ey = b.y - a.y, length = hypot(ex, ey);
        double nx = side * ey / length, ny = -side * ex / length;
        edges[i] = {a.x, a.y, ex, ey, nx, ny, nx * a.x + ny * a.y};
    }
    double reach = (big + EPS) * (big + EPS), keep = (small - EPS) * (small - EPS);
    auto fits = [&](Pt p) {
        for (Pt v : pts) {
            if ((p.x - v.x) * (p.x - v.x) + (p.y - v.y) * (p.y - v.y) > reach) {
                return false;
            }
        }
        bool outside = false;
        for (const Edge& e : edges) {
            if (e.nx * p.x + e.ny * p.y > e.c) {
                outside = true;
            }
            double t = ((p.x - e.ax) * e.ex + (p.y - e.ay) * e.ey) / (e.ex * e.ex + e.ey * e.ey);
            t = std::min(1.0, std::max(0.0, t));
            double dx = p.x - e.ax - t * e.ex, dy = p.y - e.ay - t * e.ey;
            if (dx * dx + dy * dy < keep) {
                return false;
            }
        }
        return outside;
    };
    // the goat's area is where the discs of radius R around the vertices meet,
    // and when any of it is far enough from the bed, so is one of its corners
    // or a crossing of its boundary with the boundary of the bed grown by r
    std::vector<Pt> found;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            found.clear();
            if (i < j) {
                circles(pts[i], big, pts[j], big, found);
            }
            circles(pts[i], big, pts[j], small, found);
            lineCircle(edges[j].nx, edges[j].ny, edges[j].c + small, pts[i], big, found);
            for (Pt p : found) {
                if (fits(p)) {
                    printf("%.6f %.6f\n", p.x, p.y);
                    return 0;
                }
            }
        }
    }
    printf("No solution\n");
}
