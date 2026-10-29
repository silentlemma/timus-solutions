#include <cstdio>

const int MAX_BASE = 36;
const int BUFFER_SIZE = 4096;

int main() {
    char buffer[BUFFER_SIZE];
    int total = 0, top = 1;
    // the digits are summed chunk by chunk: the line of up to 10^6 digits is
    // never stored
    for (size_t length; (length = fread(buffer, 1, sizeof(buffer), stdin)) > 0;) {
        for (size_t i = 0; i < length; ++i) {
            char c = buffer[i];
            if (c <= ' ')
                continue;
            int digit = c >= 'A' ? c - 'A' + 10 : c - '0';
            total += digit;
            if (digit > top)
                top = digit;
        }
    }
    // base is 1 modulo base - 1, so the number is congruent to its digit sum
    for (int base = top + 1; base <= MAX_BASE; ++base) {
        if (total % (base - 1) == 0) {
            printf("%d\n", base);
            return 0;
        }
    }
    puts("No solution.");
}
