#include <algorithm>
#include <cstdio>
#include <vector>

const int KINDS = 3;

int main() {
    long long len[KINDS], price[KINDS];
    for (int k = 0; k < KINDS; k++)
        if (scanf("%lld", &len[k]) != 1)
            return 1;
    for (int k = 0; k < KINDS; k++)
        if (scanf("%lld", &price[k]) != 1)
            return 1;
    int n, a, b;
    if (scanf("%d %d %d", &n, &a, &b) != KINDS)
        return 1;
    std::vector<long long> x(n + 1, 0);
    for (int i = 2; i <= n; i++)
        if (scanf("%lld", &x[i]) != 1)
            return 1;
    if (a > b)
        std::swap(a, b);
    // cost[i]: the cheapest way from a to i; it never decreases along the
    // line, so for every kind of ticket the farthest start in reach is best
    std::vector<long long> cost(n + 1, 0);
    int from[KINDS] = {a, a, a};
    for (int i = a + 1; i <= b; i++) {
        cost[i] = -1;
        for (int k = 0; k < KINDS; k++) {
            while (x[i] - x[from[k]] > len[k])
                from[k]++;
            if (from[k] < i && (cost[i] < 0 || cost[from[k]] + price[k] < cost[i]))
                cost[i] = cost[from[k]] + price[k];
        }
    }
    printf("%lld\n", cost[b]);
}
