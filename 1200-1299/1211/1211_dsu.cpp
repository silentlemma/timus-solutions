#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int MAX_CHILDREN = 25000;
constexpr int BUFFER_SIZE = 16384;
constexpr int DECIMAL = 10;
static unsigned char input[BUFFER_SIZE];
static int position, available;
static std::int16_t sets[MAX_CHILDREN + 1];

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(input, 1, sizeof input, stdin));
        position = 0;
        if (available == 0)
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
        value = DECIMAL * value + ch - '0';
        ch = next_byte();
    }
    return value;
}

int root(int child) {
    while (sets[child] > 0) {
        const int parent = sets[child];
        if (sets[parent] > 0)
            sets[child] = sets[parent];
        child = sets[child];
    }
    return child;
}

int main() {
    for (int tests = next_int(); tests > 0; --tests) {
        const int size = next_int();
        std::fill_n(sets + 1, size, -1);
        int confessions = 0;
        bool consistent = true;
        for (int child = 1; child <= size; ++child) {
            const int named = next_int();
            if (named == 0) {
                ++confessions;
            } else if (consistent) {
                int a = root(child), b = root(named);
                if (a == b) {
                    consistent = false;
                } else {
                    if (sets[a] > sets[b])
                        std::swap(a, b);
                    sets[a] += sets[b];
                    sets[b] = a;
                }
            }
        }
        std::puts(consistent && confessions == 1 ? "YES" : "NO");
    }
}
