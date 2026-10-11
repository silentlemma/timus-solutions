#include <algorithm>
#include <cstdio>

const int FLOORS = 1000;
// ten eggs already allow a binary search over all the floors
const int EGGS = 10;

int best[EGGS + 1][FLOORS + 1];

int main() {
    // best[k][n]: the fewest drops that settle n floors with k eggs; with d
    // drops and k eggs one can tell apart reach(d, k) floors, where
    // reach(d, k) = reach(d - 1, k - 1) + reach(d - 1, k) + 1
    int reach[EGGS + 1] = {0}, next[EGGS + 1] = {0};
    for (int d = 1; reach[1] < FLOORS; d++) {
        for (int k = 1; k <= EGGS; k++) {
            next[k] = std::min(FLOORS, reach[k - 1] + reach[k] + 1);
            for (int n = reach[k] + 1; n <= next[k]; n++) {
                best[k][n] = d;
            }
        }
        std::copy(next, next + EGGS + 1, reach);
    }
    int eggs, floors;
    while (scanf("%d %d", &eggs, &floors) == 2 && (eggs != 0 || floors != 0)) {
        printf("%d\n", best[std::min(eggs, EGGS)][floors]);
    }
}
