#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>

typedef long long ll;

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2) return 0;
    std::vector<ll> xs(n), ys(n), across(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &xs[i], &ys[i]);
    // a ball of diameter D hits the pins whose centres lie in a strip of width
    // D + 1 along its path, so the narrowest strip holding k centres decides, and
    // one side of that strip runs along two centres, so only those directions
    double best = k > 1 ? HUGE_VAL : 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            ll dx = xs[j] - xs[i], dy = ys[j] - ys[i];
            for (int t = 0; t < n; t++) across[t] = dx * ys[t] - dy * xs[t];
            std::sort(across.begin(), across.end());
            ll gap = across[k - 1] - across[0];
            for (int t = 1; t + k <= n; t++) gap = std::min(gap, across[t + k - 1] - across[t]);
            best = std::min(best, gap / std::hypot((double)dx, (double)dy));
        }
    }
    // a ball of any size will do when the strip is no wider than a pin
    if (best > 1) printf("%.10f\n", best - 1);
    else puts("0.000000");
    return 0;
}
