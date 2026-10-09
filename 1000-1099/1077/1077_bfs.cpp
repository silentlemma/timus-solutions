#include <cstdio>
#include <queue>
#include <string>
#include <utility>
#include <vector>

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<std::pair<int, int>> ends(m);
    std::vector<std::vector<std::pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &ends[i].first, &ends[i].second);
        adj[ends[i].first].push_back({ends[i].second, i});
        adj[ends[i].second].push_back({ends[i].first, i});
    }
    std::vector<int> parent(n + 1, 0), depth(n + 1, -1);
    std::vector<bool> tree(m, false);
    // a breadth-first forest keeps the tree paths, and so the tours, short
    for (int root = 1; root <= n; root++) {
        if (depth[root] >= 0)
            continue;
        depth[root] = 0;
        std::queue<int> queue;
        queue.push(root);
        while (!queue.empty()) {
            int u = queue.front();
            queue.pop();
            for (auto [v, i] : adj[u])
                if (depth[v] < 0) {
                    depth[v] = depth[u] + 1;
                    parent[v] = u;
                    tree[i] = true;
                    queue.push(v);
                }
        }
    }
    std::string out;
    int count = 0;
    // every road outside the forest closes its own tour with the tree path
    for (int i = 0; i < m; i++) {
        if (tree[i])
            continue;
        auto [a, b] = ends[i];
        std::vector<int> left, right;
        while (depth[a] > depth[b])
            left.push_back(a), a = parent[a];
        while (depth[b] > depth[a])
            right.push_back(b), b = parent[b];
        while (a != b) {
            left.push_back(a), right.push_back(b);
            a = parent[a], b = parent[b];
        }
        left.push_back(a);
        left.insert(left.end(), right.rbegin(), right.rend());
        out += std::to_string(left.size());
        for (int c : left)
            out += " " + std::to_string(c);
        out += "\n";
        count++;
    }
    printf("%d\n%s", count, out.c_str());
}
