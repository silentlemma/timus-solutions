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
    output.number(n * n + n / 2 + 1);
    output.line();
    int big = n * n, small = 1;
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < n; ++col) {
            // Only two counters are needed for the original checkerboard construction.
            output.number((row + col) % 2 == 0 ? big-- : small++);
        }
        output.line();
    }
    output.flush();
}
