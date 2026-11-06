#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

constexpr int BUFFER_SIZE = 16384;
constexpr int DECIMAL = 10;
static unsigned char input[BUFFER_SIZE];
static int position, available;

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(input, 1, sizeof input, stdin));
        position = 0;
        if (available == 0)
            return EOF;
    }
    return input[position++];
}

std::uint32_t next_int() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    std::uint32_t value = 0;
    while (ch >= '0' && ch <= '9') {
        value = value * DECIMAL + ch - '0';
        ch = next_byte();
    }
    return value;
}

int main() {
    const auto size = next_int();
    std::vector<std::uint32_t> events(2 * size);
    // At equal value, put the problem before the student who can solve it.
    for (std::uint32_t i = 0; i < size; ++i)
        events[i] = (next_int() << 1) | 1;
    for (std::uint32_t i = size; i < events.size(); ++i)
        events[i] = next_int() << 1;
    const auto modulus = next_int();
    std::sort(events.begin(), events.end());
    std::uint64_t ways = 1 % modulus;
    std::uint32_t free = 0;
    for (auto event : events) {
        if ((event & 1) == 0) {
            ++free;
        } else {
            ways = ways * free % modulus;
            if (ways == 0)
                break;
            --free;
        }
    }
    std::printf("%u\n", static_cast<unsigned>(ways));
}
