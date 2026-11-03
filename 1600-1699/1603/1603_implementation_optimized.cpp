#include <cstdint>
#include <cstdio>
#include <cstring>
#include <utility>

const int SIDE = 4;
const int CELLS = SIDE * SIDE;
const int LETTERS = 26;
const int COLORS = 2;
const int STATE_BITS = CELLS - 1;
const int BYTE_BITS = 8;
const int MEMO_BYTES = CELLS * (1 << STATE_BITS) / BYTE_BITS, MAX_WORDS = 100;
uint32_t positions[LETTERS], colors[COLORS], nearCells[CELLS], allowed[CELLS];
int capacity[COLORS][LETTERS], length;
unsigned char failed[MEMO_BYTES];
char grid[CELLS], word[CELLS + 1], queries[MAX_WORDS][CELLS + 1];
bool answers[MAX_WORDS];

bool walk(int cell, uint32_t used, int index) {
    if (index + 1 == length)
        return true;
    // Endpoint is already known to be present; delete its bit from the key.
    uint32_t compressed = (used & ((uint32_t(1) << cell) - 1)) | ((used >> (cell + 1)) << cell);
    uint32_t key = (uint32_t(cell) << STATE_BITS) | compressed;
    unsigned char flag = static_cast<unsigned char>(1u << (key % BYTE_BITS));
    if (failed[key / BYTE_BITS] & flag)
        return false;
    uint32_t options = nearCells[cell] & allowed[index + 1] & ~used;
    while (options) {
        uint32_t bit = options & -options;
        if (walk(__builtin_ctz(bit), used | bit, index + 1))
            return true;
        options -= bit;
    }
    failed[key / BYTE_BITS] |= flag;
    return false;
}

bool found(const char *original) {
    std::strcpy(word, original);
    length = std::strlen(word);
    if (__builtin_popcount(positions[word[0] - 'a']) >
        __builtin_popcount(positions[word[length - 1] - 'a']))
        for (int left = 0, right = length - 1; left < right; left++, right--)
            std::swap(word[left], word[right]);
    int needed[COLORS][LETTERS] = {};
    for (int i = 0; i < length; i++)
        needed[i % COLORS][word[i] - 'a']++;
    uint32_t starts = 0;
    for (int color = 0; color < COLORS; color++) {
        bool possible = true;
        for (int letter = 0; letter < LETTERS; letter++)
            if (needed[0][letter] > capacity[color][letter] ||
                needed[1][letter] > capacity[color ^ 1][letter])
                possible = false;
        if (possible)
            starts |= colors[color];
    }
    if (!starts)
        return false;
    allowed[length - 1] = positions[word[length - 1] - 'a'];
    for (int i = length - 2; i >= 0; i--) {
        allowed[i] = 0;
        uint32_t cells = positions[word[i] - 'a'];
        while (cells) {
            uint32_t bit = cells & -cells;
            int cell = __builtin_ctz(bit);
            if (nearCells[cell] & allowed[i + 1])
                allowed[i] |= bit;
            cells -= bit;
        }
    }
    starts &= allowed[0];
    if (!starts)
        return false;
    std::memset(failed, 0, sizeof(failed));
    while (starts) {
        uint32_t bit = starts & -starts;
        if (walk(__builtin_ctz(bit), bit, 0))
            return true;
        starts -= bit;
    }
    return false;
}

int main() {
    char row[SIDE + 1];
    for (int r = 0; r < SIDE; r++) {
        scanf("%4s", row);
        std::memcpy(grid + r * SIDE, row, SIDE);
    }
    for (int cell = 0; cell < CELLS; cell++) {
        uint32_t bit = uint32_t(1) << cell;
        positions[grid[cell] - 'a'] |= bit;
        int r = cell / SIDE, c = cell % SIDE;
        colors[(r + c) % COLORS] |= bit;
        if (r > 0)
            nearCells[cell] |= uint32_t(1) << (cell - SIDE);
        if (r + 1 < SIDE)
            nearCells[cell] |= uint32_t(1) << (cell + SIDE);
        if (c > 0)
            nearCells[cell] |= uint32_t(1) << (cell - 1);
        if (c + 1 < SIDE)
            nearCells[cell] |= uint32_t(1) << (cell + 1);
    }
    for (int color = 0; color < COLORS; color++)
        for (int letter = 0; letter < LETTERS; letter++)
            capacity[color][letter] = __builtin_popcount(positions[letter] & colors[color]);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%16s", queries[i]);
        int previous = 0;
        while (previous < i && std::strcmp(queries[previous], queries[i]))
            previous++;
        answers[i] = previous < i ? answers[previous] : found(queries[i]);
        printf("%s: %s\n", queries[i], answers[i] ? "YES" : "NO");
    }
}
