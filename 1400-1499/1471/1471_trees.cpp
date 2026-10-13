#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> us(n - 1), vs(n - 1), ws(n - 1), start(n + 1, 0);
    for (int i = 0; i + 1 < n; i++) {
        scanf("%d %d %d", &us[i], &vs[i], &ws[i]);
        start[us[i] + 1]++;
        start[vs[i] + 1]++;
    }
    // adjacency lists packed into one array (both directions of each edge)
    for (int i = 0; i < n; i++)
        start[i + 1] += start[i];
    vector<int> fill(start.begin(), start.end() - 1), adj(2 * (n - 1)), weight(2 * (n - 1));
    for (int i = 0; i + 1 < n; i++) {
        adj[fill[us[i]]] = vs[i], weight[fill[us[i]]++] = ws[i];
        adj[fill[vs[i]]] = us[i], weight[fill[vs[i]]++] = ws[i];
    }

    // Euler tour from vertex 0: a vertex is written on entry and after each child
    vector<int> parent(n, -1), depth(n, 0), dist(n, 0), first(n, 0), tour = {0};
    vector<int> pointer(start.begin(), start.end() - 1), stack = {0};
    while (!stack.empty()) {
        int v = stack.back();
        int p = pointer[v];
        if (p < start[v + 1]) {
            pointer[v]++;
            int u = adj[p];
            if (u == parent[v])
                continue;
            parent[u] = v;
            depth[u] = depth[v] + 1;
            dist[u] = dist[v] + weight[p];
            first[u] = tour.size();
            tour.push_back(u);
            stack.push_back(u);
        } else {
            stack.pop_back();
            if (!stack.empty())
                tour.push_back(stack.back());
        }
    }

    // sparse table: the shallowest vertex of each run of 2^k tour entries
    int len = tour.size();
    vector<vector<int>> table = {tour};
    for (int span = 1; 2 * span <= len; span *= 2) {
        const vector<int> &prev = table.back();
        vector<int> level(len - 2 * span + 1);
        for (int i = 0; i < (int)level.size(); i++) {
            int a = prev[i], b = prev[i + span];
            level[i] = depth[a] <= depth[b] ? a : b;
        }
        table.push_back(level);
    }

    int m;
    scanf("%d", &m);
    while (m--) {
        int a, b;
        scanf("%d %d", &a, &b);
        int lo = first[a], hi = first[b];
        if (lo > hi)
            swap(lo, hi);
        int k = __lg(hi - lo + 1);
        int x = table[k][lo], y = table[k][hi - (1 << k) + 1];
        int lca = depth[x] <= depth[y] ? x : y;
        printf("%d\n", dist[a] + dist[b] - 2 * dist[lca]);
    }
}
