#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
    long long length;
    int n;
    if (scanf("%lld %d", &length, &n) != 2) return 0;
    std::vector<long long> s(n);
    for (auto &v : s) scanf("%lld", &v);
    // a cut at x between supports s[i] and s[i + 1] leaves both parts
    // standing when the left centre x/2 lies in [s[0], s[i]] and the right
    // centre (x + length)/2 lies in [s[i + 1], s[n - 1]]
    long long loAll = 2 * s[0], hiAll = 2 * s[n - 1] - length, safe = 0;
    for (int i = 0; i + 1 < n; i++) {
        long long lo = std::max({s[i], loAll, 2 * s[i + 1] - length});
        long long hi = std::min({s[i + 1], hiAll, 2 * s[i]});
        safe += std::max(0LL, hi - lo);
    }
    printf("%lld\n", length - safe);
    return 0;
}
