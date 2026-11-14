#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

constexpr double MIN_ROPE = 1.0;
constexpr double MAX_ROPE = 50.0;
constexpr double EPS = 1e-9;
constexpr double MIN_SEPARATION = 2 * MIN_ROPE;

struct Tree {
    double x, y;
    double limitSquared = MAX_ROPE * MAX_ROPE;
    double limit = MAX_ROPE;
};

double separationSquared(const Tree &a, const Tree &b) {
    const double dx = a.x - b.x, dy = a.y - b.y;
    return dx * dx + dy * dy;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<Tree> trees(n);
    for (auto &tree : trees)
        scanf("%lf %lf", &tree.x, &tree.y);
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            const double distance = separationSquared(trees[i], trees[j]);
            trees[i].limitSquared = std::min(trees[i].limitSquared, distance);
            trees[j].limitSquared = std::min(trees[j].limitSquared, distance);
        }
    }
    for (auto &tree : trees)
        tree.limit = std::sqrt(tree.limitSquared);
    std::sort(trees.begin(), trees.end(),
              [](const Tree &a, const Tree &b) { return a.limitSquared > b.limitSquared; });

    double best = 0;
    for (int i = 0; i + 1 < n; ++i) {
        const Tree &a = trees[i];
        if (a.limitSquared + trees[i + 1].limitSquared <= best)
            break;
        for (int j = i + 1; j < n; ++j) {
            const Tree &b = trees[j];
            const double upper = a.limitSquared + b.limitSquared;
            if (upper <= best || b.limit < MIN_ROPE - EPS)
                break;
            const double squared = separationSquared(a, b);
            const double sum = a.limit + b.limit;
            if (squared >= sum * sum) {
                best = upper;
                break;
            }
            if (squared < MIN_SEPARATION * MIN_SEPARATION - EPS)
                continue;
            // On a + b = distance the convex objective is largest at an endpoint.
            const double distance = std::sqrt(squared);
            const double longA = std::min(a.limit, distance - MIN_ROPE);
            const double longB = std::min(b.limit, distance - MIN_ROPE);
            const double shortA = distance - longB, shortB = distance - longA;
            best =
                std::max({best, longA * longA + shortB * shortB, shortA * shortA + longB * longB});
        }
    }
    printf("%.4f\n", std::acos(-1.0) * best);
}
