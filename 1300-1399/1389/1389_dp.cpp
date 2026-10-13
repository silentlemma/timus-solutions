#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<int> a(m), b(m);
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &a[i], &b[i]);
        adj[a[i]].push_back(i);
        adj[b[i]].push_back(i);
    }
    // breadth-first order from city 1 with the road to each parent
    vector<int> parent(n + 1, 0), up(n + 1, -1), order = {1};
    parent[1] = -1;
    for (size_t k = 0; k < order.size(); k++) {
        int v = order[k];
        for (int e : adj[v]) {
            int u = a[e] + b[e] - v;
            if (u != parent[v]) {
                parent[u] = v;
                up[u] = e;
                order.push_back(u);
            }
        }
    }
    // leaves first: close the road to the parent while both ends are free
    vector<bool> used(n + 1, false), chosen(m, false);
    int count = 0;
    for (int k = n - 1; k >= 0; k--) {
        int v = order[k];
        if (up[v] >= 0 && !used[v] && !used[parent[v]]) {
            used[v] = used[parent[v]] = true;
            chosen[up[v]] = true;
            count++;
        }
    }
    printf("%d\n", count);
    for (int i = 0; i < m; i++)
        if (chosen[i])
            printf("%d %d\n", a[i], b[i]);
}
