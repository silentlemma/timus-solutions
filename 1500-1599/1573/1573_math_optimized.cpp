#include <cstdio>

int main() {
    int blue, red, yellow, count;
    std::scanf("%d%d%d%d", &blue, &red, &yellow, &count);
    // yellow is the longest allowed name: six letters plus the terminator.
    constexpr int COLOR_CAPACITY = 7;
    // one reagent from each needed bag, chosen independently
    // three distinct colors, each with at most 100 choices, give at most 1000000.
    int ways = 1;
    for (int i = 0; i < count; ++i) {
        char color[COLOR_CAPACITY];
        std::scanf("%6s", color);
        // the three color names have different initials.
        if (color[0] == 'B')
            ways *= blue;
        else if (color[0] == 'R')
            ways *= red;
        else
            ways *= yellow;
    }
    std::printf("%d\n", ways);
}
