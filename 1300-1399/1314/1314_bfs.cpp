#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>

const int IDS = 32768; // station indices go up to 32767

std::vector<int> adj[IDS];
bool present[IDS];

std::vector<int> bfs(int start) {
    std::vector<int> dist(IDS, -1);
    std::queue<int> queue;
    dist[start] = 0;
    queue.push(start);
    while (!queue.empty()) {
        int u = queue.front();
        queue.pop();
        for (int v : adj[u]) {
            if (dist[v] < 0) {
                dist[v] = dist[u] + 1;
                queue.push(v);
            }
        }
    }
    return dist;
}

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int i = 0; i < n; i++) {
        int k = 0;
        if (scanf("%d", &k) != 1)
            return 0;
        std::vector<int> line(k);
        for (int &s : line) {
            if (scanf("%d", &s) != 1)
                return 0;
            present[s] = true;
        }
        for (int j = 0; j + 1 < k; j++) {
            adj[line[j]].push_back(line[j + 1]);
            adj[line[j + 1]].push_back(line[j]);
        }
    }
    int m = 0;
    if (scanf("%d", &m) != 1)
        return 0;
    std::vector<int> seen(m);
    for (int &s : seen) {
        if (scanf("%d", &s) != 1)
            return 0;
    }
    // the stations seen must be a walk through the network ...
    for (int i = 0; i < m; i++) {
        if (seen[i] < 0 || seen[i] >= IDS || !present[seen[i]])
            return 0;
        const std::vector<int> &prev = adj[seen[i > 0 ? i - 1 : 0]];
        if (i > 0 && std::find(prev.begin(), prev.end(), seen[i]) == prev.end())
            return 0;
    }
    std::vector<int> first = bfs(seen[0]);
    // ... and a shortest one, or no target fits it
    if (first[seen[m - 1]] != m - 1)
        return 0;
    std::vector<int> last = bfs(seen[m - 1]);
    // a target fits when the walk can go on to it along a shortest path
    for (int t = 0; t < IDS; t++) {
        if (first[t] >= 0 && last[t] >= 0 && first[t] == m - 1 + last[t])
            printf("%d\n", t);
    }
    return 0;
}
