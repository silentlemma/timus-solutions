#include <cstdint>
#include <cstdio>

constexpr int BUFFER_SIZE = 16384;
constexpr int DECIMAL = 10;
static unsigned char input[BUFFER_SIZE];
static int position, available;

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(input, 1, sizeof input, stdin));
        position = 0;
        if (available == 0)
            return EOF;
    }
    return input[position++];
}

int number() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    const bool negative = ch == '-';
    if (negative || ch == '+')
        ch = next_byte();
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = value * DECIMAL + ch - '0';
        ch = next_byte();
    }
    return negative ? -value : value;
}

int main() {
    const int count = number();
    const int x = number(), y = number();
    const int next_x = number(), next_y = number();
    const std::int64_t dx = next_x - x, dy = next_y - y;
    const bool vertical = dx == 0;
    int low = vertical ? y : x;
    int high = low;
    int low_id = 1, high_id = 1;
    for (int i = 2; i <= count; ++i) {
        const int current_x = i == 2 ? next_x : number();
        const int current_y = i == 2 ? next_y : number();
        if (dx * (current_y - y) != dy * (current_x - x)) {
            std::puts("0");
            return 0;
        }
        const int coordinate = vertical ? current_y : current_x;
        if (coordinate < low) {
            low = coordinate;
            low_id = i;
        }
        if (coordinate > high) {
            high = coordinate;
            high_id = i;
        }
    }
    std::printf("1\n%d %d\n", low_id, high_id);
}
