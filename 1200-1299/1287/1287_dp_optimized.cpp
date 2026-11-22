#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <emmintrin.h>
#include <utility>

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

    void word(char *text) {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        while (c > ' ') {
            *text++ = c;
            c = byte();
        }
        *text = 0;
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

constexpr int MAX_WIDTH = 1400;
constexpr int LANES = 8;
constexpr int ROW_SIZE = MAX_WIDTH + LANES + 2;
constexpr int DIRECTIONS = 3;

using RunRow = std::int16_t[DIRECTIONS][ROW_SIZE];

static char colors[2][ROW_SIZE];
static RunRow lengths[2];

__m128i load_colors(const char *row) {
    return _mm_loadl_epi64(reinterpret_cast<const __m128i *>(row));
}

// Duplicate each byte comparison into a full 16-bit run-length mask.
__m128i widen_mask(__m128i mask) { return _mm_unpacklo_epi8(mask, mask); }

__m128i extend(__m128i current, const char *previous, const std::int16_t *run) {
    const auto same = widen_mask(_mm_cmpeq_epi8(current, load_colors(previous)));
    const auto previous_run = _mm_loadu_si128(reinterpret_cast<const __m128i *>(run));
    return _mm_add_epi16(_mm_and_si128(same, previous_run), _mm_set1_epi16(1));
}

int max_lane(__m128i value) {
    std::int16_t lanes[LANES];
    _mm_storeu_si128(reinterpret_cast<__m128i *>(lanes), value);
    return *std::max_element(lanes, lanes + LANES);
}

int main() {
    Input input;
    int width = input.number();
    auto *previous = colors[0];
    auto *current = colors[1];
    auto *previous_runs = &lengths[0];
    auto *current_runs = &lengths[1];
    auto lower_best = _mm_setzero_si128();
    auto upper_best = _mm_setzero_si128();
    int across_best[2]{};
    for (int y = 0; y < width; ++y) {
        input.word(current + 1);
        for (int start = 1, end = 1; start <= width; start = end) {
            const char grain = current[start];
            do {
                ++end;
            } while (current[end] == grain);
            auto &best = across_best[grain == 'S'];
            best = std::max(best, end - start);
        }
        // Eight lanes extend the two diagonals and the vertical run together.
        // Zero padding makes the final partial block safe; color masks ignore it.
        for (int x = 1; x <= width; x += LANES) {
            const auto grain = load_colors(current + x);
            auto longest = _mm_setzero_si128();
            for (int direction = 0; direction < DIRECTIONS; ++direction) {
                const int from = x + direction - 1;
                const auto run = extend(grain, previous + from, (*previous_runs)[direction] + from);
                _mm_storeu_si128(reinterpret_cast<__m128i *>((*current_runs)[direction] + x), run);
                longest = _mm_max_epi16(longest, run);
            }
            const auto lower = widen_mask(_mm_cmpeq_epi8(grain, _mm_set1_epi8('s')));
            const auto upper = widen_mask(_mm_cmpeq_epi8(grain, _mm_set1_epi8('S')));
            lower_best = _mm_max_epi16(lower_best, _mm_and_si128(lower, longest));
            upper_best = _mm_max_epi16(upper_best, _mm_and_si128(upper, longest));
        }
        std::swap(previous, current);
        std::swap(previous_runs, current_runs);
    }
    const int lower = std::max(across_best[0], max_lane(lower_best));
    const int upper = std::max(across_best[1], max_lane(upper_best));
    const char winner = lower > upper ? 's' : (upper > lower ? 'S' : '?');
    std::printf("%c\n%d\n", winner, std::max(lower, upper));
}
