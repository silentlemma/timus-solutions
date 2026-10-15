#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const long long MOD = 1000000000;

int main() {
    int n, m;
    if (!(cin >> n >> m))
        return 0;
    vector<string> grid(n);
    for (auto &row : grid)
        cin >> row;
    vector<vector<int>> id(n, vector<int>(m, -1));
    int v = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (grid[i][j] == '.')
                id[i][j] = v++;
    // the Laplacian of the bedroom graph; by the matrix-tree theorem any
    // cofactor counts its spanning trees (0 when it is disconnected)
    vector<vector<long long>> lap(v, vector<long long>(v, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            int u = id[i][j];
            if (u < 0)
                continue;
            for (int w : {i + 1 < n ? id[i + 1][j] : -1, j + 1 < m ? id[i][j + 1] : -1})
                if (w >= 0) {
                    lap[u][u]++, lap[w][w]++;
                    lap[u][w]--, lap[w][u]--;
                }
        }
    int size = v - 1;
    vector<vector<long long>> a(size, vector<long long>(size));
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            a[i][j] = (lap[i][j] % MOD + MOD) % MOD;
    // Elimination by Euclid's algorithm on rows: it only subtracts multiples
    // of rows and swaps them, so it works modulo 10^9, which is not prime.
    long long det = 1;
    for (int k = 0; k < size; k++) {
        for (int i = k + 1; i < size; i++)
            while (a[i][k] != 0) {
                long long q = a[k][k] / a[i][k];
                for (int j = k; j < size; j++)
                    a[k][j] = ((a[k][j] - q * a[i][j]) % MOD + MOD) % MOD;
                swap(a[k], a[i]);
                det = (MOD - det) % MOD;
            }
        det = det * a[k][k] % MOD;
    }
    printf("%lld\n", det);
}
