#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int, int>>> out(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        out[a].push_back({b, c});
        indeg[b]++;
    }
    int s, f;
    scanf("%d %d", &s, &f);
    // the network has no cycles: take the stations in topological order and
    // keep the best profit of a route from S to each of them, -1 if unreachable
    vector<long long> best(n + 1, -1);
    best[s] = 0;
    vector<int> order;
    for (int v = 1; v <= n; v++)
        if (indeg[v] == 0)
            order.push_back(v);
    for (size_t k = 0; k < order.size(); k++) {
        int v = order[k];
        for (auto [w, c] : out[v]) {
            if (best[v] >= 0 && best[v] + c > best[w])
                best[w] = best[v] + c;
            if (--indeg[w] == 0)
                order.push_back(w);
        }
    }
    if (best[f] < 0)
        puts("No solution");
    else
        printf("%lld\n", best[f]);
}
