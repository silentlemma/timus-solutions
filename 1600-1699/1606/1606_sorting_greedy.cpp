#include <cstdint>
#include <cstdio>

constexpr int FINISH = 0;
constexpr int START = 100000;
constexpr int MAX_FLAGS = 50000;

constexpr int BUFFER_SIZE = 1 << 15;

int readByte() {
    static unsigned char input[BUFFER_SIZE];
    static size_t position = 0, length = 0;
    if (position == length) {
        length = fread(input, 1, sizeof input, stdin);
        position = 0;
        if (length == 0)
            return EOF;
    }
    return input[position++];
}

int number() {
    int ch = readByte();
    while (ch != EOF && ch <= ' ')
        ch = readByte();
    const bool negative = ch == '-';
    if (negative)
        ch = readByte();
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = 10 * value + ch - '0';
        ch = readByte();
    }
    return negative ? -value : value;
}

int main() {
    static uint16_t atHeight[START + 1], path[MAX_FLAGS];
    static int x[MAX_FLAGS + 1];
    const int n = number();
    for (int id = 1; id <= n; ++id) {
        x[id] = number();
        atHeight[number()] = static_cast<uint16_t>(id);
    }
    int count = 0;
    bool right = false;
    for (int y = START; y >= FINISH; --y) {
        const uint16_t id = atHeight[y];
        if (id == 0)
            continue;
        if (count == 0) {
            path[count++] = id;
            continue;
        }
        const bool step = x[id] > x[path[count - 1]];
        // A step in the same direction moves the endpoint to the new extreme.
        if (count == 1 || step != right)
            path[count++] = id;
        else
            path[count - 1] = id;
        right = step;
    }
    printf("%d\n", count);
    for (int i = 0; i < count; ++i)
        printf("%d%c", int(path[i]), i + 1 == count ? '\n' : ' ');
}
