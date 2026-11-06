#include <array>
#include <charconv>
#include <cstdint>
#include <cstdio>
#include <cstdlib>

constexpr int REACH = 5;
constexpr int DIAMOND_SIDES = 4;
constexpr int MAX_SIDE = 150;
constexpr int STRIDE = MAX_SIDE + 2 * REACH;
constexpr int FIELD_WIDTH = 5;

int main() {
    int height, width;
    if (std::scanf("%d%d", &height, &width) != 2) {
        return 0;
    }
    // The zero border makes every ring a list of unconditional accesses.
    std::array<std::uint16_t, STRIDE * STRIDE> grid{};
    for (int row = REACH; row < height + REACH; ++row) {
        for (int col = REACH; col < width + REACH; ++col) {
            unsigned value;
            std::scanf("%u", &value);
            grid[row * STRIDE + col] = static_cast<std::uint16_t>(value);
        }
    }
    std::array<std::array<int, DIAMOND_SIDES * REACH>, REACH> rings;
    for (int d = 1; d <= REACH; ++d) {
        int end = 0;
        for (int row = -d; row <= d; ++row) {
            const int col = d - std::abs(row);
            rings[d - 1][end++] = row * STRIDE + col;
            if (col != 0) {
                rings[d - 1][end++] = row * STRIDE - col;
            }
        }
    }
    std::array<char, MAX_SIDE * FIELD_WIDTH> output;
    for (int row = REACH; row < height + REACH; ++row) {
        char *end = output.data();
        for (int col = REACH; col < width + REACH; ++col) {
            const int cell = row * STRIDE + col;
            int mask = -1;
            if (grid[cell] == 0) {
                mask = 0;
                for (int d = 1; d <= REACH && mask == 0; ++d) {
                    for (int i = 0; i < DIAMOND_SIDES * d; ++i) {
                        mask |= grid[cell + rings[d - 1][i]];
                    }
                }
            }
            end = std::to_chars(end, output.data() + output.size(), mask).ptr;
            *end++ = col + 1 == width + REACH ? '\n' : ' ';
        }
        std::fwrite(output.data(), 1, end - output.data(), stdout);
    }
}
