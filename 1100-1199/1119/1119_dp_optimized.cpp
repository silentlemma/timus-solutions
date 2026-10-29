#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>

constexpr int SIDE = 100;
constexpr int MAX_DIAGONALS = 100;

int main() {
    int width, height, count;
    scanf("%d%d%d", &width, &height, &count);
    // at most 100 diagonal blocks: fixed arrays need no heap allocation
    std::pair<int, int> blocks[MAX_DIAGONALS];
    for (int i = 0; i < count; ++i) {
        scanf("%d%d", &blocks[i].first, &blocks[i].second);
    }
    std::sort(blocks, blocks + count);
    // a route can use a chain of diagonal blocks increasing in both
    // coordinates; each one replaces two sides by one diagonal
    int chain[MAX_DIAGONALS];
    int best = 0;
    for (int i = 0; i < count; ++i) {
        chain[i] = 1;
        for (int j = 0; j < i; ++j) {
            if (blocks[j].first < blocks[i].first && blocks[j].second < blocks[i].second) {
                chain[i] = std::max(chain[i], chain[j] + 1);
            }
        }
        best = std::max(best, chain[i]);
    }
    double length = SIDE * (width + height - 2 * best) + SIDE * std::sqrt(2.0) * best;
    // no std::round needed: 100 * sqrt(2) * best is irrational for best > 0, so the
    // length is never exactly halfway between two integers
    printf("%.0f\n", length);
}
