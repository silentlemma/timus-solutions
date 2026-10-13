#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

vector<int> parent;

int find(int v) {
    while (parent[v] != v)
        v = parent[v] = parent[parent[v]];
    return v;
}

int main() {
    int k;
    scanf("%d", &k);
    vector<long long> x(k), y(k), z(k), r(k);
    for (int i = 0; i < k; i++)
        scanf("%lld %lld %lld %lld", &x[i], &y[i], &z[i], &r[i]);
    parent.resize(k);
    iota(parent.begin(), parent.end(), 0);
    // two balls share more than one point when the centres are closer than r1 + r2
    for (int i = 0; i < k; i++)
        for (int j = i + 1; j < k; j++) {
            long long dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j];
            if (dx * dx + dy * dy + dz * dz < (r[i] + r[j]) * (r[i] + r[j]))
                parent[find(j)] = find(i);
        }
    // each group lists its planets in order, and groups come by their first planet
    vector<vector<int>> groups(k);
    for (int v = 0; v < k; v++)
        groups[find(v)].push_back(v);
    sort(groups.begin(), groups.end());
    for (auto &g : groups) {
        if (g.empty())
            continue;
        for (size_t i = 0; i < g.size(); i++)
            printf(i ? ", %d" : "%d", g[i]);
        printf("\n");
    }
}
