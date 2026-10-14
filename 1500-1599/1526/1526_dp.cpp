#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
    int p, t, n, m;
    scanf("%d %d %d %d", &p, &t, &n, &m);
    int half = t / 2, full = (1 << n) - 1;
    // after[x]: the dishes that may still be brought over a plate of dish x
    vector<int> after(n, full);
    for (int k = 0; k < m; k++) {
        int i, j;
        scanf("%d %d", &i, &j);
        after[i - 1] &= ~(1 << (j - 1));
    }
    // the count of time-tables depends only on the set of dishes that may be
    // brought; plates above a plate of x shrink that set to its part in after[x]
    vector<bool> seen(full + 1, false);
    vector<int> stack = {full}, order;
    seen[full] = true;
    while (!stack.empty()) {
        int allowed = stack.back();
        stack.pop_back();
        order.push_back(allowed);
        for (int x = 0; x < n; x++)
            if (allowed >> x & 1 && !seen[allowed & after[x]]) {
                seen[allowed & after[x]] = true;
                stack.push_back(allowed & after[x]);
            }
    }
    sort(order.begin(), order.end(),
         [](int a, int b) { return __builtin_popcount(a) < __builtin_popcount(b); });
    // ways[s][q]: time-tables of q dishes with the set s allowed
    vector<vector<int>> ways(full + 1);
    for (int allowed : order) {
        vector<int> f(half + 1, 0), tree(half, 0); // tree[q]: one plate with q dishes over it
        f[0] = 1;
        for (int q = 1; q <= half; q++) {
            long long sum = 0;
            for (int x = 0; x < n; x++)
                if (allowed >> x & 1) {
                    int inner = allowed & after[x];
                    sum += inner == allowed ? f[q - 1] : ways[inner][q - 1];
                }
            tree[q - 1] = sum % p;
            // the first plate holds a dishes over it, the rest follow it
            long long total = 0;
            for (int a = 0; a < q; a++)
                total = (total + (long long)tree[a] * f[q - 1 - a]) % p;
            f[q] = total;
        }
        ways[allowed] = f;
    }
    printf("%d\n", ways[full][half] % p);
}
