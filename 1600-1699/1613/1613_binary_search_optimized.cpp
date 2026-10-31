#include <algorithm>
#include <cstdint>
#include <cstdio>

// refills allow arbitrarily long input with only four kibibytes of storage.
const int INPUT_BUFFER = 4096;
char input_buffer[INPUT_BUFFER];
int input_pos = 0, input_len = 0;

int read_byte() {
    if (input_pos == input_len) {
        input_len = static_cast<int>(fread(input_buffer, 1, INPUT_BUFFER, stdin));
        input_pos = 0;
        if (input_len == 0)
            return EOF;
    }
    return input_buffer[input_pos++];
}

int next_int() {
    int c = read_byte();
    while (c != EOF && c <= ' ')
        c = read_byte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read_byte();
    }
    return value;
}

const int MAX_CITIES = 69999, CITY_BITS = 17;
std::uint64_t pairs[MAX_CITIES];
int main() {
    int n = next_int();
    // city <= 69999 needs 17 bits; count < 10^9 uses 30 more, within uint64_t.
    for (int i = 0; i < n; i++)
        pairs[i] = (std::uint64_t(next_int()) << CITY_BITS) | std::uint64_t(i + 1);
    std::sort(pairs, pairs + n);
    int q = next_int();
    for (int i = 0; i < q; i++) {
        int lo = next_int(), hi = next_int(), x = next_int();
        std::uint64_t base = std::uint64_t(x) << CITY_BITS;
        auto it = std::lower_bound(pairs, pairs + n, base + lo);
        putchar(it != pairs + n && *it <= base + hi ? '1' : '0');
    }
    putchar('\n');
}
