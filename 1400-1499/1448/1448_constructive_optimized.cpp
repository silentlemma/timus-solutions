#include <algorithm>
#include <cstdio>

constexpr int FULL = 100;
constexpr int BLOCK = 8192 / FULL * FULL;

int main() {
    int count, brightness;
    if (std::scanf("%d%d", &count, &brightness) != 2)
        return 0;

    char lamps[BLOCK];
    int remainder = 0;
    for (int i = 0; i < FULL; ++i) {
        remainder += brightness;
        const bool on = remainder >= FULL;
        lamps[i] = on ? '1' : '0';
        if (on)
            remainder -= FULL;
    }
    // Every block starts at the same phase of the repeating pattern.
    for (int i = FULL; i < BLOCK; i += FULL)
        std::copy_n(lamps, FULL, lamps + i);
    while (count > 0) {
        const int length = std::min(count, BLOCK);
        std::fwrite(lamps, 1, length, stdout);
        count -= length;
    }
    std::putchar('\n');
}
