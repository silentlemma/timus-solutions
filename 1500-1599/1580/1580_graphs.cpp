#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

struct Edge {
    int u, v;
    long long a;
};

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    vector<Edge> edges(m);
    vector<vector<pair<int, long long>>> adj(n);
    for (auto &e : edges) {
        if (scanf("%d %d", &e.u, &e.v) != 2 || scanf("%lld", &e.a) != 1)
            return 0;
        e.u--, e.v--;
        adj[e.u].push_back({e.v, e.a});
        adj[e.v].push_back({e.u, e.a});
    }
    // in halves of a rouble, each debt in a component is sign * t + base for
    // the debt t of its first student; an edge closing an odd cycle fixes t
    vector<long long> sign(n, 0), base(n, 0), twice(n, 0);
    for (int start = 0; start < n; start++) {
        if (sign[start])
            continue;
        sign[start] = 1;
        vector<int> comp = {start};
        bool fixed = false;
        long long t = 0;
        for (size_t head = 0; head < comp.size(); head++) {
            int v = comp[head];
            for (auto [u, a] : adj[v]) {
                if (!sign[u]) {
                    sign[u] = -sign[v], base[u] = 2 * a - base[v];
                    comp.push_back(u);
                } else if (sign[u] == sign[v] && !fixed) {
                    fixed = true;
                    t = (2 * a - base[u] - base[v]) / (2 * sign[v]);
                }
            }
        }
        if (!fixed) {
            // no odd cycle: one debt can move freely against its neighbours
            puts("IMPOSSIBLE");
            return 0;
        }
        for (int v : comp)
            twice[v] = sign[v] * t + base[v];
    }
    // the claims may also contradict each other
    for (auto &e : edges)
        if (twice[e.u] + twice[e.v] != 2 * e.a) {
            puts("IMPOSSIBLE");
            return 0;
        }
    for (long long t : twice)
        printf("%s%lld.%s\n", t < 0 ? "-" : "", llabs(t) / 2, llabs(t) % 2 ? "50" : "00");
}
