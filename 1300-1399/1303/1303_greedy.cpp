#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int m = 0;
    if (scanf("%d", &m) != 1)
        return 0;
    std::vector<std::pair<int, int>> segments;
    int left = 0, right = 0;
    while (scanf("%d %d", &left, &right) == 2 && (left != 0 || right != 0)) {
        segments.push_back({left, right});
    }
    std::sort(segments.begin(), segments.end());
    std::vector<std::pair<int, int>> chosen;
    int covered = 0;
    size_t i = 0;
    while (covered < m) {
        // among the segments that start inside the covered part, take the
        // one that reaches furthest; it is never worse than any other
        int best = -1;
        for (; i < segments.size() && segments[i].first <= covered; i++) {
            if (best < 0 || segments[i].second > segments[best].second)
                best = (int)i;
        }
        if (best < 0 || segments[best].second <= covered) {
            puts("No solution");
            return 0;
        }
        chosen.push_back(segments[best]);
        covered = segments[best].second;
    }
    printf("%d\n", (int)chosen.size());
    for (auto &s : chosen)
        printf("%d %d\n", s.first, s.second);
    return 0;
}
