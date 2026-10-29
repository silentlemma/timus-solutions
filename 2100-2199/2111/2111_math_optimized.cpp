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
    int n = readInt();
    long long total = 0;
    for (int i = 0; i < n; i++) {
        int d = readInt();
        total += d;
    }
    // a trip to a city with load L costs L d there and (L - d) d back; summed over
    // any order this is (sum of d)^2, so the order does not matter
    printf("%lld\n", total * total);
}
