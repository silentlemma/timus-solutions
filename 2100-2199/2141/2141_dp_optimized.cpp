#include <algorithm>
#include <cstdio>

const int BUFFER_SIZE = 4096;
char input[BUFFER_SIZE];
int position, available;

int readByte() {
    if (position == available) {
        available = std::fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (!available)
            return EOF;
    }
    return input[position++];
}

int nextInt() {
    int ch = readByte();
    while (ch <= ' ')
        ch = readByte();
    int sign = 1, value = 0;
    if (ch == '-') {
        sign = -1;
        ch = readByte();
    }
    while (ch >= '0' && ch <= '9') {
        value = value * 10 + ch - '0';
        ch = readByte();
    }
    return sign * value;
}

int main() {
    int n = nextInt();
    long long plus = nextInt(), minus = 0, best = std::max(0LL, plus);
    for (int i = 1; i < n; i++) {
        long long value = nextInt(), nextPlus = value + std::max(0LL, minus);
        minus = plus - value;
        plus = nextPlus;
        best = std::max(best, std::max(plus, minus));
    }
    printf("%lld\n", best);
}
