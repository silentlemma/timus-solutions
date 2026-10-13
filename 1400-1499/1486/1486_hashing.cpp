#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

typedef unsigned long long ull;
// two hashes modulo two primes, packed into one 64-bit key
const ull MOD1 = 1000000007, MOD2 = 998244353;
const ull ROW1 = 131, ROW2 = 137, COL1 = 1009, COL2 = 1013;
const int HALF = 32;

int n, m;
vector<string> grid;

ull power(ull b, int e, ull mod) {
    ull r = 1;
    for (; e > 0; e--)
        r = r * b % mod;
    return r;
}

bool same(int r1, int c1, int r2, int c2, int k) {
    for (int t = 0; t < k; t++)
        if (grid[r1 + t].compare(c1, k, grid[r2 + t], c2, k) != 0)
            return false;
    return true;
}

// two different equal k x k squares, as top-left corners
bool find(int k, int &r1, int &c1, int &r2, int &c2) {
    int width = m - k + 1;
    vector<vector<ull>> rows(n, vector<ull>(width));
    ull p1 = power(ROW1, k, MOD1), p2 = power(ROW2, k, MOD2);
    for (int i = 0; i < n; i++) {
        ull h1 = 0, h2 = 0;
        for (int j = 0; j < m; j++) {
            ull c = grid[i][j];
            h1 = (h1 * ROW1 + c) % MOD1;
            h2 = (h2 * ROW2 + c) % MOD2;
            if (j >= k) {
                ull old = grid[i][j - k];
                h1 = (h1 + MOD1 - old * p1 % MOD1) % MOD1;
                h2 = (h2 + MOD2 - old * p2 % MOD2) % MOD2;
            }
            if (j >= k - 1)
                rows[i][j - k + 1] = h1 << HALF | h2;
        }
    }
    p1 = power(COL1, k, MOD1), p2 = power(COL2, k, MOD2);
    vector<ull> col1(width, 0), col2(width, 0);
    vector<pair<ull, int>> keys;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < width; j++) {
            ull a1 = rows[i][j] >> HALF, a2 = rows[i][j] & ((1ULL << HALF) - 1);
            col1[j] = (col1[j] * COL1 + a1) % MOD1;
            col2[j] = (col2[j] * COL2 + a2) % MOD2;
            if (i >= k) {
                ull b1 = rows[i - k][j] >> HALF, b2 = rows[i - k][j] & ((1ULL << HALF) - 1);
                col1[j] = (col1[j] + MOD1 - b1 * p1 % MOD1) % MOD1;
                col2[j] = (col2[j] + MOD2 - b2 * p2 % MOD2) % MOD2;
            }
            if (i >= k - 1)
                keys.push_back({col1[j] << HALF | col2[j], (i - k + 1) * width + j});
        }
    sort(keys.begin(), keys.end());
    for (size_t t = 1; t < keys.size(); t++)
        if (keys[t].first == keys[t - 1].first) {
            r1 = keys[t - 1].second / width, c1 = keys[t - 1].second % width;
            r2 = keys[t].second / width, c2 = keys[t].second % width;
            if (same(r1, c1, r2, c2, k))
                return true;
        }
    return false;
}

int main() {
    scanf("%d %d", &n, &m);
    grid.resize(n);
    vector<char> buf(m + 2);
    for (auto &line : grid) {
        scanf("%s", buf.data());
        line = buf.data();
    }
    // equal k x k squares contain equal (k - 1) x (k - 1) ones, so the
    // largest size can be found by binary search
    int lo = 1, hi = min(n, m), best = 0, br1 = 0, bc1 = 0, br2 = 0, bc2 = 0;
    while (lo <= hi) {
        int k = (lo + hi) / 2, r1, c1, r2, c2;
        if (find(k, r1, c1, r2, c2)) {
            best = k, br1 = r1, bc1 = c1, br2 = r2, bc2 = c2;
            lo = k + 1;
        } else
            hi = k - 1;
    }
    if (!best) {
        puts("0");
        return 0;
    }
    printf("%d\n%d %d\n%d %d\n", best, br1 + 1, bc1 + 1, br2 + 1, bc2 + 1);
}
