#include <cstdint>
#include <cstdio>
#include <cstring>
#include <vector>

const int BASE = 10, DIGITS = 6, MAX_INPUT = 100000, WORD_BITS = 64;

int main() {
    char text[MAX_INPUT + 1];
    scanf("%100000s", text);
    int n = static_cast<int>(strlen(text)), first = 1;
    // Try lengths in order; the first absent value is the global answer.
    for (int length = 1; length <= DIGITS; length++, first *= BASE) {
        int count = (BASE - 1) * first, modulus = first * BASE, value = 0;
        std::vector<uint64_t> seen((count + WORD_BITS - 1) / WORD_BITS);
        for (int i = 0; i < n; i++) {
            value = (value * BASE + text[i] - '0') % modulus;
            if (i + 1 >= length && value >= first) {
                int offset = value - first;
                seen[offset / WORD_BITS] |= uint64_t(1) << (offset % WORD_BITS);
            }
        }
        for (int offset = 0; offset < count; offset++)
            if (!(seen[offset / WORD_BITS] & (uint64_t(1) << (offset % WORD_BITS)))) {
                printf("%d\n", first + offset);
                return 0;
            }
    }
}
