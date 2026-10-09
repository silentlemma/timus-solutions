#include <algorithm>
#include <cstdio>
#include <map>
#include <numeric>
#include <utility>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<int> x(n), y(n);
    for (int i = 0; i < n; i++)
        if (scanf("%d %d", &x[i], &y[i]) != 2)
            return 0;
    int best = std::min(n, 2);
    for (int i = 0; i < n; i++) {
        // the points on one line through point i have the same reduced direction
        std::map<std::pair<int, int>, int> count;
        for (int j = i + 1; j < n; j++) {
            int dx = x[j] - x[i], dy = y[j] - y[i], g = std::gcd(dx, dy);
            dx /= g;
            dy /= g;
            // opposite directions are the same line
            if (dx < 0 || (dx == 0 && dy < 0)) {
                dx = -dx;
                dy = -dy;
            }
            best = std::max(best, ++count[{dx, dy}] + 1);
        }
    }
    printf("%d\n", best);
}
