#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

int width;
vector<long long> tree;

// the largest level at the places lo to hi of the chains
long long segMax(int lo, int hi) {
    long long best = 0;
    for (lo += width, hi += width + 1; lo < hi; lo >>= 1, hi >>= 1) {
        if (lo & 1)
            best = max(best, tree[lo++]);
        if (hi & 1)
            best = max(best, tree[--hi]);
    }
    return best;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        if (scanf("%d %d", &a, &b) != 2)
            return 0;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // heavy-light decomposition: every cave's heavy child continues its chain,
    // and the chains lie consecutively in one segment tree of maxima
    vector<int> parent(n + 1, 0), depth(n + 1, 0), order = {1};
    parent[1] = -1;
    for (size_t i = 0; i < order.size(); i++) {
        int v = order[i];
        for (int u : adj[v])
            if (u != parent[v]) {
                parent[u] = v;
                depth[u] = depth[v] + 1;
                order.push_back(u);
            }
    }
    vector<int> size(n + 1, 1), heavy(n + 1, 0);
    for (int i = n - 1; i > 0; i--) {
        int v = order[i], p = parent[v];
        size[p] += size[v];
        if (heavy[p] == 0 || size[v] > size[heavy[p]])
            heavy[p] = v;
    }
    vector<int> head(n + 1), index(n + 1);
    int next = 0;
    for (int v : order)
        if (v == 1 || heavy[parent[v]] != v)
            for (int u = v; u; u = heavy[u]) {
                head[u] = v;
                index[u] = next++;
            }
    width = 1;
    while (width < n)
        width *= 2;
    tree.assign(2 * width, 0);
    int q;
    if (scanf("%d", &q) != 1)
        return 0;
    for (int i = 0; i < q; i++) {
        char kind;
        int u, v;
        if (scanf(" %c", &kind) != 1 || scanf("%d %d", &u, &v) != 2)
            return 0;
        if (kind == 'I') {
            int at = index[u] + width;
            tree[at] += v;
            for (at >>= 1; at; at >>= 1)
                tree[at] = max(tree[2 * at], tree[2 * at + 1]);
            continue;
        }
        long long best = 0;
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]])
                swap(u, v);
            best = max(best, segMax(index[head[u]], index[u]));
            u = parent[head[u]];
        }
        best = max(best, segMax(min(index[u], index[v]), max(index[u], index[v])));
        printf("%lld\n", best);
    }
}
