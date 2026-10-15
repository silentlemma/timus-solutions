#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int g, w, b, p, n;
    scanf("%d %d %d %d %d", &g, &w, &b, &p, &n);
    int last = g - b;  // the barbell starts at s = 0 .. g - b
    std::vector<int> diff(last + 2, 0);
    auto add = [&](int lo, int hi, int value) {
        lo = std::max(lo, 0);
        hi = std::min(hi, last);
        if (lo <= hi) {
            diff[lo] += value;
            diff[hi + 1] -= value;
        }
    };
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        // a plate [a, a + p] hurts the worm [x, x + w] when they overlap by a
        // positive length, that is for whole a from x - p + 1 to x + w - 1.
        // The left plate starts at s, the right one at s + b - p
        int lo1 = x - p + 1, hi1 = x + w - 1;
        int lo2 = x - b + 1, hi2 = x + w - 1 - b + p;
        add(lo1, hi1, 1);
        add(lo2, hi2, 1);
        // a worm under both plates is hurt once
        add(std::max(lo1, lo2), std::min(hi1, hi2), -1);
    }
    int best = 0, bestHurt = 0, hurt = 0;
    for (int s = 0; s <= last; s++) {
        hurt += diff[s];
        if (s == 0 || hurt < bestHurt) {
            bestHurt = hurt;
            best = s;
        }
    }
    printf("%d\n", best);
}
