#include <cstdint>
#include <cstdio>

// The 15000th prime is 163841, so these bounds cover every statement query.
constexpr int LIMIT = 163842;
constexpr int PRIME_COUNT = 15000;
constexpr int FIRST_ODD = 3;
constexpr int BYTE_BITS = 8;
constexpr int ODD_COUNT = LIMIT / 2;
constexpr unsigned WORD_BASE = 1u << 16;
static unsigned char composite[(ODD_COUNT + BYTE_BITS - 1) / BYTE_BITS];
static std::uint16_t low[PRIME_COUNT];

bool marked(int index) { return composite[index / BYTE_BITS] & (1u << (index % BYTE_BITS)); }
void mark(int index) { composite[index / BYTE_BITS] |= 1u << (index % BYTE_BITS); }

int main() {
    for (int p = FIRST_ODD; p * p < LIMIT; p += 2)
        if (!marked(p / 2))
            for (int q = p * p / 2; q < ODD_COUNT; q += p)
                mark(q);
    int used = 0, first_high = PRIME_COUNT, second_high = PRIME_COUNT;
    low[used++] = 2;
    for (int p = FIRST_ODD; p < LIMIT; p += 2)
        if (!marked(p / 2)) {
            // Sorted primes need only two indices to recover the high bits.
            if (static_cast<unsigned>(p) >= WORD_BASE && first_high == PRIME_COUNT)
                first_high = used;
            if (static_cast<unsigned>(p) >= 2 * WORD_BASE && second_high == PRIME_COUNT)
                second_high = used;
            low[used++] = static_cast<std::uint16_t>(p);
        }
    int queries;
    if (scanf("%d", &queries) != 1)
        return 0;
    while (queries--) {
        int index;
        scanf("%d", &index);
        --index;
        unsigned value = low[index];
        if (index >= first_high)
            value += WORD_BASE;
        if (index >= second_high)
            value += WORD_BASE;
        printf("%u\n", value);
    }
}
