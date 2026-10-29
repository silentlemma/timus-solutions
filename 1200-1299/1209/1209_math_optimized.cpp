#include <cmath>
#include <cstdio>

// whether v is a perfect square, with the floating root corrected exactly.
static bool square(long long v) {
    long long r = (long long)std::sqrt((double)v);
    while (r * r > v) {
        r--;
    }
    while ((r + 1) * (r + 1) <= v) {
        r++;
    }
    return r * r == v;
}

// the positions are read with getchar and the answers written with putchar,
// without scanf and without a string of the whole output
int readInt() {
    int c = getchar();
    while (c <= ' ' && c != EOF) {
        c = getchar();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = getchar();
    }
    return value;
}

int main() {
    const long long SQUARE = 8;
    int n = readInt();
    for (int i = 0; i < n; i++) {
        long long k = readInt();
        // the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
        // perfect square
        putchar(square(SQUARE * (k - 1) + 1) ? '1' : '0');
        putchar(i + 1 < n ? ' ' : '\n');
    }
}
