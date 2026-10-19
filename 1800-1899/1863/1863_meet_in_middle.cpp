#include <algorithm>
#include <cstdio>
#include <vector>

long long n;
std::vector<long long> start, rest;
long long shallowest, deepest;

// a signing of the second half with this total and these lowest and highest
// running sums fits after depth x exactly when -low <= x <= n - high, and
// it ends at x + total
void walk(size_t i, long long total, long long low, long long high) {
    if (i == rest.size()) {
        auto first = std::lower_bound(start.begin(), start.end(), -low);
        if (first == start.end() || *first > n - high) return;
        shallowest = std::min(shallowest, *first + total);
        auto last = std::upper_bound(start.begin(), start.end(), n - high) - 1;
        deepest = std::max(deepest, *last + total);
        return;
    }
    for (long long u : {total + rest[i], total - rest[i]}) {
        long long a = std::min(low, u), b = std::max(high, u);
        if (b - a <= n) walk(i + 1, u, a, b);
    }
}

int main() {
    long long s;
    int k;
    if (scanf("%lld", &n) != 1) return 0;
    scanf("%lld %d", &s, &k);
    std::vector<long long> moves(k);
    for (auto &d : moves) scanf("%lld", &d);
    int half = k / 2;
    // the depths the first half of the moves can reach without leaving
    // [0, n]; equal depths are kept once
    start = {s};
    for (int i = 0; i < half; i++) {
        std::vector<long long> next;
        for (long long p : start) {
            if (p + moves[i] <= n) next.push_back(p + moves[i]);
            if (p - moves[i] >= 0) next.push_back(p - moves[i]);
        }
        std::sort(next.begin(), next.end());
        next.erase(std::unique(next.begin(), next.end()), next.end());
        start = next;
    }
    rest.assign(moves.begin() + half, moves.end());
    shallowest = n + 1;
    deepest = -1;
    walk(0, 0, 0, 0);
    printf("%lld %lld\n", shallowest, deepest);
    return 0;
}
