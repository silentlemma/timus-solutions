#include <cstdio>

// scanf and printf instead of iostream
int main() {
    int capacity, minutes;
    if (scanf("%d %d", &capacity, &minutes) != 2)
        return 0;
    int jam = 0;
    for (int i = 0; i < minutes; ++i) {
        int cars;
        if (scanf("%d", &cars) != 1)
            return 0;
        // the light lets capacity cars through, but never more than are waiting
        jam += cars - capacity;
        if (jam < 0)
            jam = 0;
    }
    printf("%d\n", jam);
    return 0;
}
