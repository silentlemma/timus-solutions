#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

typedef long long ll;

struct P {
    ll x, y;
};

ll cross(P o, P a, P b) { return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x); }

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<P> towers(n), monuments(m);
    for (auto &p : towers)
        if (scanf("%lld %lld", &p.x, &p.y) != 2)
            return 0;
    for (auto &p : monuments)
        if (scanf("%lld %lld", &p.x, &p.y) != 2)
            return 0;
    std::vector<std::vector<double>> dist(n, std::vector<double>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            dist[i][j] = std::hypot((double)(towers[i].x - towers[j].x),
                                    (double)(towers[i].y - towers[j].y));
    const double inf = 1e18;
    double best = inf;
    if (m == 0) {
        // any convex border contains a triangle of its towers that is not
        // longer, so the best border is the shortest triangle with an area
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    if (cross(towers[i], towers[j], towers[k]) != 0)
                        best = std::min(best, dist[i][j] + dist[j][k] + dist[k][i]);
    } else {
        // the border goes clockwise, so the inside is on the right of every
        // side: a side i -> j may be used when all monuments are strictly right
        std::vector<std::vector<bool>> ok(n, std::vector<bool>(n, false));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                if (i == j)
                    continue;
                bool all = true;
                for (const P &p : monuments)
                    if (cross(towers[i], towers[j], p) >= 0) {
                        all = false;
                        break;
                    }
                ok[i][j] = all;
            }
        // a monument inside rules out degenerate borders; from every first
        // tower, the shortest way around through towers in their order
        for (int s = 0; s < n; s++) {
            std::vector<double> way(n, inf);
            way[s] = 0;
            for (int step = 1; step < n; step++) {
                int k = (s + step) % n;
                for (int back = 0; back < step; back++) {
                    int j = (s + back) % n;
                    if (ok[j][k])
                        way[k] = std::min(way[k], way[j] + dist[j][k]);
                }
                if (ok[k][s])
                    best = std::min(best, way[k] + dist[k][s]);
            }
        }
    }
    printf("%.2f\n", best);
}
