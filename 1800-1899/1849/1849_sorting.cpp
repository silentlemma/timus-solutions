#include <algorithm>
#include <cstdio>
#include <limits>
#include <numeric>
#include <vector>

const int SPAN = 10000;  // coordinates lie in [-SPAN, SPAN]
const int REACH = 10;    // direction parts lie in [-REACH, REACH]
const int WIDTH = 2 * SPAN + 1, TURN = 2 * REACH + 1;
const int LOWEST = std::numeric_limits<int>::min();

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<int> rx(n), ry(n);
    for (int i = 0; i < n; i++) scanf("%d %d", &rx[i], &ry[i]);
    long long q, x, y, vx, vy, ax, bx, ay, by, avx, bvx, avy, bvy;
    scanf("%lld %lld %lld %lld %lld", &q, &x, &y, &vx, &vy);
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &ax, &bx, &ay, &by, &avx, &bvx, &avy, &bvy);
    // every direction is filed under its primitive vector
    std::vector<std::pair<int, int>> primitive;
    std::vector<int> code(TURN * TURN, 0);
    for (int dx = -REACH; dx <= REACH; dx++) {
        for (int dy = -REACH; dy <= REACH; dy++) {
            int g = std::gcd(dx, dy);
            if (g == 0) continue;
            std::pair<int, int> key = {dx / g, dy / g};
            auto it = std::find(primitive.begin(), primitive.end(), key);
            code[(dx + REACH) * TURN + dy + REACH] = it - primitive.begin();
            if (it == primitive.end()) primitive.push_back(key);
        }
    }
    int kinds = primitive.size();
    std::vector<int> xs(q), ys(q), kind(q), start(kinds + 1, 0);
    for (int i = 0; i < q; i++) {
        xs[i] = x;
        ys[i] = y;
        kind[i] = code[(vx + REACH) * TURN + vy + REACH];
        start[kind[i] + 1]++;
        x = (ax * (x + SPAN) + bx) % WIDTH - SPAN;
        y = (ay * (y + SPAN) + by) % WIDTH - SPAN;
        vx = (avx * (vx + REACH) + bvx) % TURN - REACH;
        vy = (avy * (vy + REACH) + bvy) % TURN - REACH;
    }
    // the shots in order of their direction, by counting
    std::partial_sum(start.begin(), start.end(), start.begin());
    std::vector<int> shots(q), fill(start.begin(), start.end() - 1);
    for (int i = 0; i < q; i++) shots[fill[kind[i]]++] = i;
    int best = 0, bestCount = -1;
    std::vector<std::pair<int, int>> rabbits(n);
    for (int k = 0; k < kinds; k++) {
        if (start[k] == start[k + 1]) continue;
        int dx = primitive[k].first, dy = primitive[k].second;
        // rabbits by the line along (dx, dy) and then by the place on it
        for (int i = 0; i < n; i++) {
            rabbits[i] = {rx[i] * dy - ry[i] * dx, rx[i] * dx + ry[i] * dy};
        }
        std::sort(rabbits.begin(), rabbits.end());
        for (int j = start[k]; j < start[k + 1]; j++) {
            int i = shots[j];
            int line = xs[i] * dy - ys[i] * dx, place = xs[i] * dx + ys[i] * dy;
            auto from = std::lower_bound(rabbits.begin(), rabbits.end(),
                                         std::make_pair(line, place));
            auto to = std::lower_bound(rabbits.begin(), rabbits.end(),
                                       std::make_pair(line + 1, LOWEST));
            int got = to - from;
            // a later shot wins a tie
            if (got > bestCount || (got == bestCount && i > best)) {
                best = i;
                bestCount = got;
            }
        }
    }
    printf("%d %d\n", best + 1, bestCount);
    return 0;
}
