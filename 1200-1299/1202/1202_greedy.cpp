#include <algorithm>
#include <cstdio>
#include <cstdlib>

int main() {
    int n;
    scanf("%d", &n);
    long long y = 1, vertical = 0;
    int low = 0, high = 0, right = 0;
    bool blocked = false;
    for (int i = 0; i < n; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        if (i > 0 && !blocked) {
            // the rectangles form a chain from left to right, so the
            // horizontal part is fixed; only the height at each border varies
            int lo = std::max(low, y1) + 1, hi = std::min(high, y2) - 1;
            if (lo > hi) {
                blocked = true;
            } else {
                // moving only when forced is optimal: clamp into the crossing
                long long target = std::min<long long>(std::max<long long>(y, lo), hi);
                vertical += std::llabs(target - y);
                y = target;
            }
        }
        low = y1, high = y2, right = x2;
    }
    if (blocked) {
        printf("-1\n");
    } else {
        printf("%lld\n", right - 2 + vertical + std::llabs(high - 1 - y));
    }
}
