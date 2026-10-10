#include <algorithm>
#include <cmath>
#include <cstdio>
#include <limits>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<double> x(n), y(n);
    for (int k = 0; k < n; k++)
        if (scanf("%lf %lf", &x[k], &y[k]) != 2)
            return 0;
    auto dist = [&](int a, int b) { return std::hypot(x[a] - x[b], y[a] - y[b]); };
    // a shortest path never crosses itself, so on a convex polygon the visited
    // camps form an arc and the path ends at one of its ends; at[i] and
    // at_end[i] are the best paths over the arc from camp i, ending at either end
    const double INF = std::numeric_limits<double>::infinity();
    std::vector<double> at(n, 0), at_end(n, 0);
    for (int length = 1; length < n; length++) {
        std::vector<double> grow(n, INF), grow_end(n, INF);
        for (int i = 0; i < n; i++) {
            int j = (i + length - 1) % n, before = (i + n - 1) % n, after = (i + length) % n;
            for (auto [cost, here] : {std::pair{at[i], i}, std::pair{at_end[i], j}}) {
                grow[before] = std::min(grow[before], cost + dist(here, before));
                grow_end[i] = std::min(grow_end[i], cost + dist(here, after));
            }
        }
        at.swap(grow);
        at_end.swap(grow_end);
    }
    double best = INF;
    for (int i = 0; i < n; i++)
        best = std::min({best, at[i], at_end[i]});
    printf("%.3f\n", best);
}
