#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

const int FIELDS = 3;

int main() {
    int n = 0, m = 0;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    std::vector<int> k(n), first(n), last(n);
    int total = 0;
    for (int i = 0; i < n; i++) {
        if (scanf("%d %d %d", &k[i], &first[i], &last[i]) != FIELDS)
            return 0;
        total += k[i];
    }
    int target = std::min(m, total);
    // best[j]: the cheapest way to make exactly j brooms at the factories so far
    std::vector<double> best(target + 1, HUGE_VAL), fresh, cost;
    best[0] = 0;
    int reach = 0;
    for (int i = 0; i < n; i++) {
        double step = k[i] > 1 ? double(last[i] - first[i]) / (k[i] - 1) : 0.0;
        // cost[x]: x brooms at this factory, the j-th one costing first + step (j - 1)
        cost.assign(k[i] + 1, 0);
        for (int x = 0; x <= k[i]; x++)
            cost[x] = x * first[i] + step * x * (x - 1) / 2;
        reach = std::min(target, reach + k[i]);
        fresh = best;
        for (int j = 1; j <= reach; j++) {
            double here = fresh[j];
            for (int x = 1; x <= std::min(j, k[i]); x++)
                here = std::min(here, best[j - x] + cost[x]);
            fresh[j] = here;
        }
        best.swap(fresh);
    }
    if (target < m)
        printf("Maximum possible amount: %d\n", target);
    printf("Minimum possible cost: %.2f\n", best[target]);
    return 0;
}
