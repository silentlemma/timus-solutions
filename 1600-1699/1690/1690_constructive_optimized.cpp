#include <array>
#include <cstdint>
#include <cstdio>

constexpr int CLASSES = 4;
constexpr int MAX_ARMY = 5000;
constexpr int INPUT_BUFFER = 8192;

class Input {
    unsigned char buffer[INPUT_BUFFER];
    std::size_t position = 0, length = 0;

    int byte() {
        if (position == length) {
            length = std::fread(buffer, 1, sizeof buffer, stdin);
            position = 0;
            if (!length)
                return EOF;
        }
        return buffer[position++];
    }

  public:
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        const bool negative = c == '-';
        if (negative)
            c = byte();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return negative ? -value : value;
    }
};

int main() {
    Input input;
    const int required = input.number();
    if (required < 1 || required > MAX_ARMY)
        return 0;

    std::uint16_t selected[CLASSES][MAX_ARMY];
    std::array<int, CLASSES> counts{};
    // After this many candidates, some parity class must have reached the quota.
    const int prefix = CLASSES * (required - 1) + 1;
    for (int i = 1; i <= prefix; ++i) {
        const unsigned x = input.number();
        const unsigned y = input.number();
        const unsigned group = (x & 1U) * 2U + (y & 1U);
        selected[group][counts[group]++] = static_cast<std::uint16_t>(i);
        if (counts[group] == required) {
            std::puts("OK");
            for (int j = 0; j < required; ++j)
                std::printf("%d%c", selected[group][j], j + 1 == required ? '\n' : ' ');
            return 0;
        }
    }
}
