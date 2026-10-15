#include <algorithm>
#include <cstdio>
#include <vector>

// the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
// is larger than the i values before it
long long pairSum(std::vector<long long> &a) {
    std::sort(a.begin(), a.end());
    long long total = 0, before = 0;
    for (size_t i = 0; i < a.size(); i++) {
        total += a[i] * (long long)i - before;
        before += a[i];
    }
    return total;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);
    // walking along the streets, a visit covers |dx| + |dy|
    long long pairs = (long long)n * (n - 1) / 2;
    printf("%lld\n", (pairSum(x) + pairSum(y)) / pairs);
}
