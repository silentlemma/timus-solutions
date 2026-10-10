#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

// counts are kept only for every STRIDE-th height, so that the table fits in
// the memory limit; the heights between are recomputed by recursion
const int STRIDE = 4;
// the first line holds N, H and M
const int HEADER = 3;

std::vector<std::vector<long long>> offset; // -1 where nothing is stored
std::vector<long long> memo;

// a tower with h levels whose lowest has m bricks uses at most this many
long long most(long long h, long long m) { return m * h + h * (h - 1) / 2; }

// towers of h levels starting with m bricks that use at most n bricks
long long count(long long n, int h, int m) {
    if (m == 0 || n < m)
        return 0;
    if (h == 1)
        return 1;
    n = std::min(n, most(h, m));
    long long key = h < (int)offset.size() && m < (int)offset[h].size() ? offset[h][m] : -1;
    if (key >= 0 && memo[key + n] >= 0)
        return memo[key + n];
    long long ways = count(n - m, h - 1, m - 1) + count(n - m, h - 1, m + 1);
    if (key >= 0)
        memo[key + n] = ways;
    return ways;
}

int main() {
    long long total;
    int height, base;
    if (scanf("%lld %d %d", &total, &height, &base) != HEADER)
        return 0;
    // offset[h][m] starts the stored counts for h levels and m bricks below,
    // kept only for the widths that a tower can reach at that height
    offset.assign(height + 1, std::vector<long long>(base + height + 2, -1));
    long long size = 0;
    for (int h = STRIDE; h <= height; h += STRIDE) {
        int depth = height - h, low = base - depth;
        while (low < 1)
            low += 2;
        for (int m = low; m <= base + depth; m += 2) {
            offset[h][m] = size;
            size += most(h, m) + 1;
        }
    }
    memo.assign(size, -1);
    std::string out = std::to_string(count(total, height, base)) + "\n";
    long long k;
    while (scanf("%lld", &k) == 1 && k > 0) {
        // lexicographic order: the narrower next level comes first
        long long n = total;
        int m = base;
        out += std::to_string(m);
        for (int h = height; h > 1; h--) {
            long long fewer = count(n - m, h - 1, m - 1);
            n -= m;
            if (k <= fewer)
                m--;
            else {
                k -= fewer;
                m++;
            }
            out += " " + std::to_string(m);
        }
        out += "\n";
    }
    fputs(out.c_str(), stdout);
}
