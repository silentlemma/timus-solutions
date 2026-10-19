#include <cmath>
#include <cstdio>
#include <unordered_map>
#include <vector>

const int FACES = 6;

int main() {
    int side, n;
    if (scanf("%d %d", &side, &n) != 2) return 0;
    int count = n * n * n;
    // crystals with the same rune touch: the crystals and their contacts
    // form the n x n x n grid, whatever the turns of the crystals
    std::vector<std::vector<int>> near(count);
    std::unordered_map<long long, int> first;
    first.reserve(FACES * count);
    for (int c = 0; c < count; c++) {
        for (int f = 0; f < FACES; f++) {
            long long rune;
            scanf("%lld", &rune);
            if (rune == 0) continue;
            auto it = first.find(rune);
            if (it == first.end()) {
                first[rune] = c;
            } else {
                near[c].push_back(it->second);
                near[it->second].push_back(c);
            }
        }
    }
    // grid steps from start to every crystal
    auto spread = [&](int start) {
        std::vector<int> steps(count, -1), queue = {start};
        steps[start] = 0;
        for (size_t i = 0; i < queue.size(); i++) {
            for (int w : near[queue[i]]) {
                if (steps[w] < 0) {
                    steps[w] = steps[queue[i]] + 1;
                    queue.push_back(w);
                }
            }
        }
        return steps;
    };
    // a corner touches the fewest crystals; the three corners n - 1 steps
    // away lie along the edges from it, and the steps to a corner and to
    // one of them give the coordinate along that edge
    int corner = 0;
    for (int c = 1; c < count; c++) {
        if (near[c].size() < near[corner].size()) corner = c;
    }
    std::vector<int> origin = spread(corner);
    std::vector<std::vector<int>> axes;
    for (int c = 0; c < count; c++) {
        if (origin[c] == n - 1 && near[c].size() == near[corner].size()) axes.push_back(spread(c));
    }
    int m;
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        a--;
        b--;
        double square = 0;
        for (const auto &far : axes) {
            int x = (origin[a] - far[a] + n - 1) / 2, y = (origin[b] - far[b] + n - 1) / 2;
            square += (double)(x - y) * (x - y);
        }
        printf("%.7f\n", side * std::sqrt(square));
    }
    return 0;
}
