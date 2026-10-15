#include <algorithm>
#include <cstdio>
#include <vector>

struct P {
    double x, y;
};
typedef std::vector<P> Poly;

double cross(P a, P b, P c) { return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x); }

// the part of a convex polygon on the given side (sign of the cross
// product) of the line through a and b
Poly clip(const Poly& poly, P a, P b, double sign) {
    Poly out;
    size_t count = poly.size();
    for (size_t i = 0; i < count; i++) {
        P p = poly[i], q = poly[(i + 1) % count];
        double sp = cross(a, b, p) * sign, sq = cross(a, b, q) * sign;
        if (sp >= 0) {
            out.push_back(p);
        }
        if ((sp > 0 && sq < 0) || (sp < 0 && sq > 0)) {
            double t = sp / (sp - sq);
            out.push_back({p.x + (q.x - p.x) * t, p.y + (q.y - p.y) * t});
        }
    }
    return out;
}

double area(const Poly& poly) {
    double total = 0;
    for (size_t i = 0; i < poly.size(); i++) {
        P a = poly[(i + poly.size() - 1) % poly.size()], b = poly[i];
        total += a.x * b.y - b.x * a.y;
    }
    return total / 2;
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    Poly pts(n);
    for (P& p : pts) {
        scanf("%lf %lf", &p.x, &p.y);
    }
    k = std::min(k, n - k);
    if (k == 1) {
        // every rope lies along the fence: the rabbit cannot get in at all
        printf("%.9f\n", 1.0);
        return 0;
    }
    double whole = area(pts), reachable = 0;
    for (int i = 0; i < n; i++) {
        // the face next to side i is on the side's side of every rope; only
        // the ropes from vertices i + 1 - k, ..., i pass over that side
        P mid = {(pts[i].x + pts[(i + 1) % n].x) / 2, (pts[i].y + pts[(i + 1) % n].y) / 2};
        std::vector<int> ropes = {i + 1 - k, i};
        for (int j = i + 2 - k; j < i; j++) {
            ropes.push_back(j);
        }
        Poly face = pts;
        for (int j : ropes) {
            P a = pts[(j % n + n) % n], b = pts[(j + k) % n];
            face = clip(face, a, b, cross(a, b, mid) > 0 ? 1 : -1);
            if (face.empty()) {
                break;
            }
        }
        reachable += face.empty() ? 0 : area(face);
    }
    printf("%.9f\n", (whole - reachable) / whole);
}
