#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;

const uint64_t GOLDEN = 0x9E3779B97F4A7C15ULL;
const uint64_t MIX1 = 0xBF58476D1CE4E5B9ULL, MIX2 = 0x94D049BB133111EBULL;
const int SHIFT1 = 30, SHIFT2 = 27, SHIFT3 = 31;

// a splitmix64 step: well-spread 64-bit labels from a counter
uint64_t mix(uint64_t x) {
    x += GOLDEN;
    x = (x ^ (x >> SHIFT1)) * MIX1;
    x = (x ^ (x >> SHIFT2)) * MIX2;
    return x ^ (x >> SHIFT3);
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    vector<int> from(m), to(m);
    vector<vector<pair<int, int>>> adj(n);
    for (int e = 0; e < m; e++) {
        if (scanf("%d %d", &from[e], &to[e]) != 2)
            return 0;
        from[e]--, to[e]--;
        adj[from[e]].push_back({to[e], e});
        adj[to[e]].push_back({from[e], e});
    }
    // a spanning tree in breadth-first order
    vector<int> parent(n, -1), parentEdge(n, -1), order = {0};
    vector<bool> seen(n, false), inTree(m, false);
    seen[0] = true;
    for (size_t i = 0; i < order.size(); i++)
        for (auto [u, e] : adj[order[i]])
            if (!seen[u]) {
                seen[u] = true;
                parent[u] = order[i], parentEdge[u] = e, inTree[e] = true;
                order.push_back(u);
            }
    // every other channel gets a random label; a tree channel gets the XOR
    // of the labels of the channels whose cycles pass through it, which is
    // the XOR over the subtree below it
    vector<uint64_t> label(m, 0), below(n, 0);
    for (int e = 0; e < m; e++)
        if (!inTree[e]) {
            label[e] = mix(e);
            below[from[e]] ^= label[e];
            below[to[e]] ^= label[e];
        }
    for (int i = n - 1; i > 0; i--) {
        int v = order[i];
        label[parentEdge[v]] = below[v];
        below[parent[v]] ^= below[v];
    }
    // a bridge (label 0) cuts with any other channel; two other channels cut
    // together exactly when no cycle passes through just one of them
    sort(label.begin(), label.end());
    long long bridges = count(label.begin(), label.end(), 0ULL), rest = m - bridges;
    long long total = (long long)m * (m - 1) / 2 - rest * (rest - 1) / 2;
    for (long long i = bridges, j = bridges; i < m; i = j) {
        while (j < m && label[j] == label[i])
            j++;
        total += (j - i) * (j - i - 1) / 2;
    }
    printf("%lld\n", total);
}
