#include <cstdio>
#include <vector>

int n;
std::vector<std::vector<int>> adj;
std::vector<int> matchLeft, matchRight, stamp;
int round_ = 0;

// Kuhn's augmenting search on the doubled graph: left copies and right
// copies of the canoeists, adj[u] the right neighbours of left u
bool augment(int u) {
    for (int v : adj[u]) {
        if (stamp[v] == round_) continue;
        stamp[v] = round_;
        if (matchRight[v] < 0 || augment(matchRight[v])) {
            matchLeft[u] = v;
            matchRight[v] = u;
            return true;
        }
    }
    return false;
}

int main() {
    int k, m;
    if (scanf("%d %d %d", &n, &k, &m) < 1) return 0;
    adj.assign(n, {});
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        adj[a - 1].push_back(b - 1);
        adj[b - 1].push_back(a - 1);
    }
    // each crew must get at least k between its two members; this linear
    // program has a half-integral optimum, k/2 for each copy of a canoeist
    // in a minimum vertex cover of the doubled bipartite graph
    matchLeft.assign(n, -1);
    matchRight.assign(n, -1);
    stamp.assign(n, -1);
    for (int u = 0; u < n; u++, round_++) augment(u);
    // Konig: left copies unreachable from free left copies by alternating
    // paths, and right copies reachable, form a minimum cover
    std::vector<bool> seenLeft(n, false), seenRight(n, false);
    std::vector<int> queue;
    for (int u = 0; u < n; u++) {
        if (matchLeft[u] < 0) {
            seenLeft[u] = true;
            queue.push_back(u);
        }
    }
    for (size_t i = 0; i < queue.size(); i++) {
        for (int v : adj[queue[i]]) {
            if (seenRight[v]) continue;
            seenRight[v] = true;
            int w = matchRight[v];
            if (w >= 0 && !seenLeft[w]) {
                seenLeft[w] = true;
                queue.push_back(w);
            }
        }
    }
    for (int v = 0; v < n; v++) {
        int copies = !seenLeft[v] + seenRight[v];
        printf("%.1f\n", copies * k / 2.0);
    }
    return 0;
}
