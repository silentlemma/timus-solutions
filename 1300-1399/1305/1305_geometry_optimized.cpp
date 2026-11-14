#include <algorithm>
#include <array>
#include <cstdio>
#include <iterator>
#include <utility>

namespace {
constexpr int BUFFER_SIZE = 8192;
constexpr int DECIMAL = 10;
using Point = std::pair<int, int>;

class Input {
    std::array<unsigned char, BUFFER_SIZE> buffer{};
    std::size_t position = 0, length = 0;

    int byte() {
        if (position == length) {
            length = std::fread(buffer.data(), 1, buffer.size(), stdin);
            position = 0;
            if (!length) {
                return EOF;
            }
        }
        return buffer[position++];
    }

  public:
    int number() {
        int ch = byte();
        while (ch != EOF && ch <= ' ') {
            ch = byte();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + ch - '0';
            ch = byte();
        }
        return value;
    }
};
} // namespace

int main() {
    Input input;
    const int count = input.number();
    if (!count) {
        return 0;
    }
    int x = input.number(), y = input.number();
    int min_x = x, max_x = x, min_y = y, max_y = y;
    int min_sum = x + y, max_sum = x + y, min_diff = x - y, max_diff = x - y;
    for (int i = 1; i < count; ++i) {
        x = input.number();
        y = input.number();
        min_x = std::min(min_x, x);
        max_x = std::max(max_x, x);
        min_y = std::min(min_y, y);
        max_y = std::max(max_y, y);
        min_sum = std::min(min_sum, x + y);
        max_sum = std::max(max_sum, x + y);
        min_diff = std::min(min_diff, x - y);
        max_diff = std::max(max_diff, x - y);
    }
    // Intersect consecutive supporting lines around the hull.
    std::array corners{
        Point{min_sum - min_y, min_y},  Point{max_diff + min_y, min_y},
        Point{max_x, max_x - max_diff}, Point{max_x, max_sum - max_x},
        Point{max_sum - max_y, max_y},  Point{min_diff + max_y, max_y},
        Point{min_x, min_x - min_diff}, Point{min_x, min_sum - min_x},
    };
    auto end = std::unique(corners.begin(), corners.end());
    if (end != corners.begin() + 1 && *std::prev(end) == corners.front()) {
        --end;
    }
    for (auto it = corners.begin(); it != end; ++it) {
        std::printf("%d %d\n", it->first, it->second);
    }
}
