#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int IO_SIZE = 16384;
constexpr int DECIMAL_DIGITS = 20;
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
    void number(unsigned long long value) {
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

constexpr int MAX_WINDOW = 50;
int plans[MAX_WINDOW];

int main() {
    Input input;
    Output output;
    int n = input.number(), m = input.number();
    for (int i = 0; i < m; ++i)
        plans[i] = input.number();
    int head = 0, stock = 0;
    for (int month = 0; month < n; ++month) {
        int best = plans[head] - stock, index = head;
        for (int t = 2; t <= m; ++t) {
            if (++index == m)
                index = 0;
            int delta = plans[index] - stock;

            // ceil(delta/t) > best exactly when delta > best*t, even for negatives.
            if (delta > best * t)
                best = delta >= 0 ? (delta + t - 1) / t : delta / t;
        }
        stock += best;

        if (best < 0)
            output.byte('-');
        output.number(best < 0 ? -best : best);
        output.byte(month + 1 == n ? '\n' : ' ');
        if (month + 1 < n) {
            plans[head] = input.number();
            if (++head == m)
                head = 0;
        }
    }
    output.flush();
}
