#include <bitset>
#include <cstdio>
#include <utility>
#include <vector>

const int MAX_N = 250;
// bit MAX_N of an equation is its right-hand side
typedef std::bitset<MAX_N + 1> Row;

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // equation v over GF(2): the chosen technicians turn valve v an odd number of times
    std::vector<Row> eq(n);
    for (int t = 0; t < n; t++) {
        int v;
        while (scanf("%d", &v) == 1 && v != -1)
            eq[v - 1][t] = 1;
    }
    for (auto &e : eq)
        e[MAX_N] = 1;
    // Gauss-Jordan elimination: column c ends with a single 1, in its pivot row
    std::vector<int> pivot_of(n, -1);
    int rank = 0;
    for (int c = 0; c < n; c++) {
        int r = rank;
        while (r < n && !eq[r][c])
            r++;
        if (r == n)
            continue;
        std::swap(eq[r], eq[rank]);
        for (int i = 0; i < n; i++)
            if (i != rank && eq[i][c])
                eq[i] ^= eq[rank];
        pivot_of[c] = rank++;
    }
    for (int r = rank; r < n; r++)
        if (eq[r][MAX_N]) {
            printf("No solution\n");
            return 0;
        }
    // independent technicians make the solution unique, so it is also the shortest
    bool first = true;
    for (int c = 0; c < n; c++)
        if (pivot_of[c] >= 0 && eq[pivot_of[c]][MAX_N]) {
            printf(first ? "%d" : " %d", c + 1);
            first = false;
        }
    printf("\n");
}
