#include <algorithm>
#include <cstdio>

int main() {
    int n;
    long long a;
    scanf("%d %lld", &n, &a);
    // plus and minus are the best sums of segments ending at the current dish
    // whose last dish counts with a plus or with a minus; before the second
    // dish no minus segment exists, and 0 there only means "start anew"
    long long plus = a, minus = 0, best = std::max(0LL, a);
    for (int i = 1; i < n; i++) {
        scanf("%lld", &a);
        long long nextPlus = a + std::max(0LL, minus);
        minus = plus - a;
        plus = nextPlus;
        best = std::max(best, std::max(plus, minus));
    }
    printf("%lld\n", best);
    return 0;
}
