#include <algorithm>
#include <cstdio>
#include <vector>

constexpr int IO_SIZE = 16384;
constexpr int DECIMAL_DIGITS = 16;
class Input {
    char data[IO_SIZE];
    int position = 0, size = 0;

  public:
    int byte() {
        if (position == size) {
            size = std::fread(data, 1, sizeof data, stdin);
            position = 0;
            if (size == 0)
                return EOF;
        }
        return static_cast<unsigned char>(data[position++]);
    }
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = byte();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return value * sign;
    }
};
class Output {
    char data[IO_SIZE];
    int size = 0;

  public:
    void flush() {
        std::fwrite(data, 1, size, stdout);
        size = 0;
    }
    void byte(char c) {
        if (size == IO_SIZE)
            flush();
        data[size++] = c;
    }
    void number(unsigned value) {
        char digits[DECIMAL_DIGITS];
        int count = 0;
        do {
            digits[count++] = '0' + value % 10;
            value /= 10;
        } while (value);
        while (count)
            byte(digits[--count]);
    }
};

constexpr int INDEX_BITS = 10;
constexpr int INDEX_MASK = (1 << INDEX_BITS) - 1;

int main() {
    Input input;
    Output output;
    int size = input.number();
    std::vector<int> ordered(size);
    for (int i = 0; i < size; ++i) {
        int threshold = input.number();
        ordered[i] = (threshold << INDEX_BITS) | (i + 1);
    }
    std::sort(ordered.begin(), ordered.end());
    std::vector<int> sizes;
    for (int count = 1; count <= size; ++count) {
        if ((ordered[count - 1] >> INDEX_BITS) <= count &&
            (count == size || (ordered[count] >> INDEX_BITS) > count + 1))
            sizes.push_back(count);
    }
    output.number(sizes.size());
    output.byte('\n');
    for (int count : sizes) {
        output.number(count);
        for (int i = 0; i < count; ++i) {
            output.byte(' ');
            output.number(ordered[i] & INDEX_MASK);
        }
        output.byte('\n');
    }
    output.flush();
}
