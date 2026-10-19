#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <string>
#include <unordered_set>
#include <vector>

const int LONGEST = 50;
const int SHIFT = 28;  // star counts fit in 28 bits

uint64_t pairKey(uint64_t first, uint64_t last) { return first << SHIFT | last; }

int main() {
    int n, m;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<uint64_t> stars(n);
    for (auto &s : stars) scanf("%llu", (unsigned long long *)&s);
    scanf("%d", &m);
    std::vector<std::unordered_set<uint64_t>> wanted(LONGEST + 1);
    for (int i = 0; i < m; i++) {
        unsigned long long x, y;
        int d;
        scanf("%llu %llu %d", &x, &y, &d);
        wanted[d].insert(pairKey(x, y));
    }
    // a war of d days ending k days ago began k + d - 1 days ago; reach[k]
    // is the oldest day of a matching war that ends k days ago
    std::vector<int> reach(n, -1);
    for (int d = 2; d <= std::min(LONGEST, n); d++) {
        if (wanted[d].empty()) continue;
        for (int k = 0; k + d <= n; k++) {
            if (wanted[d].count(pairKey(stars[k + d - 1], stars[k]))) {
                reach[k] = std::max(reach[k], k + d - 1);
            }
        }
    }
    std::string out(n, '0');
    int cover = -1;
    for (int k = 0; k < n; k++) {
        cover = std::max(cover, reach[k]);
        if (cover >= k) out[k] = '1';
    }
    puts(out.c_str());
    return 0;
}
