#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <utility>
#include <vector>

typedef long long ll;
typedef std::pair<ll, ll> P;

const int CORNERS = 3;

ll cross(P o, P a, P b) {
    return (a.first - o.first) * (b.second - o.second) -
           (a.second - o.second) * (b.first - o.first);
}

// convex hull, counterclockwise, without points on the edges
std::vector<P> hull(std::vector<P> pts) {
    std::sort(pts.begin(), pts.end());
    pts.erase(std::unique(pts.begin(), pts.end()), pts.end());
    std::vector<P> h(2 * pts.size());
    int k = 0;
    for (size_t i = 0; i < pts.size(); i++) {
        while (k >= 2 && cross(h[k - 2], h[k - 1], pts[i]) <= 0)
            k--;
        h[k++] = pts[i];
    }
    for (int i = (int)pts.size() - 2, t = k + 1; i >= 0; i--) {
        while (k >= t && cross(h[k - 2], h[k - 1], pts[i]) <= 0)
            k--;
        h[k++] = pts[i];
    }
    h.resize(k - 1);
    return h;
}

// an open convex polygon: the places where the tanker hits a ship
struct Polygon {
    std::vector<P> v;
    ll x0, x1, y0, y1;
    std::vector<std::pair<P, P>> axes; // edge normal, (lo, hi) of the projection

    explicit Polygon(std::vector<P> vertices) : v(vertices) {
        x0 = x1 = v[0].first, y0 = y1 = v[0].second;
        for (P p : v) {
            x0 = std::min(x0, p.first), x1 = std::max(x1, p.first);
            y0 = std::min(y0, p.second), y1 = std::max(y1, p.second);
        }
        for (size_t i = 0; i < v.size(); i++) {
            P a = v[i], b = v[(i + 1) % v.size()];
            P n = {b.second - a.second, a.first - b.first};
            P range = project(n);
            axes.push_back({n, range});
        }
    }

    P project(P n) const {
        ll lo = n.first * v[0].first + n.second * v[0].second, hi = lo;
        for (P p : v) {
            ll d = n.first * p.first + n.second * p.second;
            lo = std::min(lo, d), hi = std::max(hi, d);
        }
        return {lo, hi};
    }

    // whether p is strictly inside
    bool holds(P p) const {
        for (size_t i = 0; i < v.size(); i++)
            if (cross(v[i], v[(i + 1) % v.size()], p) <= 0)
                return false;
        return true;
    }

    // whether the segment pq crosses the inside: no axis separates them,
    // neither an edge normal nor the normal of pq itself
    bool blocks(P p, P q) const {
        if (std::max(p.first, q.first) <= x0 || std::min(p.first, q.first) >= x1)
            return false;
        if (std::max(p.second, q.second) <= y0 || std::min(p.second, q.second) >= y1)
            return false;
        for (auto &axis : axes) {
            P n = axis.first;
            ll a = n.first * p.first + n.second * p.second,
               b = n.first * q.first + n.second * q.second;
            if (std::max(a, b) <= axis.second.first || std::min(a, b) >= axis.second.second)
                return false;
        }
        P n = {q.second - p.second, p.first - q.first};
        ll c = n.first * p.first + n.second * p.second;
        P range = project(n);
        return range.first < c && c < range.second;
    }
};

int main() {
    ll dx, dy;
    scanf("%lld %lld", &dx, &dy);
    std::vector<P> tanker(CORNERS);
    for (P &p : tanker)
        scanf("%lld %lld", &p.first, &p.second);
    P goal;
    int n;
    scanf("%lld %lld %d", &goal.first, &goal.second, &n);
    // the tanker is placed by its first corner; offsets of all corners
    P start = tanker[0];
    ll xlo = 0, xhi = dx, ylo = 0, yhi = dy;
    std::vector<P> offsets;
    for (P t : tanker) {
        P o = {t.first - start.first, t.second - start.second};
        offsets.push_back(o);
        xlo = std::max(xlo, -o.first), xhi = std::min(xhi, dx - o.first);
        ylo = std::max(ylo, -o.second), yhi = std::min(yhi, dy - o.second);
    }
    std::vector<Polygon> polygons;
    for (int i = 0; i < n; i++) {
        std::vector<P> ship(CORNERS), sums;
        for (P &p : ship)
            scanf("%lld %lld", &p.first, &p.second);
        for (P s : ship)
            for (P o : offsets)
                sums.push_back({s.first - o.first, s.second - o.second});
        polygons.emplace_back(hull(sums));
    }
    auto isFree = [&](P p) {
        if (p.first < xlo || p.first > xhi || p.second < ylo || p.second > yhi)
            return false;
        for (auto &g : polygons)
            if (g.holds(p))
                return false;
        return true;
    };
    if (!isFree(goal)) {
        printf("-1\n");
        return 0;
    }
    if (goal == start) {
        printf("0.000\n");
        return 0;
    }
    // shortest paths bend only at corners of the forbidden polygons
    std::set<P> corners;
    for (auto &g : polygons)
        for (P v : g.v)
            if (isFree(v))
                corners.insert(v);
    std::vector<P> points = {start, goal};
    points.insert(points.end(), corners.begin(), corners.end());
    int m = points.size();
    std::vector<double> dist(m, INFINITY);
    std::vector<bool> done(m);
    dist[0] = 0;
    while (true) {
        int i = -1;
        for (int j = 0; j < m; j++)
            if (!done[j] && dist[j] < INFINITY && (i < 0 || dist[j] < dist[i]))
                i = j;
        if (i < 0 || i == 1)
            break;
        done[i] = true;
        P p = points[i];
        for (int j = 0; j < m; j++) {
            P q = points[j];
            if (done[j] || q == p)
                continue;
            double nd =
                dist[i] + std::hypot(double(q.first - p.first), double(q.second - p.second));
            if (nd >= dist[j])
                continue;
            bool clear = true;
            for (auto &g : polygons)
                if (g.blocks(p, q)) {
                    clear = false;
                    break;
                }
            if (clear)
                dist[j] = nd;
        }
    }
    if (dist[1] < INFINITY)
        printf("%.3f\n", dist[1]);
    else
        printf("-1\n");
}
