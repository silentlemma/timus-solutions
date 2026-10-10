#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

typedef std::pair<long long, long long> Pt;

long long cross(const Pt &o, const Pt &a, const Pt &b) {
    return (a.first - o.first) * (b.second - o.second) -
           (a.second - o.second) * (b.first - o.first);
}

int main() {
    int n, gap;
    scanf("%d %d", &n, &gap);
    std::vector<Pt> pts(n);
    for (auto &p : pts) {
        scanf("%lld %lld", &p.first, &p.second);
    }
    std::sort(pts.begin(), pts.end());
    // the shortest wall is the convex hull pushed out by L: its straight
    // parts add up to the hull perimeter, and its arcs turn once around a
    // full circle of radius L in total
    std::vector<Pt> hull;
    for (int pass = 0; pass < 2; pass++) {
        std::vector<Pt> part;
        for (const Pt &p : pts) {
            while (part.size() >= 2 && cross(part[part.size() - 2], part.back(), p) <= 0) {
                part.pop_back();
            }
            part.push_back(p);
        }
        hull.insert(hull.end(), part.begin(), part.end() - 1);
        std::reverse(pts.begin(), pts.end());
    }
    double length = 2 * std::acos(-1.0) * gap;
    for (size_t k = 0; k < hull.size(); k++) {
        const Pt &a = hull[k];
        const Pt &b = hull[(k + 1) % hull.size()];
        length += std::hypot(double(a.first - b.first), double(a.second - b.second));
    }
    printf("%lld\n", std::llround(length));
}
