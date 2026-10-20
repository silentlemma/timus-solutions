#include <cstdio>
#include <string>
#include <vector>

typedef unsigned long long u64;

constexpr int SMALL = 60;  // only boxes up to the number of bits can receive extra bottles

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    std::vector<std::vector<u64>> binom(n + 1, std::vector<u64>(n + 1, 0));
    for (int i = 0; i <= n; i++) {
        binom[i][0] = 1;
        for (int j = 1; j <= i; j++) binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
    }
    u64 top = (1ULL << n) - 1;
    int last = top < (u64)SMALL ? (int)top : SMALL;
    // Box k gets one bottle for every bottle placed in a box j != k with
    // popcount(j) = k; boxes above 60 hold only their own one, and the small
    // boxes are filled from the top down, as popcount(j) < j for j > 1.
    std::vector<u64> count(last + 1, 1);
    for (int k = last; k >= 1; k--) {
        u64 total = 1 + (k <= n ? binom[n][k] : 0) - (k == 1);
        for (int j = k + 1; j <= last; j++)
            if (__builtin_popcount(j) == k) total += count[j] - 1;
        count[k] = total;
    }
    std::string out;
    for (int i = 0; i < q; i++) {
        u64 a;
        scanf("%llu", &a);
        if (i) out += ' ';
        out += std::to_string(a <= (u64)last ? count[a] : 1ULL);
    }
    puts(out.c_str());
    return 0;
}
