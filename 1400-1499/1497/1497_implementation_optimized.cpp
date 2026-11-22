#include <cstdio>
#include <emmintrin.h>

constexpr int MAX_WIDTH = 1000, LANES = 16, IO_SIZE = 16384;
unsigned char input[IO_SIZE];
int position, available;
char row[MAX_WIDTH + LANES]{};
unsigned previous[(MAX_WIDTH + LANES - 1) / LANES]{};

int byte() {
    if (position == available) {
        available = std::fread(input, 1, sizeof input, stdin);
        position = 0;
        if (available == 0)
            return EOF;
    }
    return input[position++];
}

int main() {
    int c = byte(), size = 0;
    while (c >= 0 && c <= ' ')
        c = byte();
    while (c >= '0' && c <= '9') {
        size = size * 10 + c - '0';
        c = byte();
    }
    bool left = true, right = true, up = true, down = true;
    const __m128i one = _mm_set1_epi8('1');
    for (int y = 0; y < size; ++y) {
        for (int x = 0; x < size; ++x) {
            while (c >= 0 && c <= ' ')
                c = byte();
            row[x] = static_cast<char>(c);
            c = byte();
        }
        unsigned carry = 0;
        for (int x = 0; x < size; x += LANES) {
            const int take = size - x < LANES ? size - x : LANES;
            const unsigned mask = (1U << take) - 1;
            const __m128i chars = _mm_loadu_si128(reinterpret_cast<const __m128i *>(row + x));
            const unsigned bits =
                static_cast<unsigned>(_mm_movemask_epi8(_mm_cmpeq_epi8(chars, one))) & mask;
            const unsigned before = (bits << 1) | carry;
            const unsigned horizontal = x == 0 ? mask & ~1U : mask;
            left &= (bits & ~before & horizontal) == 0;
            right &= (~bits & before & horizontal) == 0;
            if (y > 0) {
                up &= (bits & ~previous[x / LANES]) == 0;
                down &= (~bits & previous[x / LANES] & mask) == 0;
            }
            previous[x / LANES] = bits;
            carry = (bits >> (take - 1)) & 1U;
        }
        if (!(left || right || up || down)) {
            std::puts("No");
            return 0;
        }
    }
    std::puts("Yes");
}
