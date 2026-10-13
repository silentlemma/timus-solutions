#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const int INF = 1 << 30;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> w(n, vector<int>(n, INF));
    vector<int> ea(m), eb(m), ec(m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &ea[i], &eb[i], &ec[i]);
        ea[i]--, eb[i]--;
        w[ea[i]][eb[i]] = w[eb[i]][ea[i]] = ec[i];
    }
    // Prim on the matrix; heaviest[u][v] is the heaviest tree edge between u and v
    vector<vector<int>> heaviest(n, vector<int>(n, 0));
    vector<vector<bool>> inTree(n, vector<bool>(n, false));
    vector<int> dist = w[0], parent(n, 0), order = {0};
    vector<bool> done(n, false);
    done[0] = true;
    long long total = 0;
    for (int step = 1; step < n; step++) {
        int v = -1;
        for (int u = 0; u < n; u++)
            if (!done[u] && (v < 0 || dist[u] < dist[v]))
                v = u;
        int p = parent[v], c = dist[v];
        total += c;
        inTree[p][v] = inTree[v][p] = true;
        for (int u : order)
            heaviest[u][v] = heaviest[v][u] = max(heaviest[p][u], c);
        done[v] = true;
        order.push_back(v);
        for (int u = 0; u < n; u++)
            if (!done[u] && w[v][u] < dist[u])
                dist[u] = w[v][u], parent[u] = v;
    }
    // the next tree swaps one outside edge for the heaviest edge on its tree path
    long long swap = INF;
    for (int i = 0; i < m; i++)
        if (!inTree[ea[i]][eb[i]])
            swap = min(swap, (long long)ec[i] - heaviest[ea[i]][eb[i]]);
    printf("Cost: %lld\n", total);
    printf("Cost: %lld\n", swap == INF ? -1 : total + swap);
}
