#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <vector>

const double ROOT2 = std::sqrt(2.0);
const int WIDEST = 128, MOVES = 8;

int main() {
    int n, m, k;
    double v;
    scanf("%d %d %d %lf", &n, &m, &k, &v);
    // cells over a grid with a border of buildings, so no move needs a
    // bounds check
    int w = n + 2;
    std::vector<char> free((m + 2) * w, 0);
    char row[WIDEST];
    for (int r = 1; r <= m; r++) {
        scanf("%127s", row);
        for (int c = 1; c <= n && row[c - 1]; c++)
            free[r * w + c] = row[c - 1] == '.';
    }
    int x, y;
    scanf("%d %d", &x, &y);
    int at = y * w + x;
    free[at] = 1; // John stands there, whatever the map shows
    // a step along a side costs 1, along a diagonal sqrt 2, and a diagonal
    // may pass a building's corner
    int steps[] = {1, -1, w, -w, w + 1, w - 1, -w + 1, -w - 1};
    double costs[] = {1, 1, 1, 1, ROOT2, ROOT2, ROOT2, ROOT2};
    // parts of the town joined by moves, so an unreachable bomb costs nothing
    std::vector<int> part(free.size(), 0), stack;
    for (size_t c = 0; c < free.size(); c++) {
        if (!free[c] || part[c])
            continue;
        part[c] = c + 1;
        stack.assign(1, c);
        while (!stack.empty()) {
            int a = stack.back();
            stack.pop_back();
            for (int s : steps)
                if (free[a + s] && !part[a + s]) {
                    part[a + s] = c + 1;
                    stack.push_back(a + s);
                }
        }
    }
    std::vector<double> dist(free.size());
    // shortest walk by A*, with the octile distance as an estimate that
    // never exceeds the true length
    auto walk = [&](int from, int to) {
        auto guess = [&](int c) {
            int dy = std::abs(c / w - to / w), dx = std::abs(c % w - to % w);
            if (dx < dy)
                std::swap(dx, dy);
            return dx + (ROOT2 - 1) * dy;
        };
        std::fill(dist.begin(), dist.end(), HUGE_VAL);
        dist[from] = 0;
        std::priority_queue<std::pair<double, int>, std::vector<std::pair<double, int>>,
                            std::greater<std::pair<double, int>>>
            q;
        q.push({guess(from), from});
        while (true) {
            auto [key, c] = q.top();
            q.pop();
            if (c == to)
                return dist[to];
            if (key > dist[c] + guess(c))
                continue;
            for (int i = 0; i < MOVES; i++) {
                int b = c + steps[i];
                double d = dist[c] + costs[i];
                if (free[b] && d < dist[b]) {
                    dist[b] = d;
                    q.push({d + guess(b), b});
                }
            }
        }
    };
    std::map<std::pair<int, int>, double> known;
    double total = 0;
    while (k--) {
        scanf("%d %d", &x, &y);
        int target = y * w + x;
        // an unreachable bomb is skipped and John stays where he is
        if (part[target] != part[at])
            continue;
        auto it = known.find({at, target});
        double d = it != known.end() ? it->second : walk(at, target);
        known[{at, target}] = known[{target, at}] = d;
        total += d;
        at = target;
    }
    printf("%.2f\n", total / v);
}
