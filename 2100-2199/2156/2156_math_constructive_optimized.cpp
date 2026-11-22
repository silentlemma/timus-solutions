#include <bitset>
#include <cstdio>
#include <initializer_list>

const int MAX_FRIENDS = 100000;
constexpr int IO_SIZE = 4096;
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

int main() {
    Input input;
    Output output;
    int n = input.number(), first = input.number(), previous = first;
    std::bitset<MAX_FRIENDS> falls;
    int count = 0;
    // The signed differences sum to zero. Mark just the edges with a drop.
    for (int edge = 0; edge < n; ++edge) {
        int current = edge + 1 < n ? input.number() : first;
        if (previous > current) {
            falls.set(edge);
            ++count;
        }
        previous = current;
    }
    if (count == 0) {
        falls.set(0);
        count = 1;
    }
    for (char c : {'Y', 'E', 'S', '\n'})
        output.byte(c);
    for (bool group : {true, false}) {
        output.number(group ? count : n - count);
        output.byte('\n');
        char separator = '\0';
        for (int edge = 0; edge < n; ++edge) {
            if (falls[edge] != group)
                continue;
            if (separator)
                output.byte(separator);
            output.number(edge + 1);
            separator = ' ';
        }
        output.byte('\n');
    }
    output.flush();
}
