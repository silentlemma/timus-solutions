#include <array>
#include <cstdio>

constexpr int BUFFER_SIZE = 16384;

class Input {
    std::array<unsigned char, BUFFER_SIZE> buffer;
    std::size_t position = 0;
    std::size_t size = 0;

    int byte() {
        if (position == size) {
            position = 0;
            size = std::fread(buffer.data(), 1, buffer.size(), stdin);
            if (size == 0) {
                return EOF;
            }
        }
        return buffer[position++];
    }

  public:
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ') {
            c = byte();
        }
        const bool negative = c == '-';
        if (negative || c == '+') {
            c = byte();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = byte();
        }
        return negative ? -value : value;
    }
};

int main() {
    Input input;
    const int n = input.number();
    const long long first_x = input.number();
    const long long first_y = input.number();
    long long previous_x = first_x;
    long long previous_y = first_y;
    long long twice_area = 0;
    for (int i = 1; i < n; ++i) {
        const long long x = input.number();
        const long long y = input.number();
        twice_area += previous_x * y - previous_y * x;
        previous_x = x;
        previous_y = y;
    }
    twice_area += previous_x * first_y - previous_y * first_x;
    std::puts(twice_area > 0 ? "ccw" : "cw");
}
