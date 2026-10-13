#include <cmath>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    // rows A x = 1: every player move then earns the same; x scaled to sum 1 is the answer
    vector<vector<double>> rows(n, vector<double>(n + 1, 1.0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%lf", &rows[i][j]);
    for (int col = 0; col < n; col++) {
        int pivot = col;
        for (int r = col + 1; r < n; r++)
            if (fabs(rows[r][col]) > fabs(rows[pivot][col]))
                pivot = r;
        swap(rows[col], rows[pivot]);
        for (int r = col + 1; r < n; r++) {
            double f = rows[r][col] / rows[col][col];
            for (int j = col; j <= n; j++)
                rows[r][j] -= f * rows[col][j];
        }
    }
    vector<double> x(n);
    double total = 0;
    for (int i = n - 1; i >= 0; i--) {
        double s = rows[i][n];
        for (int j = i + 1; j < n; j++)
            s -= rows[i][j] * x[j];
        x[i] = s / rows[i][i];
        total += x[i];
    }
    for (int i = 0; i < n; i++)
        printf("%.5f\n", x[i] / total);
}
