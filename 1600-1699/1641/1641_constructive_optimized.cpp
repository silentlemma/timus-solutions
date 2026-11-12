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
    int n, k, remaining;
    scanf("%d%d%d", &n, &k, &remaining);
    Output output;
    for (int i = 0; i < n; ++i) {
        output.number(i % k + 1);
        output.line();
    }
    auto pair = [&](int a, int b) {
        output.number(a + 1);
        output.number(b + 1);
        output.line();
        --remaining;
    };
    for (int i = 0; i + 1 < n; i += 2)
        pair(i, i + 1);
    int anchor = (n - 1) % k == 0 ? 1 : 0;
    if (n % 2)
        pair(anchor, n - 1);
    for (int a = 0; a < n && remaining; ++a)
        for (int b = a + 1; b < n && remaining; ++b) {
            if (a % k == b % k)
                continue;
            // These predicates identify exactly the already emitted covering pairs.
            if ((a % 2 == 0 && b == a + 1) || (n % 2 && b == n - 1 && a == anchor))
                continue;
            pair(a, b);
        }
    output.flush();
}
