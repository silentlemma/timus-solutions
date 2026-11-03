#include <cstdint>
#include <cstdio>
#include <vector>

const int MAX_COORD = 32000, BUFFER_SIZE = 4096;
unsigned char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (available == 0)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int main() {
    int n = next_int();
    // No counter exceeds the15000 stars. Packed counters and a small input
    // buffer avoid full integer arrays, retained tokens and a large output string.
    std::vector<uint16_t> tree(MAX_COORD + 2), count(n);
    for (int i = 0; i < n; i++) {
        int start = next_int() + 1;
        next_int();
        int level = 0;
        for (int j = start; j; j &= j - 1)
            level += tree[j];
        count[level]++;
        for (int j = start; j <= MAX_COORD + 1; j += j & -j)
            tree[j]++;
    }
    for (uint16_t value : count)
        printf("%u\n", static_cast<unsigned>(value));
}
