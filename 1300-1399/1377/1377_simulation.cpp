#include <cstdio>
#include <cstdlib>
#include <vector>

// east, south, west, north: turning right moves one step along this list
const int DR[] = {0, 1, 0, -1};
const int DC[] = {1, 0, -1, 0};
const int DIRECTIONS = 4;
const int FIELDS = 6;

int main() {
    int n = 0, m = 0, r1 = 0, c1 = 0, r2 = 0, c2 = 0;
    if (scanf("%d %d %d %d %d %d", &n, &m, &r1, &c1, &r2, &c2) != FIELDS)
        return 0;
    // dig the whole spiral, numbering the graves by the night they are dug,
    // with a frame of dug cells around the cemetery standing for the wall
    std::vector<std::vector<int>> night(n + 2, std::vector<int>(m + 2, -1));
    for (int r = 0; r < n + 2; r++)
        night[r][0] = night[r][m + 1] = 0;
    for (int c = 0; c < m + 2; c++)
        night[0][c] = night[n + 1][c] = 0;
    int r = 1, c = 1, d = 0;
    night[1][1] = 1;
    for (int day = 2; day <= n * m; day++) {
        while (night[r + DR[d]][c + DC[d]] >= 0)
            d = (d + 1) % DIRECTIONS;
        r += DR[d];
        c += DC[d];
        night[r][c] = day;
    }
    printf("%d\n", abs(night[r1][c1] - night[r2][c2]));
    return 0;
}
