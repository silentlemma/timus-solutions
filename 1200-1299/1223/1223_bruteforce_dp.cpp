#include <algorithm>
#include <cstdio>

const int FLOORS = 1000, EGGS = 10;
int best[EGGS + 1][FLOORS + 1];

int main() {
    for (int floors = 1; floors <= FLOORS; floors++)
        best[1][floors] = floors;
    // Ten eggs suffice for binary search over all allowed floors.
    // Try every first drop and minimize its worst of the two outcomes.
    for (int eggs = 2; eggs <= EGGS; eggs++)
        for (int floors = 1; floors <= FLOORS; floors++) {
            best[eggs][floors] = floors;
            for (int first = 1; first <= floors; first++)
                best[eggs][floors] =
                    std::min(best[eggs][floors],
                             1 + std::max(best[eggs - 1][first - 1], best[eggs][floors - first]));
        }
    int eggs, floors;
    while (scanf("%d %d", &eggs, &floors) == 2 && (eggs || floors))
        printf("%d\n", best[std::min(eggs, EGGS)][floors]);
}
