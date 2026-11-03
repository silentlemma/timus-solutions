#include <cstdio>

const int BUFFER = 1 << 14;
char buffer[BUFFER];
int position, available;
int readByte() {
    if (position == available) {
        available = (int)fread(buffer, 1, BUFFER, stdin);
        position = 0;
        if (!available)
            return EOF;
    }
    return buffer[position++];
}
long long nextInt() {
    int c = readByte();
    while (c <= ' ')
        c = readByte();
    bool negative = c == '-';
    if (negative)
        c = readByte();
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return negative ? -value : value;
}
int main() {
    int n = (int)nextInt(), left = 1;
    long long previous = nextInt(), best = -1;
    for (int right = 2; right <= n; right++) {
        long long current = nextInt(), difference = current - previous;
        if (difference < 0)
            difference = -difference;
        if (difference > best) {
            best = difference;
            left = right - 1;
        }
        previous = current;
    }
    printf("%d %d\n", left, left + 1);
}
