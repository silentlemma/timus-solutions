#include <algorithm>
#include <cstdio>
#include <limits>
#include <map>
#include <set>
#include <tuple>
#include <unordered_map>
#include <vector>

// an edge from its left end to its right end, or a fly when both ends meet
struct Item {
    long long lx, ly, rx, ry;
    int polygon;
    bool top;  // the inside lies below the edge
};

static bool point(const Item &s) { return s.lx == s.rx; }

// where s lies against t, both crossing the sweep line just right of its
// position: -1 below, 1 above, 0 the same edge or a fly on it. The
// comparison uses the end of one that lies over the other.
static int side(const Item &s, const Item &t) {
    if (point(t) || (!point(s) && s.lx < t.lx)) return -side(t, s);
    long long tx = t.rx - t.lx, ty = t.ry - t.ly;
    long long c = tx * (s.ly - t.ly) - ty * (s.lx - t.lx);
    if (c == 0 && !point(s)) {
        // two edges of one polygon from a common left end
        c = tx * (s.ry - t.ly) - ty * (s.rx - t.lx);
    }
    return (c > 0) - (c < 0);
}

struct Below {
    bool operator()(const Item *s, const Item *t) const { return side(*s, *t) < 0; }
};

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<std::pair<long long, long long>> flies(n);
    for (auto &f : flies) scanf("%lld %lld", &f.first, &f.second);
    int m;
    scanf("%d", &m);
    std::map<std::pair<long long, long long>, int> corners;  // vertex -> polygon
    // x -> (low y, high y, polygon) of vertical edges
    std::unordered_map<long long, std::vector<std::tuple<long long, long long, int>>> upright;
    std::vector<Item> edges;
    for (int p = 0; p < m; p++) {
        int k;
        scanf("%d", &k);
        std::vector<long long> xs(k), ys(k);
        for (int i = 0; i < k; i++) scanf("%lld %lld", &xs[i], &ys[i]);
        for (int i = 0; i < k; i++) {
            long long ax = xs[(i + k - 1) % k], ay = ys[(i + k - 1) % k], bx = xs[i], by = ys[i];
            corners[{bx, by}] = p;
            if (ax == bx) {
                upright[ax].emplace_back(std::min(ay, by), std::max(ay, by), p);
                continue;
            }
            // counter-clockwise: the inside is left of the edge, so an edge
            // running right to left has the inside below it
            bool top = ax > bx;
            if (top) {
                edges.push_back({bx, by, ax, ay, p, true});
            } else {
                edges.push_back({ax, ay, bx, by, p, false});
            }
        }
    }
    for (auto &entry : upright) std::sort(entry.second.begin(), entry.second.end());
    int e = edges.size();
    std::vector<int> starts(e), ends(e), order(n);
    for (int i = 0; i < e; i++) starts[i] = ends[i] = i;
    for (int i = 0; i < n; i++) order[i] = i;
    auto byLeft = [&](int a, int b) { return edges[a].lx < edges[b].lx; };
    auto byRight = [&](int a, int b) { return edges[a].rx < edges[b].rx; };
    std::sort(starts.begin(), starts.end(), byLeft);
    std::sort(ends.begin(), ends.end(), byRight);
    std::sort(order.begin(), order.end(), [&](int a, int b) { return flies[a] < flies[b]; });
    std::set<const Item *, Below> active;
    std::vector<std::set<const Item *, Below>::iterator> where(e);
    std::vector<int> count(m, 0);
    int si = 0, ei = 0;
    for (int f : order) {
        long long x = flies[f].first, y = flies[f].second;
        // sweep every event column up to x; in a column, edges ending there
        // leave before edges starting there come in
        while (true) {
            long long column = x + 1;
            if (si < e) column = std::min(column, edges[starts[si]].lx);
            if (ei < e) column = std::min(column, edges[ends[ei]].rx);
            if (column > x) break;
            for (; ei < e && edges[ends[ei]].rx == column; ei++) active.erase(where[ends[ei]]);
            for (; si < e && edges[starts[si]].lx == column; si++) {
                where[starts[si]] = active.insert(&edges[starts[si]]).first;
            }
        }
        auto corner = corners.find({x, y});
        if (corner != corners.end()) {
            count[corner->second]++;
            continue;
        }
        auto spans = upright.find(x);
        if (spans != upright.end()) {
            const auto &list = spans->second;
            auto key = std::make_tuple(y, std::numeric_limits<long long>::max(), m);
            auto it = std::upper_bound(list.begin(), list.end(), key);
            if (it != list.begin() && std::get<1>(*std::prev(it)) >= y) {
                count[std::get<2>(*std::prev(it))]++;
                continue;
            }
        }
        Item fly = {x, y, x, y, -1, false};
        auto it = active.lower_bound(&fly);
        if (it != active.end() && ((*it)->top || side(fly, **it) == 0)) count[(*it)->polygon]++;
    }
    for (int c : count) printf("%d\n", c);
    return 0;
}
