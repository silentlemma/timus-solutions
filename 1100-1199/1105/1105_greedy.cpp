#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

const int SHIFTS = 3;
const double EPS = 1e-9;

int main() {
    double t0, t1;
    int n;
    if (scanf("%lf %lf", &t0, &t1) != 2 || scanf("%d", &n) != 1)
        return 0;
    std::vector<double> lo(n), hi(n);
    for (int i = 0; i < n; i++)
        scanf("%lf %lf", &lo[i], &hi[i]);
    // greedy cover: each step takes the observer reaching furthest among those
    // already present, so only neighbouring observers of the chain overlap
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int a, int b) { return lo[a] < lo[b]; });
    std::vector<int> chain;
    double cur = t0;
    int i = 0;
    while (cur < t1 && i < n) {
        int best = -1;
        for (; i < n && lo[order[i]] <= cur; i++)
            if (best < 0 || hi[order[i]] > hi[best])
                best = order[i];
        if (best < 0 || hi[best] <= cur) {
            cur = i < n ? lo[order[i]] : t1;
            continue;
        }
        chain.push_back(best);
        cur = hi[best];
    }
    // dropping every third observer of the chain leaves each piece of time
    // alone in two of the three shifts, so the best shift keeps 2/3 of it
    int m = chain.size(), best_shift = 0;
    double best_alone = -1;
    for (int shift = 0; shift < SHIFTS; shift++) {
        double alone = 0;
        for (int k = 0; k < m; k++) {
            if (k % SHIFTS == shift)
                continue;
            alone += hi[chain[k]] - lo[chain[k]];
            if (k + 1 < m && (k + 1) % SHIFTS != shift)
                alone -= 2 * std::max(0.0, hi[chain[k]] - lo[chain[k + 1]]);
        }
        if (alone > best_alone) {
            best_shift = shift;
            best_alone = alone;
        }
    }
    if (best_alone < (t1 - t0) * 2 / SHIFTS - EPS) {
        printf("0\n");
        return 0;
    }
    std::vector<int> painted;
    for (int k = 0; k < m; k++)
        if (k % SHIFTS != best_shift)
            painted.push_back(chain[k] + 1);
    printf("%d\n", (int)painted.size());
    for (int p : painted)
        printf("%d\n", p);
}
