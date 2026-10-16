#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

typedef std::pair<int, int> Range;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<Range> pieces(n);
    for (auto &p : pieces) {
        int a, b;
        scanf("%d %d", &a, &b);
        p = {std::min(a, b), std::max(a, b)};
    }
    // a domino is a range [low, high]; standing upright as (low, high) or
    // flipped as (high, low), two of a kind fit together when nested, and
    // one of each when they overlap; the two kinds are nested chains
    std::sort(pieces.begin(), pieces.end(), [](const Range &a, const Range &b) {
        return a.first != b.first ? a.first < b.first : a.second > b.second;
    });
    std::vector<Range> upright, flipped;
    for (const Range &p : pieces) {
        if (upright.empty() || p.second <= upright.back().second) {
            upright.push_back(p);
        } else if (flipped.empty() || p.second <= flipped.back().second) {
            flipped.push_back(p);
        } else {
            printf("NO\n");
            return 0;
        }
    }
    // the innermost ranges of the two chains meet in the middle
    if (!upright.empty() && !flipped.empty()) {
        Range a = upright.back(), b = flipped.back();
        if (a.second < b.first || b.second < a.first) {
            printf("NO\n");
            return 0;
        }
    }
    printf("YES\n");
    for (const Range &p : upright) printf("%d %d\n", p.first, p.second);
    for (auto it = flipped.rbegin(); it != flipped.rend(); ++it) {
        printf("%d %d\n", it->second, it->first);
    }
}
