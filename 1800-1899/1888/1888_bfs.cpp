#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int LONGEST = 50;  // experience is from 1 to 50 years

int p;
vector<vector<int>> adj;

// distances from start, -1 outside its component
vector<int> distances(int start) {
    vector<int> dist(p + 1, -1);
    vector<int> queue = {start};
    dist[start] = 0;
    for (size_t head = 0; head < queue.size(); head++) {
        int u = queue[head];
        for (int v : adj[u]) {
            if (dist[v] < 0) {
                dist[v] = dist[u] + 1;
                queue.push_back(v);
            }
        }
    }
    return dist;
}

int main() {
    int n;
    if (scanf("%d %d", &n, &p) != 2) return 0;
    adj.assign(p + 1, {});
    for (int k = 0; k < n; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // the two pilots of a flight differ by exactly one year, so a component
    // must be bipartite; within it no two pilots differ by more than their
    // distance, and BFS layers from one end of a diameter reach it
    vector<int> comp(p + 1, -1);
    vector<int> roots;
    for (int s = 1; s <= p; s++) {
        if (comp[s] >= 0) continue;
        vector<int> dist = distances(s);
        for (int u = 1; u <= p; u++) {
            if (dist[u] < 0) continue;
            comp[u] = roots.size();
            for (int v : adj[u]) {
                if ((dist[u] - dist[v]) % 2 == 0) {
                    puts("-1");
                    return 0;
                }
            }
        }
        roots.push_back(s);
    }
    vector<int> years(p + 1);
    if (roots.size() == 1) {
        int spread = -1;
        for (int s = 1; s <= p; s++) {
            vector<int> dist = distances(s);
            int far = 0;
            for (int u = 1; u <= p; u++) far = max(far, dist[u]);
            if (far > spread) {
                spread = far;
                for (int u = 1; u <= p; u++) years[u] = 1 + dist[u];
            }
        }
        printf("%d\n", spread);
    } else {
        // separate groups: one alternates 1 and 2, the others 49 and 50
        for (size_t k = 0; k < roots.size(); k++) {
            vector<int> dist = distances(roots[k]);
            for (int u = 1; u <= p; u++) {
                if (dist[u] < 0) continue;
                years[u] = k == 0 ? 1 + dist[u] % 2 : LONGEST - dist[u] % 2;
            }
        }
        printf("%d\n", LONGEST - 1);
    }
    for (int u = 1; u <= p; u++) printf("%d%c", years[u], u < p ? ' ' : '\n');
    return 0;
}
