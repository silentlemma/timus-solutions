#include <cstdio>

constexpr int IO_SIZE = 4096;
constexpr int DECIMAL_DIGITS = 16;
class Input {
    char data[IO_SIZE];
    int position = 0, size = 0;

  public:
    int last = EOF;
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
        last = c;
        return value * sign;
    }
};

bool simple(int ch) { return ch == ' ' || (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'); }

int main() {
    Input input;
    int short_limit = input.number(), long_limit = input.number();
    for (int ch = input.last; ch != EOF && ch != '\n'; ch = input.byte()) {
    }
    int length = 0, messages = 0;
    bool plain = true;
    for (int ch = input.byte(); ch != EOF && ch != '\n' && ch != '\r'; ch = input.byte()) {
        const bool letter = simple(ch);
        if (length == long_limit || (length >= short_limit && (!plain || !letter))) {
            ++messages;
            length = 0;
            plain = true;
        }
        ++length;
        plain &= letter;
    }
    std::printf("%d\n", messages + (length > 0));
}
