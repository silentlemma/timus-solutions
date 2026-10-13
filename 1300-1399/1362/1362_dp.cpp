#include <algorithm>
#include <cstdio>
#include <functional>
#include <vector>

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> adj(n + 1);
    for (int boss = 1; boss <= n; boss++) {
        int v = 0;
        while (scanf("%d", &v) == 1 && v != 0) {
            adj[boss].push_back(v);
            adj[v].push_back(boss);
        }
    }
    int root = 0;
    if (scanf("%d", &root) != 1)
        return 0;
    // calls go both up and down, so the news spreads over the tree rooted
    // at Tanya; order parents before children
    std::vector<int> parent(n + 1, 0), order(1, root);
    parent[root] = -1;
    for (size_t i = 0; i < order.size(); i++) {
        int v = order[i];
        for (int u : adj[v])
            if (u != parent[v]) {
                parent[u] = v;
                order.push_back(u);
            }
    }
    // the time of v is what it needs to tell its whole subtree; the slowest
    // subtrees are called first, the i-th call starting at minute i
    std::vector<int> time(n + 1, 0);
    std::vector<std::vector<int>> kids(n + 1);
    for (size_t i = order.size(); i-- > 0;) {
        int v = order[i];
        std::sort(kids[v].begin(), kids[v].end(), std::greater<int>());
        for (size_t j = 0; j < kids[v].size(); j++)
            time[v] = std::max(time[v], kids[v][j] + (int)j + 1);
        if (parent[v] > 0)
            kids[parent[v]].push_back(time[v]);
    }
    printf("%d\n", time[root]);
    return 0;
}
