#include <cstdio>
#include <vector>
using namespace std;

const int INF = 1 << 30;
const int TOP = 10000;  // the largest vertex number

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> chain(n);
    for (int &v : chain)
        if (scanf("%d", &v) != 1)
            return 0;
    int end = chain[n - 1];
    if (chain[0] == end) {
        printf("%d\n", end);
        return 0;
    }
    // dp[i]: fewest edges from position i to the final vertex, taking only
    // edges of p from i on; reaching the final vertex anywhere ends it
    vector<int> dp(n, INF), step(n, -1);
    // per vertex: the best dp after leaving it and where, latest on ties
    vector<int> bestValue(TOP + 1, INF), bestAt(TOP + 1, -1);
    dp[n - 1] = 0;
    for (int i = n - 2; i >= 0; i--) {
        int u = chain[i];
        if (dp[i + 1] < bestValue[u]) {
            bestValue[u] = dp[i + 1];
            bestAt[u] = i + 1;
        }
        if (u == end) {
            dp[i] = 0;
        } else if (bestValue[u] < INF) {
            dp[i] = bestValue[u] + 1;
            step[i] = bestAt[u];
        }
    }
    printf("%d", chain[0]);
    for (int i = 0; chain[i] != end;) {
        i = step[i];
        printf(" %d", chain[i]);
    }
    printf("\n");
}
