#include <bitset>
#include <cstdio>
#include <vector>

using namespace std;

const int MAXN = 1000;
const int ROW = MAXN + 2;

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> winners(n);
    vector<int> indegree(n, 0);
    static char row[ROW];
    for (int i = 0; i < n; i++) {
        scanf("%s", row);
        for (int j = 0; j < n; j++)
            if (row[j] == '1') {
                winners[i].push_back(j);
                indegree[j]++;
            }
    }
    // stronger[v]: every team that is stronger than v; the results are
    // transitive, so the wins form an acyclic graph
    vector<bitset<MAXN>> stronger(n);
    vector<int> queue;
    for (int v = 0; v < n; v++)
        if (indegree[v] == 0)
            queue.push_back(v);
    for (size_t h = 0; h < queue.size(); h++) {
        int v = queue[h];
        for (int u : winners[v]) {
            stronger[u] |= stronger[v];
            stronger[u][v] = 1;
            if (--indegree[u] == 0)
                queue.push_back(u);
        }
    }
    // A plays better than B when no team stronger than B is stronger than A
    int q;
    scanf("%d", &q);
    while (q--) {
        int a, b;
        scanf("%d %d", &a, &b);
        puts((stronger[a - 1] & stronger[b - 1]).any() ? "No" : "YES");
    }
}
