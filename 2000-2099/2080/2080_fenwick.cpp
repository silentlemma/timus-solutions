#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> uses(k + 1);
    for (int i = 1; i <= k; i++) scanf("%d", &uses[i]);
    // the stack is kept in order of next use: after a card is used, the cards above
    // it are those used before its next use, the distinct cards in between
    vector<int> nxt(k + 1), seen(n + 1, k + 1);
    for (int i = k; i >= 1; i--) {
        nxt[i] = seen[uses[i]];
        seen[uses[i]] = i;
    }
    // Fenwick tree over moments: a moment j counts once the query time i reaches
    // the previous use of its card, so the counted moments are first uses after i
    vector<int> tree(k + 1, 0);
    auto add = [&](int j) {
        for (; j <= k; j += j & -j) tree[j]++;
    };
    auto prefix = [&](int j) {
        int s = 0;
        for (; j > 0; j -= j & -j) s += tree[j];
        return s;
    };
    for (int card = 1; card <= n; card++)
        if (seen[card] <= k) add(seen[card]);
    vector<int> above(k + 1);
    for (int i = 1; i <= k; i++) {
        if (nxt[i] <= k) add(nxt[i]);
        above[i] = prefix(nxt[i] - 1) - prefix(i);
    }
    vector<int> order(n);
    iota(order.begin(), order.end(), 1);
    stable_sort(order.begin(), order.end(), [&](int a, int b) { return seen[a] < seen[b]; });
    for (int i = 0; i < n; i++) printf(i ? " %d" : "%d", order[i]);
    printf("\n");
    for (int i = 1; i <= k; i++) printf("%d\n", above[i]);
}
