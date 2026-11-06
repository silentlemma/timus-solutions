#include <array>
#include <charconv>
#include <cstdio>

constexpr int BUFFER_SIZE = 4096;
constexpr int DECIMAL = 10;
constexpr int BLOCK = 1000;
constexpr int FIXED = 153;
constexpr int OUTPUT_MARGIN = 24;

constexpr std::array<int, BLOCK> digit_cubes() {
    std::array<int, BLOCK> table{};
    for (int i = 1; i < BLOCK; ++i) {
        const int digit = i % DECIMAL;
        table[i] = table[i / DECIMAL] + digit * digit * digit;
    }
    return table;
}

int byte() {
    static unsigned char buffer[BUFFER_SIZE];
    static std::size_t position = 0;
    static std::size_t size = 0;
    if (position == size) {
        position = 0;
        size = std::fread(buffer, 1, sizeof buffer, stdin);
        if (size == 0) {
            return EOF;
        }
    }
    return buffer[position++];
}

long long number() {
    int c = byte();
    while (c != EOF && c <= ' ') {
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = DECIMAL * value + (c - '0');
        c = byte();
    }
    return value;
}

int main() {
    constexpr auto table = digit_cubes();
    char output[BUFFER_SIZE];
    char *end = output;
    for (int t = static_cast<int>(number()); t > 0; --t) {
        const int n = static_cast<int>(number());
        int gap = static_cast<int>(number());
        const long long offset = number();
        // A key has at most five digits, and a cube sum is at most 5 * 9^3.
        for (int step = 1; step < n && gap != FIXED; ++step) {
            gap = table[gap / BLOCK] + table[gap % BLOCK];
        }
        end = std::to_chars(end, output + BUFFER_SIZE - 1, gap - offset).ptr;
        *end++ = '\n';
        if (end >= output + BUFFER_SIZE - OUTPUT_MARGIN) {
            std::fwrite(output, 1, end - output, stdout);
            end = output;
        }
    }
    std::fwrite(output, 1, end - output, stdout);
}
