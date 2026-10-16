#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    int n, m, a, b, r, s;
    if (scanf("%d %d %d %d %d %d", &n, &m, &a, &b, &r, &s) < 1) return 0;
    // bus i takes the fans after the border P(i-1) up to the border P(i), with
    // P(0) = 0, P(m) = n and a <= P(i) - P(i-1) <= b; a fan in bus f puts
    // P(f) at or above them and P(f-1) below them
    std::vector<int> lo(m + 1, 0), hi(m + 1, n);
    hi[0] = 0;
    lo[m] = n;
    for (int i = 0; i < s; i++) {
        int fan, bus;
        scanf("%d %d", &fan, &bus);
        lo[bus] = std::max(lo[bus], fan);
        hi[bus - 1] = std::min(hi[bus - 1], fan - 1);
    }
    // the borders reachable from the left end and from the right end each
    // form a range, and a border is possible when it is in both
    for (int i = 1; i <= m; i++) {
        lo[i] = std::max(lo[i], lo[i - 1] + a);
        hi[i] = std::min(hi[i], hi[i - 1] + b);
    }
    for (int i = m - 1; i >= 0; i--) {
        lo[i] = std::max(lo[i], lo[i + 1] - b);
        hi[i] = std::min(hi[i], hi[i + 1] - a);
    }
    for (int i = 0; i <= m; i++) {
        if (lo[i] > hi[i]) {
            puts("IMPOSSIBLE");
            return 0;
        }
    }
    // fan r rides in bus k when some P(k-1) below r and P(k) at or above r
    // are possible borders a to b apart
    std::vector<int> buses;
    for (int k = 1; k <= m; k++) {
        int xLo = lo[k - 1], xHi = std::min(hi[k - 1], r - 1);
        int yLo = std::max(lo[k], r), yHi = hi[k];
        if (xLo <= xHi && yLo <= yHi && yHi - xLo >= a && yLo - xHi <= b) buses.push_back(k);
    }
    printf("%d\n", (int)buses.size());
    for (size_t i = 0; i < buses.size(); i++) printf(i ? " %d" : "%d", buses[i]);
    printf("\n");
    return 0;
}
