#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

long long number() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    return sign * value;
}

long long absolute(long long value) { return value < 0 ? -value : value; }

int main() {
    int count = number();
    long long y = 1, vertical = 0, low = 0, high = 0, right = 0;
    for (int i = 0; i < count; ++i) {
        number();
        long long bottom = number(), end = number(), top = number();
        if (i > 0) {
            long long first = (low > bottom ? low : bottom) + 1;
            long long last = (high < top ? high : top) - 1;
            if (first > last) {
                puts("-1");
                return 0;
            }
            // Keep the current height unless the next shared border forces a change.
            long long target = y < first ? first : y;
            if (target > last)
                target = last;
            vertical += absolute(target - y);
            y = target;
        }
        low = bottom;
        high = top;
        right = end;
    }
    printf("%lld\n", right - 2 + vertical + absolute(high - 1 - y));
}
