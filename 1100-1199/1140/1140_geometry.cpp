#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    long long sx = 0, sy = 0, sz = 0;
    for (int k = 0; k < n; k++) {
        char d;
        long long len;
        if (scanf(" %c %lld", &d, &len) != 2)
            return 0;
        (d == 'X' ? sx : d == 'Y' ? sy : sz) += len;
    }
    // a step along Y is a step along X and one along Z, so the walk ends at
    // a X + b Z; going back with m steps along Y costs |a - m| + |m| + |b - m|,
    // which is smallest at the median of a, 0 and b
    long long a = sx + sy, b = sz + sy;
    long long m = std::max(std::min(a, b), std::min(std::max(a, b), 0LL));
    std::vector<std::pair<char, long long>> back = {{'X', m - a}, {'Y', -m}, {'Z', m - b}};
    back.erase(std::remove_if(back.begin(), back.end(), [](auto &p) { return p.second == 0; }),
               back.end());
    printf("%d\n", (int)back.size());
    for (auto [d, len] : back)
        printf("%c %lld\n", d, len);
}
