#include <algorithm>
#include <cstdio>
#include <utility>

const int MAX_SEGMENTS = 99;
// the statement limits n to 99, so both input and selected segments fit this array.
std::pair<int, int> segs[MAX_SEGMENTS];

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    for (int i = 0; i < n; ++i)
        scanf("%d %d", &segs[i].first, &segs[i].second);
    // the segment that ends first leaves the most room for the rest; touching
    // ends share no inner point
    std::sort(segs, segs + n, [](const auto &p, const auto &q) { return p.second < q.second; });
    int count = 0;
    // selected intervals overwrite only input slots already visited.
    for (int i = 0; i < n; ++i)
        if (count == 0 || segs[i].first >= segs[count - 1].second)
            segs[count++] = segs[i];
    printf("%d\n", count);
    for (int i = 0; i < count; ++i)
        printf("%d %d\n", segs[i].first, segs[i].second);
}
