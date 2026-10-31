#include <cstdio>

int main() {
    // stdio avoids the fixed iostream allocation; values are printed as exact halves.
    int count, duration, start;
    scanf("%d %d %d", &count, &duration, &start);
    for (int i = 0; i < count; ++i) {
        int other;
        scanf("%d", &other);
        int doubled_time = start + duration + other;
        printf("%d%s", doubled_time / 2, doubled_time % 2 == 0 ? ".000000\n" : ".500000\n");
    }
}
