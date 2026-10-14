#include <algorithm>
#include <cmath>
#include <cstdio>
#include <tuple>
#include <vector>

using namespace std;

const double BOX = 2;  // the starting cell is a square of half-side BOX * R around the disk
const double SPAN = 4; // a site cuts a cell only within twice its reach: squared, 4 times
const double EPS = 1e-9;

struct Pt {
    double x, y;
};

// the part of the convex polygon with (p - m) . d <= 0
vector<Pt> clip(const vector<Pt> &poly, Pt m, Pt d) {
    vector<Pt> out;
    size_t n = poly.size();
    for (size_t k = 0; k < n; k++) {
        Pt p = poly[k], q = poly[(k + 1) % n];
        double sp = (p.x - m.x) * d.x + (p.y - m.y) * d.y;
        double sq = (q.x - m.x) * d.x + (q.y - m.y) * d.y;
        if (sp <= 0)
            out.push_back(p);
        if ((sp < 0 && sq > 0) || (sq < 0 && sp > 0)) {
            double t = sp / (sp - sq);
            out.push_back({p.x + t * (q.x - p.x), p.y + t * (q.y - p.y)});
        }
    }
    return out;
}

// whether a point lies in the convex polygon, counterclockwise
bool inside(const vector<Pt> &poly, Pt a) {
    size_t n = poly.size();
    for (size_t k = 0; k < n; k++) {
        Pt p = poly[k], q = poly[(k + 1) % n];
        if ((q.x - p.x) * (a.y - p.y) - (q.y - p.y) * (a.x - p.x) < -EPS)
            return false;
    }
    return true;
}

// the largest distance from c to a point of the polygon inside the disk of
// radius r around the origin
double farthest(const vector<Pt> &poly, Pt c, double r) {
    double best = 0;
    size_t n = poly.size();
    for (size_t k = 0; k < n; k++) {
        Pt p = poly[k], q = poly[(k + 1) % n];
        if (p.x * p.x + p.y * p.y <= r * r)
            best = max(best, hypot(p.x - c.x, p.y - c.y));
        // where the edge crosses the circle: |p + t (q - p)| = r
        double ux = q.x - p.x, uy = q.y - p.y;
        double a = ux * ux + uy * uy, b = p.x * ux + p.y * uy, cc = p.x * p.x + p.y * p.y - r * r;
        double disc = b * b - a * cc;
        if (a > 0 && disc >= 0)
            for (double t : {(-b - sqrt(disc)) / a, (-b + sqrt(disc)) / a})
                if (t >= 0 && t <= 1)
                    best = max(best, hypot(p.x + t * ux - c.x, p.y + t * uy - c.y));
    }
    // on an arc inside the cell the distance peaks at the circle point
    // opposite the site, if that point is in the cell
    double norm = hypot(c.x, c.y);
    Pt o = norm > 0 ? Pt{-r * c.x / norm, -r * c.y / norm} : Pt{r, 0};
    if (inside(poly, o))
        best = max(best, hypot(o.x - c.x, o.y - c.y));
    return best;
}

int main() {
    int n;
    double r;
    scanf("%d %lf", &n, &r);
    vector<Pt> sites(n);
    for (Pt &s : sites)
        scanf("%lf %lf", &s.x, &s.y);
    double side = BOX * r, answer = 0;
    for (Pt c : sites) {
        vector<Pt> poly = {{-side, -side}, {side, -side}, {side, side}, {-side, side}};
        vector<pair<double, int>> order;
        for (int j = 0; j < n; j++)
            order.push_back({pow(sites[j].x - c.x, 2) + pow(sites[j].y - c.y, 2), j});
        sort(order.begin(), order.end());
        for (auto [d, j] : order) {
            if (d == 0)
                continue; // the site itself, or another one at the same point
            double reach = 0;
            for (Pt v : poly)
                reach = max(reach, pow(v.x - c.x, 2) + pow(v.y - c.y, 2));
            if (d > SPAN * reach)
                break;
            Pt o = sites[j];
            poly = clip(poly, {(o.x + c.x) / 2, (o.y + c.y) / 2}, {o.x - c.x, o.y - c.y});
        }
        answer = max(answer, farthest(poly, c, r));
    }
    printf("%.8f\n", answer);
}
