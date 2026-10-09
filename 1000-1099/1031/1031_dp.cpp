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
    // cost[i]: the cheapest way from a to i over every earlier station j in
    // reach of one ticket; the inner loop stops once j is too far
    std::vector<long long> cost(n + 1, -1);
    cost[a] = 0;
    for (int i = a + 1; i <= b; i++)
        for (int j = i - 1; j >= a && x[i] - x[j] <= len[KINDS - 1]; j--) {
            int k = 0;
            while (x[i] - x[j] > len[k])
                k++;
            if (cost[i] < 0 || cost[j] + price[k] < cost[i])
                cost[i] = cost[j] + price[k];
        }
    printf("%lld\n", cost[b]);
}
