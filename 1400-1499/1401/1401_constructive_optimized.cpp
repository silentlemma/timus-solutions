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

const int MAX_EXPONENT = 9;
const int MAX_SIDE = 1 << MAX_EXPONENT;
// n <= 9 gives a board of at most 512 by 512 and labels at most 87381.
constexpr int LOW_BITS = 16;
uint16_t low[MAX_SIDE][MAX_SIDE];
uint8_t high[MAX_SIDE][MAX_SIDE];
int count = 0;

// recursion needs only n stack frames; reverse quarters keep the simple numbering.
void tile(int top, int left, int side, int hr, int hc) {
    int label = ++count, half = side / 2;
    for (int dr = 1; dr >= 0; --dr)
        for (int dc = 1; dc >= 0; --dc) {
            int r0 = top + dr * half, c0 = left + dc * half, r, c;
            if (r0 <= hr && hr < r0 + half && c0 <= hc && hc < c0 + half) {
                r = hr;
                c = hc;
            } else {
                r = top + half - 1 + dr;
                c = left + half - 1 + dc;
                low[r][c] = label;
                high[r][c] = label >> LOW_BITS;
            }
            if (half > 1)
                tile(r0, c0, half, r, c);
        }
}

int main() {
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    int size = 1 << n;
    tile(0, 0, size, x - 1, y - 1);
    // Three bytes per label cover every tile; output is bounded independently.
    Output output;
    for (int r = 0; r < size; ++r)
        for (int c = 0; c < size; ++c) {
            output.number(low[r][c] | (unsigned(high[r][c]) << LOW_BITS));
            output.byte(c + 1 < size ? ' ' : '\n');
        }
    output.flush();
}
