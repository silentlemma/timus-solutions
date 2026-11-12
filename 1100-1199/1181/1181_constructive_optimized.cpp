#include <array>
#include <cstdio>

constexpr int MAX_VERTICES = 1000;
constexpr int COLOR_COUNT = 3, TRIANGLE_SIZE = 3;
constexpr int COLOR_BUFFER_SIZE = MAX_VERTICES + 1;

int main() {
    int n;
    char text[COLOR_BUFFER_SIZE];
    scanf("%d%1000s", &n, text);
    std::array<int, MAX_VERTICES> color{}, left{}, right{};
    std::array<bool, MAX_VERTICES> alive{};
    std::array<int, COLOR_COUNT> counts{};
    std::array<int, MAX_VERTICES + 2 * MAX_VERTICES> pending{};
    int head = 0, tail = 0;
    for (int v = 0; v < n; ++v) {
        color[v] = text[v] == 'R' ? 0 : text[v] == 'G' ? 1 : 2;
        ++counts[color[v]];
        left[v] = (v + n - 1) % n;
        right[v] = (v + 1) % n;
        alive[v] = true;
    }
    for (int v = 0; v < n; ++v) {
        if (color[left[v]] != color[right[v]])
            pending[tail++] = v;
    }
    printf("%d\n", n - TRIANGLE_SIZE);
    int remaining = n;
    while (remaining > TRIANGLE_SIZE) {
        if (counts[0] == 1 || counts[1] == 1 || counts[2] == 1) {
            int anchor = 0;
            while (!alive[anchor] || counts[color[anchor]] != 1)
                ++anchor;
            for (int v = right[right[anchor]]; right[v] != anchor; v = right[v]) {
                printf("%d %d\n", anchor + 1, v + 1);
            }
            break;
        }
        int v = pending[head++];
        if (!alive[v] || color[left[v]] == color[right[v]])
            continue;
        int before = left[v], after = right[v];
        printf("%d %d\n", before + 1, after + 1);
        alive[v] = false;
        right[before] = after;
        left[after] = before;
        --counts[color[v]];
        --remaining;
        // Each cut adds only its two neighbours: at most 3*n queue entries in total.
        pending[tail++] = before;
        pending[tail++] = after;
    }
}
