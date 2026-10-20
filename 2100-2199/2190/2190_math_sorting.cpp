#include <algorithm>
#include <cstdio>
#include <numeric>
#include <vector>

int main() {
    int n;
    scanf("%d", &n);
    std::vector<long long> s(n), q(n);
    for (auto &v : s) scanf("%lld", &v);
    for (auto &v : q) scanf("%lld", &v);
    long long g = 0;
    for (long long v : q) g = std::gcd(g, v);
    for (auto &v : q) v /= g;
    // The heaps become k * q for an integer k >= 1, and the cost
    // sum |s - k q| = sum q |s / q - k| is convex in k with its real minimum
    // at the median of the ratios s / q weighted by q.
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(),
              [&](int i, int j) { return s[i] * q[j] < s[j] * q[i]; });
    long long total = 0;
    for (long long v : q) total += v;
    long long weight = 0;
    int median = order[n - 1];
    for (int i : order) {
        weight += q[i];
        if (2 * weight >= total) {
            median = i;
            break;
        }
    }
    long long low = s[median] / q[median];
    auto cost = [&](long long k) {
        long long sum = 0;
        for (int i = 0; i < n; i++) sum += std::llabs(s[i] - k * q[i]);
        return sum;
    };
    long long best = cost(low + 1);
    if (low >= 1) best = std::min(best, cost(low));
    printf("%lld\n", best);
    return 0;
}
