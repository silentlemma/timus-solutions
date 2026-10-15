#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const int MAX_CLIQUE = 4;  // four points pairwise 1 apart fit in space, five do not

vector<int> parent;

int find(int v) {
    while (parent[v] != v)
        v = parent[v] = parent[parent[v]];
    return v;
}

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    parent.resize(n);
    for (int v = 0; v < n; v++)
        parent[v] = v;
    vector<int> degree(n), ends(m);
    for (int i = 0; i < m; i++) {
        int u, v;
        if (scanf("%d %d", &u, &v) != 2)
            return 0;
        u--, v--;
        degree[u]++, degree[v]++;
        ends[i] = u;
        parent[find(u)] = find(v);
    }
    vector<int> size(n), edges(n), widest(n);
    for (int v = 0; v < n; v++) {
        int root = find(v);
        size[root]++;
        widest[root] = max(widest[root], degree[v]);
    }
    for (int u : ends)
        edges[find(u)]++;
    // every component must be a path or a clique of at most four vertices
    for (int root = 0; root < n; root++) {
        int k = size[root];
        if (!k)
            continue;
        bool path = edges[root] == k - 1 && widest[root] <= 2;
        bool clique = edges[root] == k * (k - 1) / 2 && k <= MAX_CLIQUE;
        if (!path && !clique) {
            puts("Unlucky Petr");
            return 0;
        }
    }
    puts("Luck is possible");
}
