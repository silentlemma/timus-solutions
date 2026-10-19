#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> Point;

// drop repeated points and points in the middle of a straight run
vector<Point> straighten(const vector<Point>& points) {
    vector<Point> out;
    for (const Point& p : points) {
        if (!out.empty() && out.back() == p) continue;
        while (out.size() >= 2) {
            const Point& a = out[out.size() - 2];
            const Point& b = out.back();
            bool same_x = a.first == b.first && b.first == p.first;
            bool same_y = a.second == b.second && b.second == p.second;
            if (!same_x && !same_y) break;
            out.pop_back();
        }
        out.push_back(p);
    }
    return out;
}

int main() {
    ll w, h, x, y, d;
    if (scanf("%lld %lld %lld %lld %lld", &w, &h, &x, &y, &d) == EOF) return 0;
    ll half = w * h / 2;
    // Finland always holds the column of cells along its coast, the
    // lighthouse, and a corridor of cells from the lighthouse to that column
    ll right = w - 1 - x - d;
    if (h + d * d + right > half) {
        puts("Impossible");
        return 0;
    }
    vector<Point> points;
    if (h + d * (w - 1 - x) <= half) {
        // every row of Finland runs from some column to the coast; the area
        // still missing pushes rows west from the top down
        ll extra = half - (h + d * (w - 1 - x));
        vector<pair<ll, ll>> cuts;  // (rows, column) from the top down
        struct Band {
            ll top, bottom, column;
        };
        Band bands[] = {{h, y + d, w - 1}, {y + d, y, x}, {y, 0, w - 1}};
        for (const Band& band : bands) {
            ll rows = band.top - band.bottom, column = band.column;
            if (rows == 0) continue;
            ll full = column > 1 ? min(rows, extra / (column - 1)) : 0;
            extra -= full * (column - 1);
            if (full) cuts.push_back({full, 1});
            if (full < rows) {
                ll part = min(extra, column - 1);
                extra -= part;
                cuts.push_back({1, column - part});
                if (full + 1 < rows) cuts.push_back({rows - full - 1, column});
            }
        }
        ll level = h;
        points.push_back({cuts[0].second, h});
        for (auto& cut : cuts) {
            points.push_back({cut.second, level});
            points.push_back({cut.second, level - cut.first});
            level -= cut.first;
        }
    } else {
        // the border goes round the lighthouse: Finland takes full corridor
        // rows at the top of the lighthouse rows and part of one more row
        ll rest = half - (h + d * d + right);
        ll more = rest / right, part = rest % right;
        ll level = y + d - 1 - more;
        points = {{w - 1, h}, {w - 1, y + d}, {x, y + d}, {x, y}, {x + d, y}, {x + d, level},
                  {w - 1 - part, level}, {w - 1 - part, level - 1}, {w - 1, level - 1},
                  {w - 1, 0}};
    }
    points = straighten(points);
    printf("%d\n", (int)points.size());
    for (const Point& p : points) printf("%lld %lld\n", p.first, p.second);
    return 0;
}
