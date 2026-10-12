#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

const double EPS = 1e-7;

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::pair<double, double>> cities(n);
    for (auto &c : cities) {
        int x = 0, y = 0;
        if (scanf("%d %d", &x, &y) != 2)
            return 0;
        c = {x, y};
    }
    int big = 0, small = 0;
    if (scanf("%d %d", &big, &small) != 2)
        return 0;
    double reach = big - small; // how far a center may be
    if (reach < 0) {
        printf("0\n");
        return 0;
    }
    // a best circle can be moved until it passes through two centers or
    // stands on one, so only such places need to be tried
    std::vector<std::pair<double, double>> places(cities);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            double ax = cities[i].first, ay = cities[i].second;
            double dx = cities[j].first - ax, dy = cities[j].second - ay;
            double half = std::hypot(dx, dy) / 2;
            if (half > 0 && half <= reach) {
                double rise = std::sqrt(std::max(0.0, reach * reach - half * half)) / (2 * half);
                double mx = ax + dx / 2, my = ay + dy / 2;
                places.push_back({mx - dy * rise, my + dx * rise});
                places.push_back({mx + dy * rise, my - dx * rise});
            }
        }
    }
    double limit = (reach + EPS) * (reach + EPS);
    int best = 0;
    for (auto &p : places) {
        int inside = 0;
        for (auto &c : cities) {
            double dx = c.first - p.first, dy = c.second - p.second;
            if (dx * dx + dy * dy <= limit)
                inside++;
        }
        best = std::max(best, inside);
    }
    printf("%d\n", best);
    return 0;
}
