#include <cstdio>

const long long HUNDREDTHS = 100, WHOLE = 100 * HUNDREDTHS;
const int TOKEN_SIZE = 16;

long long hundredths(const char *text) {
    long long value = 0, scale = HUNDREDTHS;
    while (*text && *text != '.')
        value = value * 10 + *text++ - '0';
    value *= HUNDREDTHS;
    if (*text == '.')
        for (text++; *text; text++) {
            scale /= 10;
            value += (*text - '0') * scale;
        }
    return value;
}

int main() {
    char first[TOKEN_SIZE], second[TOKEN_SIZE];
    if (scanf("%15s%15s", first, second) != 2)
        return 0;
    long long p = hundredths(first), q = hundredths(second);
    long long a = 0, b = 1, c = 1, d = 0;
    while (true) {
        long long numerator = a + c, denominator = b + d;
        if (WHOLE * numerator <= p * denominator) {
            // Skip the full run at or below P, including equality.
            long long steps = (p * b - WHOLE * a) / (WHOLE * c - p * d);
            a += steps * c;
            b += steps * d;
        } else if (WHOLE * numerator >= q * denominator) {
            long long steps = (WHOLE * c - q * d) / (q * b - WHOLE * a);
            c += steps * a;
            d += steps * b;
        } else {
            printf("%lld\n", denominator);
            return 0;
        }
    }
}
