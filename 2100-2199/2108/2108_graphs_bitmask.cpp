#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

long long number() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    return sign * value;
}

constexpr int MAX_FIGURES = 1000, MAX_RULES = 4000, WORD_BITS = 64;
constexpr int FIGURE_WORDS = (MAX_FIGURES + WORD_BITS - 1) / WORD_BITS;
constexpr int RULE_WORDS = (MAX_RULES + WORD_BITS - 1) / WORD_BITS;
uint64_t needs[MAX_FIGURES][RULE_WORDS], added[MAX_RULES][FIGURE_WORDS], owned[FIGURE_WORDS];
uint16_t remaining[MAX_RULES], queue[MAX_FIGURES];
int tail = 0, words;

bool digit() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    return c == '1';
}

void give(int word, uint64_t figures) {
    uint64_t fresh = figures & ~owned[word];
    owned[word] |= figures;
    while (fresh != 0) {
        queue[tail++] = word * WORD_BITS + __builtin_ctzll(fresh);
        fresh &= fresh - 1;
    }
}

void fire(int rule) {
    for (int word = 0; word < words; ++word)
        give(word, added[rule][word]);
}

int main() {
    int n = number(), m = number();
    words = (n + WORD_BITS - 1) / WORD_BITS;
    int rule_words = (m + WORD_BITS - 1) / WORD_BITS;
    for (int rule = 0; rule < m; ++rule) {
        for (int figure = 0; figure < n; ++figure) {
            if (digit()) {
                needs[figure][rule / WORD_BITS] |= uint64_t{1} << (rule % WORD_BITS);
                ++remaining[rule];
            }
        }
        for (int figure = 0; figure < n; ++figure)
            if (digit())
                added[rule][figure / WORD_BITS] |= uint64_t{1} << (figure % WORD_BITS);
    }
    for (int figure = 0; figure < n; ++figure)
        if (digit())
            give(figure / WORD_BITS, uint64_t{1} << (figure % WORD_BITS));
    for (int rule = 0; rule < m; ++rule)
        if (remaining[rule] == 0)
            fire(rule);
    for (int head = 0; head < tail; ++head) {
        int figure = queue[head];
        for (int word = 0; word < rule_words; ++word) {
            uint64_t rules = needs[figure][word];
            while (rules != 0) {
                int rule = word * WORD_BITS + __builtin_ctzll(rules);
                if (--remaining[rule] == 0)
                    fire(rule);
                rules &= rules - 1;
            }
        }
    }
    for (int figure = 0; figure < n; ++figure)
        std::putchar('0' + ((owned[figure / WORD_BITS] >> (figure % WORD_BITS)) & 1));
    std::putchar('\n');
}
