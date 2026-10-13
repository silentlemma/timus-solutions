#include <cstdint>
#include <cstdio>
#include <vector>

using namespace std;

// non-negative integers as base 10^9 limbs, the lowest first
typedef vector<uint32_t> Big;
const uint32_t BASE = 1000000000;

// a += b * factor, with factor below 2^64
void addMul(Big &a, const Big &b, uint64_t factor) {
    if (a.size() < b.size())
        a.resize(b.size(), 0);
    unsigned __int128 carry = 0;
    for (size_t i = 0; i < a.size(); i++) {
        unsigned __int128 v = carry + a[i] + (i < b.size() ? (unsigned __int128)b[i] * factor : 0);
        a[i] = (uint32_t)(v % BASE);
        carry = v / BASE;
    }
    while (carry) {
        a.push_back((uint32_t)(carry % BASE));
        carry /= BASE;
    }
}

int main() {
    int m, n, k;
    scanf("%d %d %d", &m, &n, &k);
    vector<vector<uint64_t>> binom(m + 1, vector<uint64_t>(m + 1, 0));
    for (int i = 0; i <= m; i++) {
        binom[i][0] = 1;
        for (int j = 1; j <= i; j++)
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
    }
    // step[c][d]: ways to follow a column with c ones by one with d ones,
    // turning at most k zeros into ones (at most 2^40 of them)
    vector<vector<uint64_t>> step(m + 1, vector<uint64_t>(m + 1, 0));
    for (int c = 0; c <= m; c++)
        for (int t = 0; t <= k && t <= m - c; t++)
            for (int s = 0; s <= c; s++)
                step[c][s + t] += binom[m - c][t] * binom[c][s];
    // ways[c]: fillings of the columns so far whose last column has c ones
    vector<Big> ways(m + 1);
    for (int c = 0; c <= m; c++)
        addMul(ways[c], Big{1}, binom[m][c]);
    for (int col = 1; col < n; col++) {
        vector<Big> next(m + 1);
        for (int c = 0; c <= m; c++)
            for (int d = 0; d <= m; d++)
                if (step[c][d])
                    addMul(next[d], ways[c], step[c][d]);
        ways = next;
    }
    Big total;
    for (const Big &w : ways)
        addMul(total, w, 1);
    while (total.size() > 1 && total.back() == 0)
        total.pop_back();
    printf("%u", total.empty() ? 0 : total.back());
    for (size_t i = total.size() - 1; i-- > 0;)
        printf("%09u", total[i]);
    printf("\n");
}
