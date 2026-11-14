#include <algorithm>
#include <array>
#include <cstdio>

using Number = unsigned long long;
const int MAX_BITS = 60;
const int BUFFER_SIZE = 1 << 15;
const int NUMBER_SIZE = 21;

int readByte() {
    static unsigned char input[BUFFER_SIZE];
    static size_t position = 0, length = 0;
    if (position == length) {
        length = fread(input, 1, sizeof input, stdin);
        position = 0;
        if (length == 0)
            return EOF;
    }
    return input[position++];
}

Number readNumber() {
    int ch = readByte();
    while (ch != EOF && ch <= ' ')
        ch = readByte();
    Number value = 0;
    while ('0' <= ch && ch <= '9') {
        value = 10 * value + ch - '0';
        ch = readByte();
    }
    return value;
}

int main() {
    const int bits = static_cast<int>(readNumber());
    int queries = static_cast<int>(readNumber());
    const int last = std::min<Number>(bits, (1ULL << bits) - 1);
    std::array<Number, MAX_BITS + 1> count{};
    Number combinations = 1;
    for (int box = 1; box <= last; ++box) {
        combinations = combinations * (bits - box + 1) / box;
        count[box] = 1 + combinations - (box == 1);
    }
    // Each small box sends its extra bottles to a single smaller box.
    for (int box = last; box > 1; --box)
        count[__builtin_popcount(box)] += count[box] - 1;
    std::array<std::array<char, NUMBER_SIZE>, MAX_BITS + 1> answers{};
    for (int box = 1; box <= last; ++box)
        snprintf(answers[box].data(), NUMBER_SIZE, "%llu", count[box]);
    static char buffer[BUFFER_SIZE];
    setvbuf(stdout, buffer, _IOFBF, sizeof buffer);
    while (queries-- > 0) {
        const Number box = readNumber();
        fputs(box <= static_cast<Number>(last) ? answers[box].data() : "1", stdout);
        putchar(queries ? ' ' : '\n');
    }
}
