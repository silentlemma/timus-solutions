#include <algorithm>
#include <tuple>
#include <cstdio>
#include <cstdlib>
#include <functional>
#include <vector>
using namespace std;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    vector<int> heights(n * n);
    for (int &h : heights)
        if (scanf("%d", &h) != 1)
            return 0;
    sort(heights.rbegin(), heights.rend());
    int mid = n / 2;
    // cells by (nearer, farther) distance from the centre row and column:
    // along any row or column this grows outwards on each side
    vector<tuple<int, int, int>> cells;  // nearer, farther, cell number
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++) {
            int a = abs(r - mid), b = abs(c - mid);
            cells.push_back({min(a, b), max(a, b), r * n + c});
        }
    sort(cells.begin(), cells.end());
    vector<vector<int>> grid(n, vector<int>(n));
    for (int k = 0; k < n * n; k++)
        grid[get<2>(cells[k]) / n][get<2>(cells[k]) % n] = heights[k];
    for (int r = 0; r < n; r++)
        for (int c = 0; c < n; c++)
            printf("%d%c", grid[r][c], c + 1 < n ? ' ' : '\n');
}
