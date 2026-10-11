#include <algorithm>
#include <cstdio>
#include <vector>

const int SIDE = 100;

struct Box {
    int lo, hi, lo2, hi2;
};

Box grow(const Box &a, const Box &b) {
    return {std::min(a.lo, b.lo), std::max(a.hi, b.hi), std::min(a.lo2, b.lo2),
            std::max(a.hi2, b.hi2)};
}

// area of the smallest picture holding the box, at least 100 by 100
long long area(const Box &b) {
    return (long long)std::max(b.hi - b.lo, SIDE) * std::max(b.hi2 - b.lo2, SIDE);
}

// splits the spots by a line across the first axis: sorted by their low
// edge, a prefix and the rest can hang apart exactly when the prefix ends
// no later than the rest begins
long long best(std::vector<Box> spots) {
    std::sort(spots.begin(), spots.end(), [](const Box &a, const Box &b) { return a.lo < b.lo; });
    int n = spots.size();
    std::vector<Box> suffix(spots);
    for (int i = n - 2; i >= 0; i--)
        suffix[i] = grow(spots[i], suffix[i + 1]);
    long long result = area(suffix[0]);
    Box prefix = spots[0];
    for (int k = 1; k < n; k++) {
        if (prefix.hi <= spots[k].lo)
            result = std::min(result, area(prefix) + area(suffix[k]));
        prefix = grow(prefix, spots[k]);
    }
    return result;
}

int main() {
    int n;
    scanf("%d", &n);
    // a picture must hold each spot whole, so it must hold its bounding square
    std::vector<Box> across(n), down(n);
    for (int i = 0; i < n; i++) {
        int r, x, y;
        scanf("%d %d %d", &r, &x, &y);
        across[i] = {x - r, x + r, y - r, y + r};
        down[i] = {y - r, y + r, x - r, x + r};
    }
    // two pictures that do not overlap are split by a vertical or a
    // horizontal line, and each can grow to 100 mm away from that line
    printf("%lld\n", std::min(best(across), best(down)));
}
