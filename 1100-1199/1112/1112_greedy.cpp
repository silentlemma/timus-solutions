#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::pair<int, int>> segs(n);
    for (auto &s : segs)
        scanf("%d %d", &s.first, &s.second);
    // the segment that ends first leaves the most room for the rest; touching
    // ends share no inner point
    std::sort(segs.begin(), segs.end(),
              [](const auto &p, const auto &q) { return p.second < q.second; });
    std::vector<std::pair<int, int>> chosen;
    for (auto &s : segs)
        if (chosen.empty() || s.first >= chosen.back().second)
            chosen.push_back(s);
    printf("%d\n", (int)chosen.size());
    for (auto &s : chosen)
        printf("%d %d\n", s.first, s.second);
}
