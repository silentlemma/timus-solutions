#include <cstdint>
#include <cstdio>
#include <vector>

const int BUFFER_SIZE = 4096, WORD_BITS = 64;
unsigned char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (available == 0)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int main() {
    int n = next_int(), m = next_int();
    // A vertically full column beside a vertically single column makes
    // exactly three dark cells. Check64columns together, plus word boundaries.
    int words = (m + WORD_BITS - 1) / WORD_BITS;
    std::vector<uint64_t> previous(words);
    for (int row = 0; row < n; row++) {
        bool leftBoth = false, leftSingle = false;
        for (int block = 0; block < words; block++) {
            int width = m - block * WORD_BITS;
            if (width > WORD_BITS)
                width = WORD_BITS;
            uint64_t current = 0;
            for (int bit = 0; bit < width; bit++) {
                int ch = read();
                while (ch != '0' && ch != '1')
                    ch = read();
                current |= uint64_t(ch - '0') << bit;
            }
            uint64_t both = previous[block] & current;
            uint64_t single = previous[block] ^ current;
            if ((both & (single >> 1)) || (single & (both >> 1)) || ((both & 1) && leftSingle) ||
                ((single & 1) && leftBoth)) {
                puts("No");
                return 0;
            }
            leftBoth = (both >> (width - 1)) & 1;
            leftSingle = (single >> (width - 1)) & 1;
            previous[block] = current;
        }
    }
    puts("Yes");
}
