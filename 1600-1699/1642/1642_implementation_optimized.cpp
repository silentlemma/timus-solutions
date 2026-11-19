#include <cstdio>

constexpr int MAX_SIGNED_DIGITS = 20;
constexpr int SEARCH_RADIUS = 2000;

long long number() {
    int c = getchar();
    while (c != EOF && c <= ' ')
        c = getchar();
    bool negative = c == '-';
    if (negative || c == '+')
        c = getchar();
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 - (c - '0');
        c = getchar();
    }
    return negative ? value : -value;
}

void output(long long value) {
    unsigned long long magnitude = static_cast<unsigned long long>(value);
    if (value < 0) {
        putchar('-');
        magnitude = static_cast<unsigned long long>(-(value + 1)) + 1;
    }
    char digits[MAX_SIGNED_DIGITS];
    int size = 0;
    do {
        digits[size++] = static_cast<char>('0' + magnitude % 10);
        magnitude /= 10;
    } while (magnitude);
    while (size)
        putchar(digits[--size]);
}

int main() {
    const long long count = number(), exit = number();
    long long left = -SEARCH_RADIUS, right = SEARCH_RADIUS;
    for (long long i = 0; i < count; ++i) {
        const long long wall = number();
        if (wall < 0 && wall > left)
            left = wall;
        if (wall > 0 && wall < right)
            right = wall;
    }
    if (exit < left || exit > right) {
        puts("Impossible");
    } else {
        output(exit > 0 ? exit : 2 * right - exit);
        putchar(' ');
        output(exit > 0 ? -2 * left + exit : -exit);
        putchar('\n');
    }
}
