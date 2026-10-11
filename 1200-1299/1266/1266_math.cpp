#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    // g[a][b]: total conductance between two nodes
    std::vector<std::vector<double>> g(n, std::vector<double>(n));
    for (int i = 0; i < m; i++) {
        int a, b, r;
        scanf("%d %d %d", &a, &b, &r);
        g[a - 1][b - 1] += 1.0 / r;
        g[b - 1][a - 1] += 1.0 / r;
    }
    // nodes cut off from node 1 carry no current and would make the
    // system singular
    std::vector<bool> seen(n);
    std::vector<int> stack = {0}, inner;
    seen[0] = true;
    while (!stack.empty()) {
        int u = stack.back();
        stack.pop_back();
        for (int v = 0; v < n; v++)
            if (g[u][v] > 0 && !seen[v]) {
                seen[v] = true;
                stack.push_back(v);
            }
    }
    for (int v = 1; v < n - 1; v++)
        if (seen[v])
            inner.push_back(v);
    // Kirchhoff at each inner node with potential 1 at node 1, 0 at node N
    int k = inner.size();
    std::vector<std::vector<double>> a(k, std::vector<double>(k + 1));
    for (int i = 0; i < k; i++) {
        int u = inner[i];
        for (int v = 0; v < n; v++)
            a[i][i] += g[u][v];
        for (int j = 0; j < k; j++)
            a[i][j] -= g[u][inner[j]];
        a[i][k] = g[u][0];
    }
    for (int c = 0; c < k; c++) {
        int p = c;
        for (int r = c + 1; r < k; r++)
            if (std::fabs(a[r][c]) > std::fabs(a[p][c]))
                p = r;
        std::swap(a[c], a[p]);
        for (int r = 0; r < k; r++)
            if (r != c && a[r][c] != 0) {
                double f = a[r][c] / a[c][c];
                for (int j = c; j <= k; j++)
                    a[r][j] -= f * a[c][j];
            }
    }
    std::vector<double> volt(n);
    volt[0] = 1;
    for (int i = 0; i < k; i++)
        volt[inner[i]] = a[i][k] / a[i][i];
    double current = 0;
    for (int v = 1; v < n; v++)
        current += g[0][v] * (1 - volt[v]);
    printf("%.2f\n", 1 / current);
}
