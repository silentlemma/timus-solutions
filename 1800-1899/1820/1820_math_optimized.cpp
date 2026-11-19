#include <cstdio>

constexpr int MAX_SIGNED_DIGITS = 20;

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
    const long long steaks = number(), capacity = number();
    long long minutes = (2 * steaks + capacity - 1) / capacity;
    if (minutes < 2)
        minutes = 2;
    output(minutes);
    putchar('\n');
}
