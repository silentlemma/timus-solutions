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

constexpr int MAX_DESTROYED = 10000;

int main() {
    Input input;
    Output output;
    input.number();
    int m = input.number();
    // Original labels never exceed 1e9, so 32-bit entries suffice.
    std::vector<int> gone;
    gone.reserve(MAX_DESTROYED);
    for (int event = 0; event < m; ++event) {
        char command[2];
        input.word(command);
        int room = input.number();
        int low = 0, high = gone.size();
        while (low < high) {
            int middle = (low + high) / 2;
            if (gone[middle] - middle <= room)
                low = middle + 1;
            else
                high = middle;
        }
        int original = room + low;
        if (command[0] == 'D')
            gone.insert(gone.begin() + low, original);
        else {
            output.number(original);
            output.byte('\n');
        }
    }
    output.flush();
}
