#include <algorithm>
#include <climits>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

constexpr long long NONE = LLONG_MIN;  // an unreachable state

int main() {
    int x, n;
    scanf("%d %d", &x, &n);
    vector<int> a(n), b(n);
    for (int& v : a) scanf("%d", &v);
    for (int& v : b) scanf("%d", &v);
    // utility above x is earned whatever the order; with b capped at x a task
    // done at repaired volume r (debt x - r) earns max(0, min(x, r) - (x - b))
    long long extra = 0;
    vector<int> need(n);
    for (int i = 0; i < n; i++) extra += max(0, b[i] - x), need[i] = x - min(b[i], x);
    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    stable_sort(order.begin(), order.end(), [&](int i, int j) { return a[i] < a[j]; });
    // some tasks are given up: they go first and only repair. The rest go by a
    // descending, so task i (ascending a) sees the given up ones before it and
    // every task from it on. best[s]: s = repair of given up tasks so far, capped
    vector<int> suffix(n + 1, 0);
    for (int k = n - 1; k >= 0; k--) suffix[k] = suffix[k + 1] + a[order[k]];
    vector<long long> best(x + 1, NONE);
    best[0] = 0;
    // from[k][s]: the previous state, and whether task k was given up
    vector<vector<pair<int, bool>>> from(n, vector<pair<int, bool>>(x + 1));
    for (int k = 0; k < n; k++) {
        int i = order[k];
        vector<long long> nxt(x + 1, NONE);
        for (int s = 0; s <= x; s++) {
            if (best[s] == NONE) continue;
            long long gain = best[s] + min(x, s + suffix[k]) - need[i];
            if (gain > nxt[s]) nxt[s] = gain, from[k][s] = {s, false};
            int t = min(x, s + a[i]);
            if (best[s] > nxt[t]) nxt[t] = best[s], from[k][t] = {s, true};
        }
        best = nxt;
    }
    int s = int(max_element(best.begin(), best.end()) - best.begin());
    printf("%lld\n", best[s] + extra);
    vector<int> givenUp, kept;  // kept comes out by a descending
    for (int k = n - 1; k >= 0; k--) {
        bool up = from[k][s].second;
        (up ? givenUp : kept).push_back(order[k]);
        s = from[k][s].first;
    }
    givenUp.insert(givenUp.end(), kept.begin(), kept.end());
    for (int k = 0; k < n; k++) printf(k ? " %d" : "%d", givenUp[k] + 1);
    printf("\n");
}
