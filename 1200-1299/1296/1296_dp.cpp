#include <algorithm>
#include <cstdio>

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    // best is the largest segment sum so far (the empty segment gives 0), and
    // ending is the largest sum of a segment that ends at the current number
    long long best = 0, ending = 0;
    for (int i = 0; i < n; i++) {
        long long p = 0;
        if (scanf("%lld", &p) != 1)
            break;
        ending = std::max(ending + p, 0LL);
        best = std::max(best, ending);
    }
    printf("%lld\n", best);
    return 0;
}
