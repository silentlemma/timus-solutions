#include <algorithm>
#include <cstdint>
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

    void signed_number(int value) {
        if (value < 0) {
            byte('-');
            number(static_cast<unsigned>(-static_cast<long long>(value)));
        } else
            number(value);
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

Input input;

struct Interval {
    std::int16_t start, end, value;
};

Interval read_interval() {
    Interval result;
    result.start = input.number();
    result.end = input.number();
    result.value = input.number();
    return result;
}

int main() {
    int first_count = input.number();
    std::vector<Interval> first(first_count);
    for (auto &interval : first)
        interval = read_interval();
    int remaining = input.number();
    Interval mask = read_interval();
    --remaining;
    std::vector<Interval> result;
    result.reserve(first_count + remaining + 1);
    for (const auto &interval : first) {
        auto start = interval.start;
        while (start < interval.end) {
            while (remaining > 0 && mask.end <= start) {
                mask = read_interval();
                --remaining;
            }
            if (mask.start <= start && start < mask.end) {
                start = mask.end;
                continue;
            }
            const auto end = start < mask.start ? std::min(interval.end, mask.start) : interval.end;
            result.push_back({start, end, interval.value});
            start = end;
        }
    }
    Output output;
    output.number(result.size());
    for (const auto &interval : result) {
        output.byte(' ');
        output.signed_number(interval.start);
        output.byte(' ');
        output.signed_number(interval.end);
        output.byte(' ');
        output.signed_number(interval.value);
    }
    output.byte('\n');
    output.flush();
}
