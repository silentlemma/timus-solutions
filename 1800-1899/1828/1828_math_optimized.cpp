#include <cstdint>
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

constexpr long long STEP_SCALE = 12, CENTER_SCALE = 6, FIRST_SCALE = 4;
constexpr long long DECIMAL_SCALE = 1000000000;
constexpr int DECIMAL_DIGITS = 9, OUTPUT_SIZE = 64, MAX_DIGITS = 20;
char output[OUTPUT_SIZE];
int used = 0;

void append_integer(long long value) {
    char digits[MAX_DIGITS];
    int first = MAX_DIGITS;
    do {
        digits[--first] = char('0' + value % 10);
        value /= 10;
    } while (value != 0);
    while (first < MAX_DIGITS)
        output[used++] = digits[first++];
}

void append_fraction(long long numerator, long long denominator) {
    if (numerator < 0) {
        output[used++] = '-';
        numerator = -numerator;
    }
    long long whole = numerator / denominator, remainder = numerator % denominator, fraction = 0;
    for (int i = 0; i < DECIMAL_DIGITS; ++i) {
        remainder *= 10;
        fraction = fraction * 10 + remainder / denominator;
        remainder %= denominator;
    }
    if (2 * remainder >= denominator && ++fraction == DECIMAL_SCALE) {
        fraction = 0;
        ++whole;
    }
    append_integer(whole);
    output[used++] = '.';
    for (long long power = DECIMAL_SCALE / 10; power != 0; power /= 10)
        output[used++] = char('0' + fraction / power % 10);
}

int main() {
    long long n = number(), sum = 0, weighted = 0;
    for (long long i = 0; i < n; ++i) {
        long long value = number();
        sum += value;
        weighted += i * value;
    }
    append_fraction((FIRST_SCALE * n - 2) * sum - CENTER_SCALE * weighted, n * (n + 1));
    output[used++] = ' ';
    append_fraction(STEP_SCALE * weighted - CENTER_SCALE * (n - 1) * sum, n * (n * n - 1));
    output[used++] = '\n';
    std::fwrite(output, 1, used, stdout);
}
