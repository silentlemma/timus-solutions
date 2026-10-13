#include <cmath>
#include <cstdio>
#include <vector>

const double GRAVITY = 10;
const double INF = 1e18;

int main() {
    int n = 0, m = 0;
    if (scanf("%d %d", &n, &m) != 2)
        return 0;
    // the speed at depth d is sqrt(2 g d), whatever the way down was
    std::vector<double> speed(m + 1);
    for (int d = 0; d <= m; d++)
        speed[d] = std::sqrt(2 * GRAVITY * d);
    // best holds the least time to reach each depth and distance to the left,
    // where a board with constant acceleration takes 2 L / (v1 + v2)
    std::vector<std::vector<double>> best(m + 1, std::vector<double>(n + 1, INF));
    best[0][0] = 0;
    for (int d = 1; d <= m; d++)
        for (int e = 0; e < d; e++) {
            double vs = speed[d] + speed[e];
            for (int x = 0; x <= n; x++) {
                if (best[e][x] >= INF)
                    continue;
                for (int y = x; y <= n; y++) {
                    double c = best[e][x] + 2 * std::hypot(y - x, d - e) / vs;
                    if (c < best[d][y])
                        best[d][y] = c;
                }
            }
        }
    printf("%.4f\n", best[m][n]);
    return 0;
}
