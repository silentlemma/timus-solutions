#include <cstdio>

const int OUTPUT_SIZE = 8192;
const int NUMBER_RESERVE = 16;

struct Output {
    char bytes[OUTPUT_SIZE];
    int used = 0;
    bool first = true;

    void flush() {
        fwrite(bytes, 1, used, stdout);
        used = 0;
    }

    void number(int value) {
        if (used + NUMBER_RESERVE >= OUTPUT_SIZE)
            flush();
        if (!first)
            bytes[used++] = ' ';
        first = false;
        char digits[NUMBER_RESERVE];
        int count = 0;
        do {
            digits[count++] = char('0' + value % 10);
            value /= 10;
        } while (value);
        while (count)
            bytes[used++] = digits[--count];
    }

    void line() {
        bytes[used++] = '\n';
        first = true;
    }
};

int main() {
    int n;
    scanf("%d", &n);
    Output output;
    output.number(1);
    output.number(n);
    const int PAIR_PERIOD = 4;
    int pairs = (n - 1) / 2;
    // The old two arms contain exactly pairs pairs, computable by their step index.
    for (int k = 1; k <= pairs; ++k)
        output.number(k % 2 ? k + 1 : n - k);
    if (n % 2 == 0 && n > 2)
        output.number(2 * (n / PAIR_PERIOD) + 1);
    for (int k = pairs; k >= 2; --k)
        output.number(k % 2 ? k : n - k + 1);
    output.line();
    for (int value = 1; value <= n; value += 2)
        output.number(value);
    for (int value = n - n % 2; value >= 2; value -= 2)
        output.number(value);
    output.line();
    output.flush();
}
