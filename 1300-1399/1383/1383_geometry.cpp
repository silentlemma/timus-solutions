#include <algorithm>
#include <cstdio>
#include <map>
#include <numeric>
#include <utility>
#include <vector>

typedef long long ll;
typedef std::pair<ll, ll> Point;
typedef std::vector<ll> Key;

ll cross(Point o, Point a, Point b) {
    return (a.first - o.first) * (b.second - o.second) -
           (a.second - o.second) * (b.first - o.first);
}

// strict convex hull, counterclockwise, of sorted distinct points
std::vector<Point> hull(const std::vector<Point> &pts) {
    std::vector<Point> h(2 * pts.size());
    size_t k = 0;
    for (size_t i = 0; i < pts.size(); i++) {
        while (k >= 2 && cross(h[k - 2], h[k - 1], pts[i]) <= 0)
            k--;
        h[k++] = pts[i];
    }
    for (size_t i = pts.size() - 1, low = k + 1; i-- > 0;) {
        while (k >= low && cross(h[k - 2], h[k - 1], pts[i]) <= 0)
            k--;
        h[k++] = pts[i];
    }
    h.resize(k - 1);
    return h;
}

// coordinates of the points in the frame o + s e1 + t e2 over their least
// common denominator: the denominator, then the pairs, sorted if asked
Key inFrame(const std::vector<Point> &pts, Point o, Point e1, Point e2, bool sortPairs) {
    ll d = e1.first * e2.second - e1.second * e2.first, g = d;
    std::vector<std::pair<ll, ll>> pairs;
    for (const Point &p : pts) {
        ll qx = p.first - o.first, qy = p.second - o.second;
        ll s = qx * e2.second - qy * e2.first, t = e1.first * qy - e1.second * qx;
        pairs.push_back({s, t});
        g = std::gcd(g, std::gcd(s, t));
    }
    if (sortPairs)
        std::sort(pairs.begin(), pairs.end());
    Key key(1, d / g);
    for (auto &pr : pairs) {
        key.push_back(pr.first / g);
        key.push_back(pr.second / g);
    }
    return key;
}

// the same for two point lists exactly when an affine map of positive
// determinant takes one onto the other
Key canonical(const std::vector<Point> &pts) {
    std::vector<Point> distinct(pts);
    std::sort(distinct.begin(), distinct.end());
    distinct.erase(std::unique(distinct.begin(), distinct.end()), distinct.end());
    if (distinct.size() == 1)
        return {0, (ll)pts.size()};
    std::vector<Point> h = hull(distinct);
    if (h.size() == 2) {
        // on one line: positions from 0 to 1 between the ends, read either way
        ll dx = h[1].first - h[0].first, dy = h[1].second - h[0].second;
        ll length = dx * dx + dy * dy, g = length;
        std::vector<ll> forward;
        for (const Point &p : pts) {
            forward.push_back((p.first - h[0].first) * dx + (p.second - h[0].second) * dy);
            g = std::gcd(g, forward.back());
        }
        ll den = length / g;
        std::vector<ll> backward;
        for (ll &t : forward) {
            t /= g;
            backward.push_back(den - t);
        }
        std::sort(forward.begin(), forward.end());
        std::sort(backward.begin(), backward.end());
        Key key = {1, den};
        const std::vector<ll> &pick = std::min(forward, backward);
        key.insert(key.end(), pick.begin(), pick.end());
        return key;
    }
    // the frame at hull vertex i: it goes to 0, the next to (1, 0) and the
    // previous to (0, 1); a map of positive determinant keeps the order
    size_t k = h.size();
    auto frameKey = [&](size_t i, const std::vector<Point> &points, bool sortPairs) {
        Point o = h[i], nxt = h[(i + 1) % k], prv = h[(i + k - 1) % k];
        return inFrame(points, o, {nxt.first - o.first, nxt.second - o.second},
                       {prv.first - o.first, prv.second - o.second}, sortPairs);
    };
    std::vector<Key> shapes;
    for (size_t i = 0; i < k; i++) {
        std::vector<Point> turned(h.begin() + i, h.end());
        turned.insert(turned.end(), h.begin(), h.begin() + i);
        shapes.push_back(frameKey(i, turned, false));
    }
    Key best = *std::min_element(shapes.begin(), shapes.end()), chosen;
    for (size_t i = 0; i < k; i++)
        if (shapes[i] == best) {
            Key candidate = frameKey(i, pts, true);
            if (chosen.empty() || candidate < chosen)
                chosen = candidate;
        }
    Key key = {2, (ll)k};
    key.insert(key.end(), chosen.begin(), chosen.end());
    return key;
}

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::map<Key, std::vector<int>> classes;
    std::map<Key, int> sizes;
    for (int project = 1; project <= n; project++) {
        int m = 0;
        if (scanf("%d", &m) != 1)
            return 0;
        std::vector<Point> pts(m);
        for (Point &p : pts)
            if (scanf("%lld %lld", &p.first, &p.second) != 2)
                return 0;
        Key key = canonical(pts);
        classes[key].push_back(project);
        sizes[key] = m;
    }
    // smaller projects first, then by the first project of the class
    std::vector<std::pair<std::pair<int, int>, const std::vector<int> *>> order;
    for (auto &c : classes)
        order.push_back({{sizes[c.first], c.second[0]}, &c.second});
    std::sort(order.begin(), order.end());
    printf("%d\n", (int)order.size());
    for (auto &o : order) {
        for (int project : *o.second)
            printf("%d ", project);
        printf("0\n");
    }
    return 0;
}
