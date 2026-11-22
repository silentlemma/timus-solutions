#include <cstdio>
#include <set>
#include <string>

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

    void word(char *text) {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        while (c > ' ') {
            *text++ = c;
            c = byte();
        }
        *text = 0;
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

constexpr int LIMIT = 20, MAX_NAME = 20;

int main() {
    std::set<std::string> names = {"sun"};
    Input input;
    Output output;
    char line[MAX_NAME + 2];
    for (;;) {
        input.word(line);
        if (!line[0])
            break;
        std::string argument = line + 1;
        if (line[0] == '+') {
            names.insert(argument);
            continue;
        }
        // Stream each query; retaining all answers would cost megabytes.
        for (char c : argument)
            output.byte(c);
        output.byte('\n');
        int shown = 0;
        for (auto it = names.lower_bound(argument); it != names.end() && shown < LIMIT; ++it) {
            if (it->compare(0, argument.size(), argument) != 0)
                break;
            output.byte(' ');
            output.byte(' ');
            for (char c : *it)
                output.byte(c);
            output.byte('\n');
            ++shown;
        }
    }
    output.flush();
}
