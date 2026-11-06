#include <cstdio>

constexpr int BUFFER_SIZE = 4096;
static unsigned char buffer[BUFFER_SIZE];
static int position, available;

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(buffer, 1, sizeof buffer, stdin));
        position = 0;
        if (!available)
            return EOF;
    }
    return buffer[position++];
}

int next_int() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    bool negative = ch == '-';
    if (negative)
        ch = next_byte();
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = value * 10 + ch - '0';
        ch = next_byte();
    }
    return negative ? -value : value;
}

int main() {
    const int start = next_int();
    const int end = next_int();
    int previous = next_int(), direction = 0, pieces = 1;
    for (int index = start; index < end; ++index) {
        const int current = next_int();
        const int step = (current > previous) - (current < previous);
        if (step && direction && step != direction) {
            // The step crossing the boundary sets no direction in the new piece.
            ++pieces;
            direction = 0;
        } else if (!direction) {
            direction = step;
        }
        previous = current;
    }
    std::printf("%d\n", pieces);
}
