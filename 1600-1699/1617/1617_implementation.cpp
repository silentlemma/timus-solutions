#include <cstdio>

const int PAIRS_PER_CAR = 4;
const int LARGEST = 700; // the widest diameter in millimetres

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    int count[LARGEST + 1] = {};
    for (int i = 0; i < n; i++) {
        int d;
        if (scanf("%d", &d) == 1)
            count[d]++;
    }
    // each diameter equips as many cars as it has full sets of four pairs
    int cars = 0;
    for (int d = 0; d <= LARGEST; d++)
        cars += count[d] / PAIRS_PER_CAR;
    printf("%d\n", cars);
}
