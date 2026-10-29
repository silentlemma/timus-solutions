#include <cstdio>

constexpr int INPUT_BUFFER_SIZE = 8192;

// the numbers are parsed by hand from 8 KB blocks, faster than scanf
int readInt() {
    static char buffer[INPUT_BUFFER_SIZE];
    static size_t position = 0;
    static size_t length = 0;
    int value = 0;
    bool started = false;
    for (;;) {
        if (position == length) {
            length = fread(buffer, 1, sizeof(buffer), stdin);
            position = 0;
            if (length == 0)
                return value;
        }
        char c = buffer[position++];
        if (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            started = true;
        } else if (started) {
            return value;
        }
    }
}

int main() {
    const int TIME = 30000;
    int n = readInt();
    // the latest start among the talks that end at each minute; times are at
    // most 30 000, so an unsigned short holds them
    static unsigned short latest[TIME + 1];
    for (int i = 0; i < n; i++) {
        int s = readInt(), e = readInt();
        if (s > latest[e]) {
            latest[e] = s;
        }
    }
    // take the talk that ends first among those starting after the last one
    int count = 0, last = 0;
    for (int e = 1; e <= TIME; e++) {
        if (latest[e] > last) {
            count++;
            last = e;
        }
    }
    printf("%d\n", count);
}
