#include <algorithm>
#include <cstdio>
#include <vector>

std::vector<std::vector<int>> adj;

// distances from s and the predecessors on the shortest paths
void bfs(int s, std::vector<int> &dist, std::vector<int> &prev) {
    dist.assign(adj.size(), -1);
    prev.assign(adj.size(), 0);
    std::vector<int> queue = {s};
    dist[s] = 0;
    for (size_t i = 0; i < queue.size(); i++)
        for (int w : adj[queue[i]])
            if (dist[w] < 0) {
                dist[w] = dist[queue[i]] + 1;
                prev[w] = queue[i];
                queue.push_back(w);
            }
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    adj.assign(n + 1, {});
    for (int i = 2; i <= n; i++) {
        int p;
        if (scanf("%d", &p) != 1)
            return 0;
        adj[i].push_back(p);
        adj[p].push_back(i);
    }
    // the farthest computer from any start is an end of a longest path; the
    // farthest one from it is the other end
    std::vector<int> dist, prev;
    bfs(1, dist, prev);
    int u = std::max_element(dist.begin() + 1, dist.end()) - dist.begin();
    bfs(u, dist, prev);
    int v = std::max_element(dist.begin() + 1, dist.end()) - dist.begin();
    // the centers are the middle one or two computers of that path
    int length = dist[v];
    std::vector<int> centers;
    for (int k = 0, x = v; k <= length; k++, x = prev[x])
        if (k == length / 2 || k == (length + 1) / 2)
            centers.push_back(x);
    std::sort(centers.begin(), centers.end());
    centers.erase(std::unique(centers.begin(), centers.end()), centers.end());
    for (size_t i = 0; i < centers.size(); i++)
        printf(i ? " %d" : "%d", centers[i]);
    printf("\n");
}
