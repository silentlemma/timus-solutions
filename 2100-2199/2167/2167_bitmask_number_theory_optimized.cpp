#include <cstdint>
#include <cstdio>

const int OUTPUT_SIZE = 8192;
const int NUMBER_RESERVE = 16;

struct Output {
    char bytes[OUTPUT_SIZE];
    int used = 0;
    bool first = true;

    void flush() {
        fwrite(bytes, 1, used, stdout);
        used = 0;
    }

    void number(int value) {
        if (used + NUMBER_RESERVE >= OUTPUT_SIZE)
            flush();
        if (!first)
            bytes[used++] = ' ';
        first = false;
        char digits[NUMBER_RESERVE];
        int count = 0;
        do {
            digits[count++] = char('0' + value % 10);
            value /= 10;
        } while (value);
        while (count)
            bytes[used++] = digits[--count];
    }

    void line() {
        bytes[used++] = '\n';
        first = true;
    }
};

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
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = next();
        }
        return value;
    }
};

constexpr int BITS = 20;
constexpr int FIRST_ODD_PRIME = 3;
constexpr int LIMIT = 1 << BITS;
constexpr int WORD_BITS = 64;
constexpr int TREE_WORDS = 2 * LIMIT / WORD_BITS;
constexpr uint64_t ODD_BITS = 0xAAAAAAAAAAAAAAAAULL;

uint64_t tree[TREE_WORDS];

bool has(int node) { return (tree[node / WORD_BITS] >> (node % WORD_BITS)) & 1; }

void mark(int node) { tree[node / WORD_BITS] |= uint64_t(1) << (node % WORD_BITS); }
void clear(int node) { tree[node / WORD_BITS] &= ~(uint64_t(1) << (node % WORD_BITS)); }

int main() {
    // The leaf half is the sieve itself; internal bits later record nonempty prefixes.
    for (int word = LIMIT / WORD_BITS; word < TREE_WORDS; ++word)
        tree[word] = ODD_BITS;
    clear(LIMIT + 1);
    mark(LIMIT + 2);
    for (int prime = FIRST_ODD_PRIME; prime * prime < LIMIT; prime += 2)
        if (has(LIMIT + prime))
            for (int composite = prime * prime; composite < LIMIT; composite += 2 * prime)
                clear(LIMIT + composite);
    for (int node = LIMIT - 1; node > 0; --node)
        if (has(2 * node) || has(2 * node + 1))
            mark(node);
    Input input;
    Output output;
    int count = input.number();
    while (count--) {
        int value = input.number(), prefix = 1;
        for (int bit = BITS - 1; bit >= 0; --bit) {
            int preferred = 2 * prefix + ((value >> bit) & 1);
            prefix = has(preferred) ? preferred : preferred ^ 1;
        }
        output.number(value ^ (prefix - LIMIT));
        output.line();
    }
    output.flush();
}
