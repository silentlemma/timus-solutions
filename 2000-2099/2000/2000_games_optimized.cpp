#include <cstdint>
#include <cstdio>

const int BUFFER_SIZE = 4096;
// refillable storage bounds memory, not input length.
unsigned char buffer[BUFFER_SIZE];
int position = 0, length = 0;
int read() {
    if (position == length) {
        length = static_cast<int>(fread(buffer, 1, BUFFER_SIZE, stdin));
        position = 0;
        if (length == 0)
            return EOF;
    }
    return buffer[position++];
}
int number() {
    int c = read();
    while (c < '0' || c > '9')
        c = read();
    int value = 0;
    do {
        value = value * 10 + c - '0';
        c = read();
    } while (c >= '0' && c <= '9');
    return value;
}

const int MAX_LENGTH = 100000;
// each value is at most 10000; uint16_t stores it without truncation.
std::uint16_t values[MAX_LENGTH];
int main() {
    int n = number(), total = 0;
    for (int i = 0; i < n; ++i) {
        values[i] = static_cast<std::uint16_t>(number());
        total += values[i];
    }
    // the total is at most 100000 * 10000 = 10^9, within signed int.
    int first = number() - 1, second = number() - 1, score = 0;
    if (first == second) {
        int left = 0;
        for (int i = 0; i < first; ++i)
            left += values[i];
        int right = total - left - values[first];
        score = values[first] + (left > right ? left : right);
    } else if (first < second) {
        for (int i = 0; i <= (first + second) / 2; ++i)
            score += values[i];
    } else {
        for (int i = (first + second + 1) / 2; i < n; ++i)
            score += values[i];
    }
    printf("%d %d\n", score, total - score);
}
