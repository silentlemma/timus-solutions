#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>

const int MAX_COORD = 1000;
const int MAX_DENOMINATOR = 4 * MAX_COORD;
const uint64_t SCALE = uint64_t(MAX_DENOMINATOR) * MAX_DENOMINATOR;
const uint64_t HALF_TURN = 2 * SCALE, FULL_TURN = 4 * SCALE;
const int DISTANCE_BITS = 12, ID_BITS = 15, KEY_SHIFT = DISTANCE_BITS + ID_BITS;
const uint64_t ID_MASK = (uint64_t(1) << ID_BITS) - 1;
const int MAX_POINTS = 30000;
const int BUFFER_SIZE = 4096;
unsigned char input[BUFFER_SIZE];
int position, available;
uint64_t keys[MAX_POINTS];

int readByte() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (!available)
            return EOF;
    }
    return input[position++];
}

int nextInt() {
    int ch = readByte();
    while (ch <= ' ')
        ch = readByte();
    int sign = 1, value = 0;
    if (ch == '-') {
        sign = -1;
        ch = readByte();
    }
    while (ch >= '0' && ch <= '9') {
        value = value * 10 + ch - '0';
        ch = readByte();
    }
    return sign * value;
}

int main() {
    int n = nextInt(), ox = nextInt(), oy = nextInt(), m = n - 1;
    for (int identity = 2; identity <= n; identity++) {
        int dx = nextInt() - ox, dy = nextInt() - oy, distance = std::abs(dx) + std::abs(dy);
        uint64_t rank = dy > 0 || (dy == 0 && dx > 0)
                            ? uint64_t(distance - dx) * SCALE / distance
                            : HALF_TURN + uint64_t(distance + dx) * SCALE / distance;
        keys[identity - 2] =
            (rank << KEY_SHIFT) | (uint64_t(distance) << ID_BITS) | uint64_t(identity);
    }
    std::sort(keys, keys + m);
    int start = 0;
    uint64_t previous = keys[m - 1] >> KEY_SHIFT;
    for (int i = 0; i < m; i++) {
        uint64_t current = keys[i] >> KEY_SHIFT;
        uint64_t gap = current >= previous ? current - previous : current + FULL_TURN - previous;
        if (gap >= HALF_TURN)
            start = i;
        previous = current;
    }
    printf("%d\n1\n", n);
    for (int i = start; i < m; i++)
        printf("%u\n", unsigned(keys[i] & ID_MASK));
    for (int i = 0; i < start; i++)
        printf("%u\n", unsigned(keys[i] & ID_MASK));
}
