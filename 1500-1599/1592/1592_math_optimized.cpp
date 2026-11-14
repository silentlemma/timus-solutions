#include <cstdint>
#include <cstdio>
#include <limits>

constexpr int HOURS = 12;
constexpr int MINUTE = 60;
constexpr int HOUR = MINUTE * MINUTE;
constexpr int CYCLE = HOURS * HOUR;
constexpr int BUFFER_SIZE = 4096;

class Input {
    unsigned char buffer[BUFFER_SIZE];
    std::size_t position = 0, size = 0;

    int byte() {
        if (position == size) {
            size = std::fread(buffer, 1, sizeof buffer, stdin);
            position = 0;
            if (size == 0)
                return EOF;
        }
        return buffer[position++];
    }

  public:
    int number() {
        int c = byte();
        while (c != EOF && (c < '0' || c > '9'))
            c = byte();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return value;
    }
};

int main() {
    Input input;
    const int count = input.number();
    std::uint16_t frequency[CYCLE]{};
    for (int i = 0; i < count; ++i) {
        const int hour = input.number();
        const int minute = input.number();
        const int second = input.number();
        ++frequency[hour % HOURS * HOUR + minute * MINUTE + second];
    }

    // The omitted sum of the initial times is constant for every target.
    int chosen = 0, later = count;
    std::int64_t best = std::numeric_limits<std::int64_t>::max();
    for (int target = 0; target < CYCLE; ++target) {
        if (!frequency[target])
            continue;
        later -= frequency[target];
        const std::int64_t cost = std::int64_t{count} * target + std::int64_t{CYCLE} * later;
        if (cost < best) {
            best = cost;
            chosen = target;
        }
    }
    const int hour = chosen / HOUR;
    std::printf("%d:%02d:%02d\n", hour ? hour : HOURS, chosen / MINUTE % MINUTE, chosen % MINUTE);
}
