#include <algorithm>
#include <cstdint>
#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

long long number() {
    int c = byte();
    while (c >= 0 && c <= ' ')
        c = byte();
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = byte();
    }
    long long value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = byte();
    }
    return sign * value;
}

constexpr int MAX_WINDOW = 50;
int plans[MAX_WINDOW];

int main() {
    int n = number(), m = number();
    for (int i = 0; i < m; ++i)
        plans[i] = number();
    int head = 0, stock = 0;
    for (int month = 0; month < n; ++month) {
        int best = plans[head] - stock, index = head;
        for (int t = 2; t <= m; ++t) {
            if (++index == m)
                index = 0;
            int delta = plans[index] - stock;
            int change = delta >= 0 ? (delta + t - 1) / t : delta / t;
            if (change > best)
                best = change;
        }
        stock += best;
        std::printf("%d%c", best, month + 1 == n ? '\n' : ' ');
        if (month + 1 < n) {
            plans[head] = number();
            if (++head == m)
                head = 0;
        }
    }
}
