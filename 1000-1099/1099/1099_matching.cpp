#include <cstdio>
#include <queue>
#include <set>
#include <vector>

int n;
std::vector<std::vector<int>> adj;
std::vector<int> match, parent, base;
std::vector<bool> used, blossom;

int lca(int a, int b) {
    std::vector<bool> seen(n, false);
    while (true) {
        a = base[a];
        seen[a] = true;
        if (match[a] < 0)
            break;
        a = parent[match[a]];
    }
    while (true) {
        b = base[b];
        if (seen[b])
            return b;
        b = parent[match[b]];
    }
}

void mark(int v, int b, int child) {
    while (base[v] != b) {
        blossom[base[v]] = blossom[base[match[v]]] = true;
        parent[v] = child;
        child = match[v];
        v = parent[match[v]];
    }
}

// Edmonds' search from an exposed vertex: an alternating tree whose odd
// cycles (blossoms) are shrunk into their base vertex
int find_path(int root) {
    used.assign(n, false);
    parent.assign(n, -1);
    for (int i = 0; i < n; i++)
        base[i] = i;
    used[root] = true;
    std::queue<int> queue;
    queue.push(root);
    while (!queue.empty()) {
        int v = queue.front();
        queue.pop();
        for (int to : adj[v]) {
            if (base[v] == base[to] || match[v] == to)
                continue;
            if (to == root || (match[to] >= 0 && parent[match[to]] >= 0)) {
                int b = lca(v, to);
                blossom.assign(n, false);
                mark(v, b, to);
                mark(to, b, v);
                for (int i = 0; i < n; i++)
                    if (blossom[base[i]]) {
                        base[i] = b;
                        if (!used[i]) {
                            used[i] = true;
                            queue.push(i);
                        }
                    }
            } else if (parent[to] < 0) {
                parent[to] = v;
                if (match[to] < 0)
                    return to;
                used[match[to]] = true;
                queue.push(match[to]);
            }
        }
    }
    return -1;
}

int main() {
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::set<int>> sets(n);
    for (int a, b; scanf("%d %d", &a, &b) == 2;)
        if (a != b && a >= 1 && a <= n && b >= 1 && b <= n) {
            sets[a - 1].insert(b - 1);
            sets[b - 1].insert(a - 1);
        }
    adj.resize(n);
    for (int v = 0; v < n; v++)
        adj[v].assign(sets[v].begin(), sets[v].end());
    match.assign(n, -1);
    base.resize(n);
    for (int v = 0; v < n; v++)
        if (match[v] < 0)
            for (int u : adj[v])
                if (match[u] < 0) {
                    match[u] = v, match[v] = u;
                    break;
                }
    for (int root = 0; root < n; root++)
        if (match[root] < 0 && !adj[root].empty())
            for (int v = find_path(root); v >= 0;) {
                int pv = parent[v], next = match[pv];
                match[v] = pv, match[pv] = v;
                v = next;
            }
    std::vector<std::pair<int, int>> pairs;
    for (int v = 0; v < n; v++)
        if (v < match[v])
            pairs.push_back({v + 1, match[v] + 1});
    printf("%d\n", 2 * (int)pairs.size());
    for (auto [a, b] : pairs)
        printf("%d %d\n", a, b);
}
