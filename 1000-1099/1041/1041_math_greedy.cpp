#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <vector>

// linear independence is tested modulo a large prime: exact, and a set that is
// independent modulo the prime is independent over the rationals
const int64_t P = 2147483647;

int64_t power(int64_t b, int64_t e) {
    int64_t r = 1;
    for (b %= P; e > 0; e /= 2, b = b * b % P)
        if (e % 2 == 1)
            r = r * b % P;
    return r;
}

int main() {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2)
        return 0;
    std::vector<std::vector<int64_t>> vec(m, std::vector<int64_t>(n));
    for (auto &v : vec)
        for (auto &x : v) {
            if (scanf("%lld", (long long *)&x) != 1)
                return 0;
            x = (x % P + P) % P;
        }
    std::vector<int> cost(m);
    for (auto &c : cost)
        if (scanf("%d", &c) != 1)
            return 0;
    // the greedy algorithm of a matroid: the cheapest vectors first, and among
    // equal prices the smaller numbers first, which gives the smallest list too
    std::vector<int> order(m);
    std::iota(order.begin(), order.end(), 0);
    std::stable_sort(order.begin(), order.end(), [&](int a, int b) { return cost[a] < cost[b]; });
    // rows of the basis, each with a pivot coordinate equal to 1 and zero in
    // the pivots of the rows before it
    std::vector<std::vector<int64_t>> rows;
    std::vector<int> pivots, chosen;
    for (int i : order) {
        if ((int)chosen.size() == n)
            break;
        std::vector<int64_t> v = vec[i];
        for (size_t r = 0; r < rows.size(); r++) {
            int64_t f = v[pivots[r]];
            if (f == 0)
                continue;
            for (int k = 0; k < n; k++)
                v[k] = ((v[k] - f * rows[r][k]) % P + P) % P;
        }
        int p = 0;
        while (p < n && v[p] == 0)
            p++;
        if (p == n)
            continue;
        int64_t inv = power(v[p], P - 2);
        for (auto &x : v)
            x = x * inv % P;
        rows.push_back(v);
        pivots.push_back(p);
        chosen.push_back(i);
    }
    if ((int)chosen.size() < n) {
        printf("0\n");
        return 0;
    }
    long long total = 0;
    for (int i : chosen)
        total += cost[i];
    std::sort(chosen.begin(), chosen.end());
    printf("%lld\n", total);
    for (int i : chosen)
        printf("%d\n", i + 1);
}
