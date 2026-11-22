#include <cstdint>
#include <cstdio>

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

constexpr int MAX_VOTES = 10000;
constexpr double PERCENT = 100.0;
constexpr int PERCENT_LENGTH = 9;
uint16_t votes[MAX_VOTES + 1];
char formatted[MAX_VOTES + 1][PERCENT_LENGTH];
unsigned char lengths[MAX_VOTES + 1];

int main() {
    Input input;
    Output output;
    int candidates = input.number(), total = input.number();
    for (int i = 0; i < total; ++i)
        ++votes[input.number()];
    for (int i = 1; i <= candidates; ++i) {
        int count = votes[i];
        // Equal vote counts have exactly the same printf rounding and representation.
        if (lengths[count] == 0)
            lengths[count] = std::snprintf(formatted[count], PERCENT_LENGTH, "%.2f%%\n",
                                           PERCENT * count / total);
        for (int j = 0; j < lengths[count]; ++j)
            output.byte(formatted[count][j]);
    }
    output.flush();
}
