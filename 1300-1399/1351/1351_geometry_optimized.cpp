#include <cstdio>

const int INPUT_SIZE = 4096;

struct Input {
    unsigned char bytes[INPUT_SIZE];
    int position = 0, length = 0;

    int next() {
        if (position == length) {
            length = int(fread(bytes, 1, sizeof(bytes), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return bytes[position++];
    }

    int number() {
        int c = next(), value = 0;
        while (c && c <= ' ')
            c = next();
        bool negative = c == '-';
        if (negative)
            c = next();
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = next();
        }
        return negative ? -value : value;
    }
};

const int OUTPUT_SIZE = 8192;
const int WORD_RESERVE = 4;

int main() {
    Input input;
    int reach = input.number(), rx = input.number(), ry = input.number();
    int lx = input.number(), ly = input.number(), n = input.number();
    int radiusSquared = reach * reach;
    char output[OUTPUT_SIZE];
    int used = 0;
    for (int i = 0; i < n; ++i) {
        int x = input.number(), y = input.number();
        int right = rx * y - ry * x, left = x * ly - y * lx;
        bool behind = (right == 0 && rx * x + ry * y < 0) || (left == 0 && lx * x + ly * y < 0);
        bool hit = right >= 0 && left >= 0 && !behind && x * x + y * y <= radiusSquared;
        const char *word = hit ? "YES\n" : "NO\n";
        for (; *word; ++word)
            output[used++] = *word;
        if (used + WORD_RESERVE > OUTPUT_SIZE) {
            fwrite(output, 1, used, stdout);
            used = 0;
        }
    }
    fwrite(output, 1, used, stdout);
}
