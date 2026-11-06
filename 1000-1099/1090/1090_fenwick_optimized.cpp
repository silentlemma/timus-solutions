#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int MAX_RECRUITS = 10000;
constexpr int BUFFER_SIZE = 4096;
static unsigned char input[BUFFER_SIZE];
static std::uint16_t counts[MAX_RECRUITS + 1];
static int position, available;

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(input, 1, sizeof input, stdin));
        position = 0;
        if (!available)
            return EOF;
    }
    return input[position++];
}

int next_int() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = value * 10 + ch - '0';
        ch = next_byte();
    }
    return value;
}

int main() {
    const int size = next_int();
    const int rows = next_int();
    int best = -1, answer = 1;
    for (int row = 1; row <= rows; ++row) {
        std::fill_n(counts, size + 1, 0);
        int jumps = 0;
        for (int seen = 0; seen < size; ++seen) {
            const int height = next_int();
            jumps += seen;
            for (int prefix = height - 1; prefix; prefix &= prefix - 1)
                jumps -= counts[prefix];
            for (int at = height; at <= size; at += at & -at)
                ++counts[at];
        }
        if (jumps > best) {
            best = jumps;
            answer = row;
        }
    }
    std::printf("%d\n", answer);
}
