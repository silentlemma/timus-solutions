#include <algorithm>
#include <cstdio>

constexpr int INPUT_BUFFER_SIZE = 4096;

int read_byte() {
    static unsigned char buffer[INPUT_BUFFER_SIZE];
    static std::size_t position = 0, length = 0;
    if (position == length) {
        length = std::fread(buffer, 1, sizeof(buffer), stdin);
        position = 0;
        if (length == 0)
            return EOF;
    }
    return buffer[position++];
}

int read_int() {
    int ch;
    do {
        ch = read_byte();
    } while (ch <= ' ' && ch != EOF);
    int sign = 1;
    if (ch == '-' || ch == '+') {
        if (ch == '-')
            sign = -1;
        ch = read_byte();
    }
    int value = 0;
    while (ch >= '0' && ch <= '9') {
        value = value * 10 + ch - '0';
        ch = read_byte();
    }
    return sign * value;
}

int main() {
    int n = read_int();
    // best is the largest segment sum so far (the empty segment gives 0), and
    // ending is the largest sum of a segment that ends at the current number
    long long best = 0, ending = 0;
    for (int i = 0; i < n; i++) {
        int p = read_int();
        ending += p;
        ending = std::max(ending, 0LL);
        best = std::max(best, ending);
    }
    printf("%lld\n", best);
    return 0;
}
