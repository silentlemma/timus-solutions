#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

const long long INF = 1LL << 60;

int main() {
    int n;
    scanf("%d", &n);
    // the Hungarian method minimises the cost -A; rows and columns from 1, 0 is a helper
    vector<vector<long long>> cost(n + 1, vector<long long>(n + 1, 0));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            scanf("%lld", &cost[i][j]);
            cost[i][j] = -cost[i][j];
        }
    vector<long long> u(n + 1, 0), v(n + 1, 0);
    vector<int> match(n + 1, 0), way(n + 1, 0); // match[j]: the row matched to column j
    for (int i = 1; i <= n; i++) {
        match[0] = i;
        int j0 = 0;
        vector<long long> low(n + 1, INF);
        vector<bool> used(n + 1, false);
        while (match[j0]) {
            used[j0] = true;
            int i0 = match[j0], j1 = 0;
            long long delta = INF;
            for (int j = 1; j <= n; j++)
                if (!used[j]) {
                    long long cur = cost[i0][j] - u[i0] - v[j];
                    if (cur < low[j]) {
                        low[j] = cur;
                        way[j] = j0;
                    }
                    if (low[j] < delta) {
                        delta = low[j];
                        j1 = j;
                    }
                }
            for (int j = 0; j <= n; j++)
                if (used[j]) {
                    u[match[j]] += delta;
                    v[j] -= delta;
                } else {
                    low[j] -= delta;
                }
            j0 = j1;
        }
        while (j0) {
            int j1 = way[j0];
            match[j0] = match[j1];
            j0 = j1;
        }
    }
    // u + v <= -A, so the bribes -u, -v cover every credit and add up to the
    // heaviest matching; shifting them until a row bribe is 0 keeps all >= 0
    long long shift = INF;
    for (int i = 1; i <= n; i++)
        shift = min(shift, -u[i]);
    for (int i = 1; i <= n; i++)
        printf("%lld%c", -u[i] - shift, i == n ? '\n' : ' ');
    for (int j = 1; j <= n; j++)
        printf("%lld%c", -v[j] + shift, j == n ? '\n' : ' ');
}
