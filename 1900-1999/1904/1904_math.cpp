#include <algorithm>
#include <cassert>
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

constexpr int MAX_FOLDS = 10, MAX_INTERVALS = 1 << (MAX_FOLDS - 1);
struct Interval {
    int16_t left, right;
};
Interval first[MAX_INTERVALS], second[MAX_INTERVALS];
int references[MAX_FOLDS];

void append(Interval *output, int &used, int left, int right) {
    if (used != 0 && left <= output[used - 1].right) {
        if (right > output[used - 1].right)
            output[used - 1].right = int16_t(right);
    } else {
        assert(used < MAX_INTERVALS);
        output[used++] = {int16_t(left), int16_t(right)};
    }
}

int main() {
    int k = number();
    for (int i = 0; i < k; ++i)
        references[i] = number();
    Interval *current = first, *next = second;
    current[0] = {0, 1};
    int count = 1;
    for (int step = k - 1; step >= 0 && count != 0; --step) {
        int begin = 0, used = 0, a = references[step];
        while (begin < count && current[begin].right < 0)
            ++begin;
        // Negative reflected intervals are ordered when the original list is reversed.
        for (int i = count - 1; i >= begin; --i) {
            int left = std::max(0, int(current[i].left));
            append(next, used, a - current[i].right, a - left);
        }
        // Every positive branch starts at or to the right of a.
        for (int i = begin; i < count; ++i) {
            int left = std::max(0, int(current[i].left));
            append(next, used, a + left, a + current[i].right);
        }
        count = used;
        std::swap(current, next);
    }
    std::printf("%d\n", count);
    for (int i = 0; i < count; ++i)
        std::printf("%d %d\n", current[i].left, current[i].right);
}
