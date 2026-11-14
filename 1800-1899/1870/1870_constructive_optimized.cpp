#include <array>
#include <charconv>
#include <cstdio>

namespace {
constexpr int DIVISOR_THREE = 3;
constexpr int BUFFER_SIZE = 8192;
constexpr int ROW_SPACE = 8; // Up to six digits, a separator and the final newline.
} // namespace

int main() {
    int size;
    if (std::scanf("%d", &size) != 1) {
        return 0;
    }
    if (size % 2 == 0 || size % DIVISOR_THREE == 0) {
        std::puts("No");
        return 0;
    }
    std::puts("Yes");
    std::array<char, BUFFER_SIZE> buffer;
    char *current = buffer.data();
    char *const end = buffer.data() + buffer.size();
    // For odd size, the modular placement visits odd rows, then even rows.
    for (int first : {1, 2}) {
        for (int row = first; row <= size; row += 2) {
            if (end - current < ROW_SPACE) {
                std::fwrite(buffer.data(), 1, current - buffer.data(), stdout);
                current = buffer.data();
            }
            if (row != 1) {
                *current++ = ' ';
            }
            current = std::to_chars(current, end, row).ptr;
        }
    }
    *current++ = '\n';
    std::fwrite(buffer.data(), 1, current - buffer.data(), stdout);
}
