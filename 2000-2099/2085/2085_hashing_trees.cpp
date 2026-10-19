#include <cstdint>
#include <cstdio>
#include <random>
#include <unordered_map>
#include <vector>

using namespace std;
typedef uint64_t u64;

constexpr u64 SEED = 31337;
constexpr int SPREAD = 31;

// spreads the random sums before hashing
struct Mix {
    size_t operator()(u64 x) const { return x ^ (x >> SPREAD); }
};
typedef unordered_map<u64, int, Mix> Table;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u - 1].push_back(v - 1);
        adj[v - 1].push_back(u - 1);
    }
    // every technology gets a random weight; a path uses each one exactly once
    // when (with overwhelming probability) its weights add up to the sum of all
    mt19937_64 rng(SEED);
    vector<u64> weight(m + 1);
    u64 goal = 0;
    for (int t = 1; t <= m; t++) goal += weight[t] = rng();
    vector<u64> own(n, 0);
    for (int v = 0; v < n; v++) {
        int a;
        scanf("%d", &a);
        for (int k = 0; k < a; k++) {
            int t;
            scanf("%d", &t);
            own[v] += weight[t];
        }
    }
    // depth[v]: the weights on the path from the root to v
    vector<int> parent(n, -1), order(1, 0);
    vector<u64> depth(n);
    depth[0] = own[0];
    for (size_t k = 0; k < order.size(); k++) {
        int v = order[k];
        for (int u : adj[v])
            if (u != parent[v]) parent[u] = v, depth[u] = depth[v] + own[u], order.push_back(u);
    }
    // small to large: below[v] maps depth -> a vertex of the subtree of v; two
    // vertices from different children of x (or x itself) join through x
    vector<Table*> below(n, nullptr);
    for (int k = n - 1; k >= 0; k--) {
        int x = order[k];
        if (own[x] == goal) {
            printf("%d %d\n", x + 1, x + 1);
            return 0;
        }
        Table* mine = new Table();
        (*mine)[depth[x]] = x;
        u64 target = goal + 2 * depth[x] - own[x];
        for (int y : adj[x]) {
            if (y == parent[x]) continue;
            Table* other = below[y];
            if (other->size() > mine->size()) swap(mine, other);
            for (auto& [d, u] : *other) {
                auto it = mine->find(target - d);
                if (it != mine->end()) {
                    printf("%d %d\n", u + 1, it->second + 1);
                    return 0;
                }
            }
            for (auto& entry : *other) mine->insert(entry);
            delete other;
        }
        below[x] = mine;
    }
    puts("No solution");
}
