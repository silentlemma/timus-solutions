#include <cstdio>
#include <vector>

const int FIELDS = 3;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<std::pair<int, int>>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a = 0, b = 0, c = 0;
        if (scanf("%d %d %d", &a, &b, &c) != FIELDS)
            return 0;
        adj[a].push_back({b, c});
        adj[b].push_back({a, c});
    }
    // an edge with s branches on one side carries the s (n - s) pairs that
    // it separates; sizes come from a parents-first order read backwards
    std::vector<int> parent(n + 1, 0), cost(n + 1, 0), order(1, 1);
    parent[1] = -1;
    for (size_t i = 0; i < order.size(); i++) {
        int v = order[i];
        for (const auto &e : adj[v])
            if (e.first != parent[v]) {
                parent[e.first] = v;
                cost[e.first] = e.second;
                order.push_back(e.first);
            }
    }
    std::vector<long long> size(n + 1, 1);
    long long total = 0;
    for (size_t i = order.size() - 1; i > 0; i--) {
        int v = order[i];
        size[parent[v]] += size[v];
        total += cost[v] * size[v] * (n - size[v]);
    }
    // every pair is counted in both directions
    printf("%.4f\n", 2.0 * (double)total / ((double)n * (n - 1)));
    return 0;
}
