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
    const long long hobbits = number(), couples = number();
    output(hobbits * (hobbits - 1) / 2 - couples);
    putchar('\n');
}
