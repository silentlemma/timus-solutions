#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

const int SIDE = 100;

int main() {
    int n, m, k;
    if (scanf("%d %d", &n, &m) != 2 || scanf("%d", &k) != 1)
        return 0;
    std::vector<std::pair<int, int>> blocks(k);
    for (auto &b : blocks)
        scanf("%d %d", &b.first, &b.second);
    std::sort(blocks.begin(), blocks.end());
    // a route can use a chain of diagonal blocks increasing in both
    // coordinates; each one replaces two sides by one diagonal
    std::vector<int> chain(k, 1);
    int best = 0;
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < i; j++)
            if (blocks[j].first < blocks[i].first && blocks[j].second < blocks[i].second)
                chain[i] = std::max(chain[i], chain[j] + 1);
        best = std::max(best, chain[i]);
    }
    double length = SIDE * (n + m - 2 * best) + SIDE * std::sqrt(2.0) * best;
    printf("%.0f\n", std::round(length));
}
