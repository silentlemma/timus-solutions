#include <cstdint>
#include <cstdio>
#include <vector>

using namespace std;

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

const int ADD = 1, ASK = 2; // record kinds; any other kind ends the input

const int MAX_RECORDS = 100002, MAX_INCREASE = 20000;
static_assert(1LL * MAX_RECORDS * MAX_INCREASE <= INT32_MAX,
              "Nonnegative block sums fit signed32-bit cells");

int n, side;
vector<int32_t> tree; // a 3D Fenwick tree, indices from 1

void add(int x, int y, int z, int k) {
    for (int i = x; i <= n; i += i & -i)
        for (int j = y; j <= n; j += j & -j) {
            int32_t *row = &tree[((long long)i * side + j) * side];
            for (int w = z; w <= n; w += w & -w)
                row[w] += k;
        }
}

long long prefix(int x, int y, int z) {
    long long total = 0;
    for (int i = x; i > 0; i -= i & -i)
        for (int j = y; j > 0; j -= j & -j) {
            const int32_t *row = &tree[((long long)i * side + j) * side];
            for (int w = z; w > 0; w -= w & -w)
                total += row[w];
        }
    return total;
}

int main() {
    Input input;
    Output output;
    n = input.number();
    side = n + 1;
    tree.assign((size_t)side * side * side, 0);
    for (;;) {
        int kind = input.number();
        if (kind != ADD && kind != ASK)
            break;
        if (kind == ADD) {
            int x = input.number(), y = input.number(), z = input.number();
            int k = input.number();
            add(x + 1, y + 1, z + 1, k);
        } else {
            int x1 = input.number(), y1 = input.number(), z1 = input.number();
            int x2 = input.number(), y2 = input.number(), z2 = input.number();
            x2++, y2++, z2++;
            // inclusion and exclusion over the eight corners of the box
            long long total = prefix(x2, y2, z2) - prefix(x1, y2, z2) - prefix(x2, y1, z2) -
                              prefix(x2, y2, z1) + prefix(x1, y1, z2) + prefix(x1, y2, z1) +
                              prefix(x2, y1, z1) - prefix(x1, y1, z1);
            output.number(total);
            output.byte('\n');
        }
    }
    output.flush();
}
