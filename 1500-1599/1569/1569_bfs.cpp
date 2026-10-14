#include <algorithm>
#include <cstdio>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

int n, m;
vector<vector<int>> adj;

// distances from the nearest source and the edges of a tree of shortest
// paths that grows from the sources
vector<int> bfs(const vector<int> &sources, vector<pair<int, int>> &tree) {
    vector<int> dist(n, -1);
    queue<int> q;
    for (int s : sources) {
        dist[s] = 0;
        q.push(s);
    }
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : adj[v])
            if (dist[u] < 0) {
                dist[u] = dist[v] + 1;
                tree.push_back({v, u});
                q.push(u);
            }
    }
    return dist;
}

int main() {
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    adj.assign(n, {});
    vector<pair<int, int>> edges(m), unused;
    for (auto &e : edges) {
        if (scanf("%d %d", &e.first, &e.second) != 2)
            return 0;
        e.first--, e.second--;
        adj[e.first].push_back(e.second);
        adj[e.second].push_back(e.first);
    }
    vector<vector<int>> dist(n);
    for (int v = 0; v < n; v++)
        dist[v] = bfs({v}, unused);
    // the middle of a tree of least diameter is a node or the middle of an edge, and
    // a tree of shortest paths from there has diameter 2 r or 2 r + 1 for the
    // largest distance r from it, and no tree can do better
    int best = -1;
    vector<int> centre;
    for (int v = 0; v < n; v++) {
        int reach = 2 * *max_element(dist[v].begin(), dist[v].end());
        if (best < 0 || reach < best)
            best = reach, centre = {v};
    }
    for (auto &e : edges) {
        int far = 0;
        for (int w = 0; w < n; w++)
            far = max(far, min(dist[e.first][w], dist[e.second][w]));
        if (2 * far + 1 < best)
            best = 2 * far + 1, centre = {e.first, e.second};
    }
    vector<pair<int, int>> tree;
    bfs(centre, tree);
    if (centre.size() > 1)
        tree.push_back({centre[0], centre[1]});
    for (auto &e : tree)
        printf("%d %d\n", e.first + 1, e.second + 1);
}
