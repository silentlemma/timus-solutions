#include <cstdio>
#include <string>
#include <vector>

const int FAR = 1 << 20;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<std::vector<int>> a(n, std::vector<int>(n)), d(n, std::vector<int>(n, FAR));
    for (auto &row : a)
        for (int &v : row) scanf("%d", &v);
    // every road must cost at least the table in both directions, so the
    // cheapest roads allowed are taken: a free road where the table says 0
    // both ways, a road with a board seen from i where it says 1 and 0
    std::vector<std::string> grid(n, std::string(n, '0'));
    for (int i = 0; i < n; i++) {
        d[i][i] = 0;
        for (int j = 0; j < n; j++) {
            if (i == j || a[i][j] + a[j][i] > 1) continue;
            d[i][j] = a[i][j];
            grid[i][j] = a[i][j] ? '2' : '1';
        }
    }
    // these roads give the smallest costs any network can have, so the table
    // is right exactly when they give it
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];
    if (d != a) {
        puts("NO");
        return 0;
    }
    puts("YES");
    for (const std::string &row : grid) puts(row.c_str());
    return 0;
}
