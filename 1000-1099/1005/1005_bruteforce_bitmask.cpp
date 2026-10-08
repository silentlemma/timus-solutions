#include <cstdio>
#include <cstdlib>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<long long> w(n);
    long long total = 0;
    for (long long &x : w) {
        if (scanf("%lld", &x) != 1)
            return 0;
        total += x;
    }
    // Gray code order: each next subset differs by one stone, so the weight of
    // the first pile is updated in O(1); the last stone can stay in pile two.
    long long pile = 0, best = total;
    int subsets = 1 << (n - 1);
    for (int g = 1; g < subsets; g++) {
        int stone = __builtin_ctz(g);
        bool added = (g ^ (g >> 1)) >> stone & 1;
        pile += added ? w[stone] : -w[stone];
        long long diff = std::llabs(total - 2 * pile);
        if (diff < best)
            best = diff;
    }
    printf("%lld\n", best);
    return 0;
}
