#include <cstdio>

const int POINTS = 5;
// point k has index k - 1: start 0, middle points FIRST_MIDDLE..LAST_MIDDLE, finish END
const int FIRST_MIDDLE = 1, POINT_3 = 2, LAST_MIDDLE = 3, END = 4;

int main() {
    int d[POINTS][POINTS];
    for (auto &row : d)
        for (int &x : row)
            scanf("%d", &x);
    // points 2, 3 and 4 (indices 1, 2, 3) come in any order, except that 3
    // may not be the last of them
    int best = -1, route[POINTS] = {};
    for (int a = FIRST_MIDDLE; a <= LAST_MIDDLE; a++)
        for (int b = FIRST_MIDDLE; b <= LAST_MIDDLE; b++)
            for (int c = FIRST_MIDDLE; c <= LAST_MIDDLE; c++) {
                if (a == b || a == c || b == c || c == POINT_3)
                    continue;
                int cost = d[0][a] + d[a][b] + d[b][c] + d[c][END];
                if (best < 0 || cost < best) {
                    best = cost;
                    int found[POINTS] = {0, a, b, c, END};
                    for (int i = 0; i < POINTS; i++)
                        route[i] = found[i];
                }
            }
    printf("%d\n", best);
    for (int i = 0; i < POINTS; i++)
        printf("%d%c", route[i] + 1, i + 1 < POINTS ? ' ' : '\n');
}
