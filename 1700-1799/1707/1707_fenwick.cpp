#include <cstdio>
#include <string>
#include <vector>

const long long MOD = 200904040963LL;  // the modulus of the hash printed for long experiments
const long long BASE = 7;
const int SHORT = 20;  // experiments up to this length are printed digit by digit
const int CORNERS = 4;
const int OPPOSITE = 3;  // the corner (a - 1, c - 1) among the four of a step

int wrap(long long v, int n) {
    int r = v % n;
    return r < 0 ? r + n : r;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    // the eyes' states are points (s, t); an experiment step asks whether a
    // rectangle holds one, answered by four prefix counts of a sweep over t
    std::vector<std::vector<int>> xs_by_y(n);
    for (int l = 0; l < m; l++) {
        int s0, t0, ds, dt, k;
        scanf("%d %d %d %d %d", &s0, &t0, &ds, &dt, &k);
        for (int i = 0; i < k; i++) {
            xs_by_y[wrap(t0 + (long long)i * dt, n)].push_back(wrap(s0 + (long long)i * ds, n));
        }
    }
    int p;
    scanf("%d", &p);
    std::vector<std::vector<std::pair<int, int>>> asks_by_y(n);
    // count 0 is a fixed zero for the corners outside the grid
    int count = 1;
    std::vector<int> lengths(p);
    std::vector<std::vector<int>> corners(p);
    for (int e = 0; e < p; e++) {
        long long a0, b0, c0, d0, da, db, dc, dd;
        int q;
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld %d", &a0, &b0, &c0, &d0, &da, &db, &dc, &dd,
              &q);
        lengths[e] = q;
        for (int j = 0; j < q; j++) {
            int a = wrap(a0 + j * da, n), b = wrap(b0 + j * db, n);
            int c = wrap(c0 + j * dc, n), d = wrap(d0 + j * dd, n);
            if (a > b) {
                std::swap(a, b);
            }
            if (c > d) {
                std::swap(c, d);
            }
            int xs[CORNERS] = {b, a - 1, b, a - 1};
            int ys[CORNERS] = {d, d, c - 1, c - 1};
            for (int r = 0; r < CORNERS; r++) {
                if (xs[r] < 0 || ys[r] < 0) {
                    corners[e].push_back(0);
                } else {
                    asks_by_y[ys[r]].push_back({xs[r], count});
                    corners[e].push_back(count++);
                }
            }
        }
    }
    std::vector<int> below(count, 0);  // points with s <= x and t <= y for each asked corner
    std::vector<int> tree(n + 1, 0);
    for (int y = 0; y < n; y++) {
        for (int x : xs_by_y[y]) {
            for (int i = x + 1; i <= n; i += i & -i) {
                tree[i]++;
            }
        }
        for (auto& ask : asks_by_y[y]) {
            int total = 0;
            for (int i = ask.first + 1; i > 0; i -= i & -i) {
                total += tree[i];
            }
            below[ask.second] = total;
        }
    }
    for (int e = 0; e < p; e++) {
        const std::vector<int>& c = corners[e];
        std::string bits;
        for (int j = 0; j < lengths[e] * CORNERS; j += CORNERS) {
            int inside = below[c[j]] - below[c[j + 1]] - below[c[j + 2]] + below[c[j + OPPOSITE]];
            bits += inside > 0 ? '1' : '0';
        }
        if (lengths[e] <= SHORT) {
            printf("%s\n", bits.c_str());
        } else {
            long long value = 0;
            for (int j = lengths[e] - 1; j >= 0; j--) {
                value = (value * BASE + (bits[j] - '0')) % MOD;
            }
            printf("%lld\n", value);
        }
    }
}
