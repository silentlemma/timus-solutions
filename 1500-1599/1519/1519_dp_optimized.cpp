#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <vector>

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

constexpr int MAX_SIDE = 12, MAX_STATES = 41835, INITIAL_CAPACITY = 16384;
constexpr int TABLE_BITS = 16, TABLE_SIZE = 1 << TABLE_BITS, KEY_BITS = 32;
constexpr uint32_t HASH_MULTIPLIER = 2654435761U;
uint16_t index_table[TABLE_SIZE];
bool free_cell[MAX_SIDE + 1][MAX_SIDE + 1];

struct Layer {
    std::vector<uint32_t> keys;
    std::vector<uint64_t> counts;
    Layer() {
        keys.reserve(INITIAL_CAPACITY);
        counts.reserve(INITIAL_CAPACITY);
    }
    void clear() {
        keys.clear();
        counts.clear();
        std::fill(index_table, index_table + TABLE_SIZE, 0);
    }
    void add(uint32_t state, uint64_t count) {
        uint32_t slot = state * HASH_MULTIPLIER >> (KEY_BITS - TABLE_BITS);
        while (index_table[slot] != 0) {
            int index = index_table[slot] - 1;
            if (keys[index] == state) {
                counts[index] += count;
                return;
            }
            slot = (slot + 1) & (TABLE_SIZE - 1);
        }
        // All balanced zero/bracket profiles of length at most13 number41835.
        assert(keys.size() < MAX_STATES);
        keys.push_back(state);
        counts.push_back(count);
        index_table[slot] = keys.size();
    }
};
Layer first, second;

typedef uint64_t u64;
const u64 OPEN = 1, CLOSE = 2; // the ends of a path piece, matched like brackets
const u64 FLIP = OPEN ^ CLOSE; // turns one end into the other
const int BITS = 2;            // bits per plug
const u64 MASK = 3;

// the plug matching the bracket at pos, searching towards step
int partner(u64 state, int pos, int step) {
    for (int depth = 0;; pos += step) {
        u64 v = state >> (BITS * pos) & MASK;
        if (v == OPEN)
            depth += step;
        else if (v == CLOSE)
            depth -= step;
        if (depth == 0)
            return pos;
    }
}

int main() {
    int n = number(), m = number();
    bool transpose = m > n;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            int c = byte();
            while (c >= 0 && c <= ' ')
                c = byte();
            free_cell[transpose ? j : i][transpose ? i : j] = c == '.';
        }
    if (transpose)
        std::swap(n, m);
    int last = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (free_cell[i][j])
                last = i * m + j;
    Layer *ways = &first, *next = &second;
    ways->keys.push_back(0);
    ways->counts.push_back(1);
    u64 total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            next->clear();
            int sl = BITS * j, su = BITS * (j + 1);
            u64 clear = ~(MASK << sl) & ~(MASK << su);
            bool down = free_cell[i + 1][j], right = free_cell[i][j + 1];
            for (size_t index = 0; index < ways->keys.size(); ++index) {
                u64 state = ways->keys[index], count = ways->counts[index];
                u64 left = state >> sl & MASK, up = state >> su & MASK, base = state & clear;
                if (!free_cell[i][j]) {
                    if (left == 0 && up == 0)
                        next->add(state, count);
                } else if (left == 0 && up == 0) {
                    if (down && right)
                        next->add(base | OPEN << sl | CLOSE << su, count);
                } else if (left == 0 || up == 0) {
                    u64 end = left | up;
                    if (down)
                        next->add(base | end << sl, count);
                    if (right)
                        next->add(base | end << su, count);
                } else if (left == up) {
                    // two openings or two closings: the far end of one of the
                    // joined pieces changes its kind
                    int far = left == OPEN ? partner(state, j + 1, 1) : partner(state, j, -1);
                    next->add(base ^ FLIP << (BITS * far), count);
                } else if (left == CLOSE) {
                    next->add(base, count);
                } else if (i * m + j == last && base == 0) {
                    total += count; // the loop closes on the last free cell
                }
            }
            std::swap(ways, next);
        }
        // the next row starts with an empty left plug
        for (auto &state : ways->keys)
            state <<= BITS;
    }
    std::printf("%llu\n", (unsigned long long)total);
}
