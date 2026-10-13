#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int SHORTEST = 3; // a route has at least three stops

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> adj(n, 0);
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        a--, b--;
        adj[a] |= 1 << b;
        adj[b] |= 1 << a;
    }

    // paths[mask][v]: simple paths from the lowest stop of mask through
    // all of mask, ending at v; a path that can close counts its cycle twice
    int full = (1 << n) - 1;
    vector<long long> paths((size_t)(full + 1) * n, 0), cycles(full + 1, 0);
    for (int s = 0; s < n; s++)
        paths[(size_t)(1 << s) * n + s] = 1;
    for (int mask = 1; mask <= full; mask++) {
        int low = mask & -mask, start = __builtin_ctz(mask);
        int free = ~mask & ~((low << 1) - 1) & full; // stops that may still join
        long long closing = 0;
        for (int v = 0; v < n; v++) {
            long long count = paths[(size_t)mask * n + v];
            if (!count)
                continue;
            if (adj[v] >> start & 1)
                closing += count;
            for (int step = adj[v] & free; step; step &= step - 1)
                paths[(size_t)(mask | (step & -step)) * n + __builtin_ctz(step)] += count;
        }
        if (__builtin_popcount(mask) >= SHORTEST)
            cycles[mask] = closing / 2;
    }

    // the bipartite graph of routes and stops needs as many rows as its
    // largest degree: the longest route or the busiest stop
    long long best = 0;
    vector<long long> through(n, 0);
    for (int mask = 1; mask <= full; mask++) {
        if (!cycles[mask])
            continue;
        best = max(best, (long long)__builtin_popcount(mask));
        for (int v = 0; v < n; v++)
            if (mask >> v & 1)
                through[v] += cycles[mask];
    }
    for (long long t : through)
        best = max(best, t);
    printf("%lld\n", best);
}
