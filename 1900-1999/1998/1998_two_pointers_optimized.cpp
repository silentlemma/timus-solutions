#include <cstdint>
#include <cstdio>

constexpr int MAX_OBJECTS = 100000;
constexpr int BUFFER_SIZE = 4096;
static unsigned char input[BUFFER_SIZE];
static int position, available;
static std::uint16_t weights[MAX_OBJECTS];
static int retreat[MAX_OBJECTS + 1];

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(input, 1, sizeof input, stdin));
        position = 0;
        if (!available)
            return EOF;
    }
    return input[position++];
}

int next_int() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = value * 10 + ch - '0';
        ch = next_byte();
    }
    return value;
}

int main() {
    const int size = next_int();
    const int event_count = next_int();
    const int limit = next_int();
    int left = 0, released_weight = 0;
    for (int right = 0; right < size; ++right) {
        weights[right] = next_int();
        released_weight += weights[right];
        // Advance only while the remaining suffix still exceeds the limit.
        while (left < right && released_weight - weights[left] > limit)
            released_weight -= weights[left++];
        retreat[right + 1] = left;
    }
    int height = 0, time = 0;
    for (int i = 0; i < event_count; ++i) {
        const int event = next_int();
        const int ordinary = event - time - 1;
        if (ordinary >= size - height)
            break;
        height = retreat[height + ordinary];
        time = event;
    }
    std::printf("%d\n", time + size - height);
}
