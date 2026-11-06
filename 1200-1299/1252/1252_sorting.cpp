#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <numeric>

constexpr int MAX_WEIGHT = 130000;
constexpr int BUFFER_SIZE = 16384;
constexpr int DECIMAL = 10;
static unsigned char input[BUFFER_SIZE];
static int offset, available;
static int positions[MAX_WEIGHT + 1];

int next_byte() {
    if (offset == available) {
        available = static_cast<int>(std::fread(input, 1, sizeof input, stdin));
        offset = 0;
        if (available == 0)
            return EOF;
    }
    return input[offset++];
}

int next_int() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = value * DECIMAL + ch - '0';
        ch = next_byte();
    }
    return value;
}

int main() {
    const int size = next_int();
    int lightest = MAX_WEIGHT, heaviest = 0;
    for (int i = 1; i <= size; ++i) {
        const int weight = next_int();
        positions[weight] = i;
        lightest = std::min(lightest, weight);
        heaviest = std::max(heaviest, weight);
    }
    int rank = 0, up = 0, down = 0;
    for (int weight = lightest; weight <= heaviest; ++weight) {
        const int position = positions[weight];
        if (position == 0)
            continue;
        ++rank;
        up = std::gcd(up, std::abs(position - rank));
        down = std::gcd(down, std::abs(position - (size + 1 - rank)));
        if (up == 1 && down == 1)
            break;
    }
    const int step = up == 0 || down == 0 ? size : std::max(up, down);
    std::printf("%d\n", step - 1);
}
