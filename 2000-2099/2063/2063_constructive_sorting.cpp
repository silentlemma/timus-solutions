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

Output output;

// FNV-1a of the whole input seeds splitmix64; the arrangements are never
// decoded, they only make the seed differ between tests
constexpr uint64_t FNV_OFFSET = 0xcbf29ce484222325ULL;
constexpr uint64_t FNV_PRIME = 0x100000001b3ULL;
constexpr uint64_t GOLDEN = 0x9e3779b97f4a7c15ULL;
constexpr uint64_t MIX_A = 0xbf58476d1ce4e5b9ULL;
constexpr uint64_t MIX_B = 0x94d049bb133111ebULL;
constexpr int SHIFT_A = 30, SHIFT_B = 27, SHIFT_C = 31;

uint64_t state;

uint64_t next_random() {
    uint64_t z = state += GOLDEN;
    z = (z ^ (z >> SHIFT_A)) * MIX_A;
    z = (z ^ (z >> SHIFT_B)) * MIX_B;
    return z ^ (z >> SHIFT_C);
}

void compare(int first, int second, int real, Output &out) {
    // Padded positions contain black balls and remain unchanged in ascending comparators.
    if (second < real) {
        out.byte('?');
        out.byte(' ');
        out.number(first + 1);
        out.byte(' ');
        out.number(second + 1);
        out.byte('\n');
    }
}

void merge_network(int start, int size, int stride, int real, Output &out) {
    int step = 2 * stride;
    if (step < size) {
        merge_network(start, size, step, real, out);
        merge_network(start + stride, size, step, real, out);
        for (int first = start + stride; first + stride < start + size; first += step)
            compare(first, first + stride, real, out);
    } else {
        compare(start, start + stride, real, out);
    }
}

void sort_network(int start, int size, int real, Output &out) {
    if (size > 1) {
        int half = size / 2;
        sort_network(start, half, real, out);
        sort_network(start + half, half, real, out);
        merge_network(start, size, 1, real, out);
    }
}

int main() {
    Input input;
    state = FNV_OFFSET;
    int games = 0;
    bool begun = false, finished = false;
    // Hash every original byte; only the leading game count needs decoding.
    for (int c = input.byte(); c != EOF; c = input.byte()) {
        state = (state ^ static_cast<unsigned char>(c)) * FNV_PRIME;
        if (!finished) {
            if (c >= '0' && c <= '9') {
                games = games * 10 + c - '0';
                begun = true;
            } else if (begun)
                finished = true;
        }
    }
    for (int game = 0; game < games; ++game) {
        int n = game + 2;
        int padded = 1;
        while (padded < n)
            padded *= 2;
        sort_network(0, padded, n, output);
        int j = 1 + int(next_random() % uint64_t(n - 1));
        output.byte('!');
        output.byte(' ');
        output.number(j);
        output.byte(' ');
        output.number(j + 1);
        output.byte('\n');
    }
    output.flush();
}
