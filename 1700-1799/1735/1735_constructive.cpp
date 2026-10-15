#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>

int main() {
    int n, k, x, y;
    std::cin >> n >> k >> x >> y;
    // the scale shows x times all the bars plus y - x times the platinum
    // ones, so the counts must have pairwise different subset sums; the
    // Conway-Guy sets u_n - u_i do, with the smallest largest count known
    std::vector<long long> u = {0, 1};
    for (int m = 1; m < n; m++) {
        int r = (int)std::lround(std::sqrt(2.0 * m));
        u.push_back(2 * u[m] - u[m - r]);
    }
    if (u[n] > k) {
        printf("NO\n");
        return 0;
    }
    printf("YES\n");
    for (int i = 0; i < n; i++) printf("%lld%c", u[n] - u[i], i + 1 < n ? ' ' : '\n');
}
