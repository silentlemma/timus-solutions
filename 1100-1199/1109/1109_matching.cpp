#include <cstdio>
#include <queue>
#include <vector>

// Hopcroft-Karp: BFS layers from the free left vertices, then vertex-disjoint
// shortest augmenting paths along the layers
struct Matching {
    int m, n;
    std::vector<std::vector<int>> adj;
    std::vector<int> match_l, match_r, dist, it;

    Matching(int m, int n) : m(m), n(n), adj(m), match_l(m, -1), match_r(n, -1) {}

    bool layer() {
        dist.assign(m, -1);
        std::queue<int> queue;
        for (int v = 0; v < m; v++)
            if (match_l[v] < 0) {
                dist[v] = 0;
                queue.push(v);
            }
        bool found = false;
        while (!queue.empty()) {
            int v = queue.front();
            queue.pop();
            for (int u : adj[v]) {
                int w = match_r[u];
                if (w < 0)
                    found = true;
                else if (dist[w] < 0) {
                    dist[w] = dist[v] + 1;
                    queue.push(w);
                }
            }
        }
        return found;
    }

    bool augment(int v) {
        for (; it[v] < (int)adj[v].size(); it[v]++) {
            int u = adj[v][it[v]], w = match_r[u];
            if (w < 0 || (dist[w] == dist[v] + 1 && augment(w))) {
                match_l[v] = u;
                match_r[u] = v;
                return true;
            }
        }
        dist[v] = -1;
        return false;
    }

    int run() {
        int size = 0;
        while (layer()) {
            it.assign(m, 0);
            for (int v = 0; v < m; v++)
                if (match_l[v] < 0 && augment(v))
                    size++;
        }
        return size;
    }
};

int main() {
    int m, n, k;
    if (scanf("%d %d", &m, &n) != 2 || scanf("%d", &k) != 1)
        return 0;
    Matching g(m, n);
    for (int i = 0; i < k; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        g.adj[a - 1].push_back(b - 1);
    }
    // a minimum edge cover takes a maximum matching and one more edge for
    // every vertex the matching leaves uncovered
    printf("%d\n", m + n - g.run());
}
