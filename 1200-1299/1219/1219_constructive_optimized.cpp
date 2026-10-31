#include <cstdio>

const int LETTERS = 26, ORDER = 3, LENGTH = 1000000;

// one cycle has exactly 26^3 letters; reuse it instead of holding a million bytes.
const int CYCLE_LENGTH = LETTERS * LETTERS * LETTERS;
int a[ORDER + 1], size = 0;
char cycle[CYCLE_LENGTH];

// a de bruijn sequence: every word of order letters once around the cycle.
static void gen(int t, int p) {
    if (t > ORDER) {
        if (ORDER % p == 0) {
            for (int i = 1; i <= p; i++)
                cycle[size++] = static_cast<char>('a' + a[i]);
        }
        return;
    }
    a[t] = a[t - p];
    gen(t + 1, p);
    for (int j = a[t - p] + 1; j < LETTERS; j++) {
        a[t] = j;
        gen(t + 1, t);
    }
}

int main() {
    gen(1, 1);
    // repeating the cycle keeps every window of three letters a cyclic window
    // of it, so each triple, pair and letter appears almost equally often
    int remaining = LENGTH;
    while (remaining >= size) {
        fwrite(cycle, 1, size, stdout);
        remaining -= size;
    }
    fwrite(cycle, 1, remaining, stdout);
    putchar('\n');
}
