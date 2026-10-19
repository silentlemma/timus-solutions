#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> ex(n), ey(n);
    vector<vector<int>> incident(k + 1);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &ex[i], &ey[i]);
        incident[ex[i]].push_back(i);
        incident[ey[i]].push_back(i);
    }
    vector<int> winner(n, 0), degree(k + 1), leaves;
    auto open = [&](int v) {  // a pair of v without a winner yet
        for (int i : incident[v])
            if (!winner[i]) return i;
        return -1;
    };
    // every team may win at most one pair: a team with a single open pair takes
    // it, which never hurts, and the pair is closed for the other team
    for (int v = 1; v <= k; v++)
        if ((degree[v] = incident[v].size()) == 1) leaves.push_back(v);
    while (!leaves.empty()) {
        int v = leaves.back();
        leaves.pop_back();
        if (degree[v] != 1) continue;
        int i = open(v), u = ex[i] + ey[i] - v;
        winner[i] = v;
        degree[v] = 0;
        if (--degree[u] == 1) leaves.push_back(u);
    }
    // what is left must be disjoint cycles (every degree 2); each cycle is walked
    // and every pair is won by the team it leads to
    for (int v = 1; v <= k; v++)
        if (degree[v] > 2) {
            puts("No");
            return 0;
        }
    for (int start = 1; start <= k; start++) {
        if (degree[start] != 2) continue;
        int v = start;
        do {
            int i = open(v), u = ex[i] + ey[i] - v;
            winner[i] = u;
            degree[v]--, degree[u]--;
            v = u;
        } while (v != start);
    }
    puts("Yes");
    for (int w : winner) printf("%d\n", w);
}
