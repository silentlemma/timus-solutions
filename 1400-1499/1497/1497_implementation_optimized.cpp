#include <cstdio>
#include <utility>

constexpr int MAX_WIDTH = 1000;
static char first[MAX_WIDTH + 1], second[MAX_WIDTH + 1];

int main() {
    int size;
    if (std::scanf("%d", &size) != 1)
        return 0;
    char *previous = first, *current = second;
    bool left = true, right = true, up = true, down = true;
    for (int y = 0; y < size; ++y) {
        std::scanf("%s", current);
        for (int x = 0; x < size; ++x) {
            const char color = current[x];
            if (x > 0 && current[x - 1] != color) {
                left &= color == '0';
                right &= color == '1';
            }
            if (y > 0 && previous[x] != color) {
                up &= color == '0';
                down &= color == '1';
            }
        }
        if (!(left || right || up || down)) {
            std::puts("No");
            return 0;
        }
        std::swap(previous, current);
    }
    std::puts("Yes");
}
