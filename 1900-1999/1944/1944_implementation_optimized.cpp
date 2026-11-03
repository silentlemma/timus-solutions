#include <algorithm>
#include <cstdio>

const int MAX_POINTS = 250, MAX_COORD = 100, SPAN = 2 * MAX_COORD + 1;
int points[MAX_POINTS];
char vertical[SPAN], row[SPAN];

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int left = 0, right = 0, lower = 0, upper = 0;
    for (int i = 0; i < n; i++) {
        int x, y;
        if (scanf("%d %d", &x, &y) != 2)
            return 0;
        left = std::min(left, x);
        right = std::max(right, x);
        lower = std::min(lower, y);
        upper = std::max(upper, y);
        // Each shifted coordinate is in[0,SPAN), so division restores y.
        points[i] = (y + MAX_COORD) * SPAN + x + MAX_COORD;
    }
    std::sort(points, points + n);
    int width = right - left + 1, next = n - 1;
    std::fill(vertical, vertical + width, '.');
    vertical[-left] = '|';
    for (int y = upper; y >= lower; y--) {
        if (y == 0) {
            std::fill(row, row + width, '-');
            row[-left] = '+';
        } else
            std::copy(vertical, vertical + width, row);
        while (next >= 0 && points[next] / SPAN == y + MAX_COORD) {
            int x = points[next--] % SPAN - MAX_COORD;
            row[x - left] = '*';
        }
        fwrite(row, 1, width, stdout);
        putchar('\n');
    }
}
