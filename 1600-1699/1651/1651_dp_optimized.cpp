#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int MAX_VERTICES = 10000;
constexpr int MAX_LENGTH = 100000;
constexpr int BUFFER_SIZE = 4096;
static unsigned char input[BUFFER_SIZE];
static int position, available;
static std::uint16_t chain[MAX_LENGTH], best[MAX_VERTICES + 1];
static int jump[MAX_LENGTH], next_at[MAX_VERTICES + 1];

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
    for (int i = 0; i < size; ++i)
        chain[i] = next_int();
    const int finish = chain[size - 1];
    if (chain[0] != finish) {
        // Any shortest subsequence walk is simple: deleting a repeated-vertex loop preserves order.
        std::fill_n(best, MAX_VERTICES + 1, MAX_VERTICES);
        int suffix_distance = 0;
        for (int i = size - 2; i >= 0; --i) {
            const int vertex = chain[i];
            if (suffix_distance < best[vertex]) {
                best[vertex] = suffix_distance;
                next_at[vertex] = i + 1;
            }
            jump[i] = next_at[vertex];
            suffix_distance = vertex == finish ? 0 : best[vertex] + 1;
        }
    }
    std::printf("%d", static_cast<int>(chain[0]));
    for (int i = 0; chain[i] != finish;) {
        i = jump[i];
        std::printf(" %d", static_cast<int>(chain[i]));
    }
    std::puts("");
}
