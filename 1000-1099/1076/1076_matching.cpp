#include <climits>
#include <cstdio>
#include <vector>

// smallest total cost of a perfect matching of rows to columns, with
// potentials u, v kept so that reduced costs stay non-negative
long long hungarian(const std::vector<std::vector<int>> &cost, int n) {
    std::vector<long long> u(n + 1), v(n + 1);
    std::vector<int> owner(n + 1), way(n + 1);
    for (int row = 1; row <= n; row++) {
        owner[0] = row;
        int col = 0;
        std::vector<long long> low(n + 1, LLONG_MAX);
        std::vector<bool> used(n + 1, false);
        do {
            used[col] = true;
            int r = owner[col], next = 0;
            long long delta = LLONG_MAX;
            for (int j = 1; j <= n; j++)
                if (!used[j]) {
                    long long cur = cost[r - 1][j - 1] - u[r] - v[j];
                    if (cur < low[j])
                        low[j] = cur, way[j] = col;
                    if (low[j] < delta)
                        delta = low[j], next = j;
                }
            for (int j = 0; j <= n; j++)
                if (used[j])
                    u[owner[j]] += delta, v[j] -= delta;
                else
                    low[j] -= delta;
            col = next;
        } while (owner[col] != 0);
        while (col) {
            int prev = way[col];
            owner[col] = owner[prev];
            col = prev;
        }
    }
    return -v[0];
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    std::vector<std::vector<int>> cost(n, std::vector<int>(n));
    long long total = 0;
    for (auto &row : cost)
        for (int &x : row) {
            scanf("%d", &x);
            total += x;
            // type j stays in container i; everything else in its column moves
            x = -x;
        }
    printf("%lld\n", total + hungarian(cost, n));
}
