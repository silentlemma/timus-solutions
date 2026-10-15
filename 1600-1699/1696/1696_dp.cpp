#include <cstdio>
#include <vector>

typedef long long ll;

int main() {
    int n, k;
    ll p;
    scanf("%d %d %lld", &n, &k, &p);
    // salaries by rank must avoid a strictly decreasing triple; the state is
    // a, the largest salary so far, and b, the largest salary that follows a
    // larger one (0 if none); ways[a][b] counts such prefixes modulo p
    std::vector<std::vector<ll>> ways(k + 1, std::vector<ll>(k + 1, 0)), next = ways;
    for (int z = 1; z <= k; z++) {
        ways[z][0] = 1 % p;
    }
    for (int step = 1; step < n; step++) {
        for (auto& row : next) {
            std::fill(row.begin(), row.end(), 0);
        }
        // a new salary z is allowed when z >= b, and turns (a, b) into (a, z) if
        // z < a, or into (z, b) if z >= a
        // z < a: (a, b) -> (a, z) for every b <= z, a prefix sum along the row
        for (int a = 1; a <= k; a++) {
            ll running = 0;
            for (int c = 0; c < a; c++) {
                running = (running + ways[a][c]) % p;
                if (c > 0) {
                    next[a][c] = running;
                }
            }
        }
        // z >= a: (a, b) -> (z, b) for every a <= z, a prefix sum down the column
        for (int b = 0; b < k; b++) {
            ll running = 0;
            for (int z = b + 1; z <= k; z++) {
                running = (running + ways[z][b]) % p;
                next[z][b] = (next[z][b] + running) % p;
            }
        }
        ways.swap(next);
    }
    ll total = 0;
    for (const auto& row : ways) {
        for (ll x : row) {
            total = (total + x) % p;
        }
    }
    // month total + 1 counted from the first month, numbered 1..p in its year
    printf("%lld\n", total + 1);
}
