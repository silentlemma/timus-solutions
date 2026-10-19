#include <algorithm>
#include <cmath>
#include <cstdio>
#include <limits>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<double> xs(n), ys(n);
    for (int i = 0; i < n; i++) scanf("%lf %lf", &xs[i], &ys[i]);
    std::vector<std::vector<int>> adjacent(n);
    for (int k = 0; k < n - 1; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        adjacent[a - 1].push_back(b - 1);
        adjacent[b - 1].push_back(a - 1);
    }
    std::vector<int> order = {0}, parent(n, -1);
    for (size_t i = 0; i < order.size(); i++) {
        int u = order[i];
        for (int v : adjacent[u]) {
            if (v != parent[u]) {
                parent[v] = u;
                order.push_back(v);
            }
        }
    }
    auto far = [&](int a, int b) { return std::hypot(xs[a] - xs[b], ys[a] - ys[b]); };
    const double INF = std::numeric_limits<double>::infinity();
    // the walk through a subtree starts at its root and ends at one of its
    // leaves: ends[u] lists them, cost[u] the shortest walk ending at each
    std::vector<std::vector<int>> ends(n);
    std::vector<std::vector<double>> cost(n);
    for (int i = n - 1; i >= 0; i--) {
        int u = order[i];
        std::vector<int> children;
        for (int v : adjacent[u]) {
            if (v != parent[u]) children.push_back(v);
        }
        if (children.empty()) {
            ends[u] = {u};
            cost[u] = {0.0};
            continue;
        }
        int k = children.size();
        // link[a][b]: leave child a at its best end and fly to child b
        std::vector<std::vector<double>> link(k, std::vector<double>(k, INF));
        for (int a = 0; a < k; a++) {
            const auto &e = ends[children[a]];
            const auto &c = cost[children[a]];
            for (int b = 0; b < k; b++) {
                for (size_t j = 0; j < e.size(); j++) {
                    link[a][b] = std::min(link[a][b], c[j] + far(e[j], children[b]));
                }
            }
        }
        // enter[m][b]: the children in mask m are done and b, in m, came last
        std::vector<std::vector<double>> enter(1 << k, std::vector<double>(k, INF));
        for (int b = 0; b < k; b++) enter[1 << b][b] = far(u, children[b]);
        for (int m = 1; m < (1 << k); m++) {
            for (int a = 0; a < k; a++) {
                if (enter[m][a] == INF) continue;
                for (int b = 0; b < k; b++) {
                    if (m >> b & 1) continue;
                    double &next = enter[m | 1 << b][b];
                    next = std::min(next, enter[m][a] + link[a][b]);
                }
            }
        }
        const auto &full = enter[(1 << k) - 1];
        for (int b = 0; b < k; b++) {
            int v = children[b];
            for (size_t j = 0; j < ends[v].size(); j++) {
                ends[u].push_back(ends[v][j]);
                cost[u].push_back(full[b] + cost[v][j]);
            }
            ends[v].clear();
            cost[v].clear();
        }
    }
    double best = INF;
    for (size_t j = 0; j < ends[0].size(); j++) {
        best = std::min(best, cost[0][j] + far(ends[0][j], 0));
    }
    printf("%.10f\n", best);
    return 0;
}
