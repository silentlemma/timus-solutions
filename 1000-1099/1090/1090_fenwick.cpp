#include <cstdio>
#include <vector>

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2)
        return 0;
    long long best = -1;
    int best_row = 0;
    std::vector<int> tree(n + 1);
    for (int r = 1; r <= k; r++) {
        tree.assign(n + 1, 0);
        long long jumps = 0;
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            // each recruit jumps once for every earlier recruit with a larger
            // number: earlier minus those not larger, counted by the tree
            int smaller = 0;
            for (int j = x; j > 0; j &= j - 1)
                smaller += tree[j];
            jumps += i - smaller;
            for (int j = x; j <= n; j += j & -j)
                tree[j]++;
        }
        if (jumps > best)
            best = jumps, best_row = r;
    }
    printf("%d\n", best_row);
}
