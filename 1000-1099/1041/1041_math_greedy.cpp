#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <random>
#include <vector>

// independence is tested modulo a prime drawn at random from [2^30, 2^31): a set
// independent modulo a prime is independent over the rationals, and an input can
// beat a fixed prime that divides one of its minors, but not a random one
const int64_t LOW = 1LL << 30, HIGH = 1LL << 31;
int64_t P;

bool isPrime(int64_t x) {
    for (int64_t d = 2; d * d <= x; d++)
        if (x % d == 0)
            return false;
    return true;
}

int64_t power(int64_t b, int64_t e) {
    int64_t r = 1;
    for (b %= P; e > 0; e /= 2, b = b * b % P)
        if (e % 2 == 1)
            r = r * b % P;
    return r;
}

int main() {
    std::mt19937_64 rng(std::chrono::steady_clock::now().time_since_epoch().count());
    do
        P = LOW + (int64_t)(rng() % (HIGH - LOW));
    while (!isPrime(P));
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
