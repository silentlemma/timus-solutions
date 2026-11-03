#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>

const int POSITION_BITS = 17, POSITION_MASK = (1 << POSITION_BITS) - 1;
const int BUFFER_SIZE = 4096;
unsigned char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (!available)
            return -1;
    }
    return input[position++];
}

int next_int() {
    int c = read();
    while (c <= ' ')
        c = read();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int main() {
    int n = next_int();
    std::vector<uint64_t> flowers(n);
    // Moisture needs30bits, position17: the combined key fits uint64.
    for (int i = 0; i < n; i++)
        flowers[i] = (uint64_t(next_int()) << POSITION_BITS) | i;
    std::sort(flowers.begin(), flowers.end());
    long long at_left = 0, at_right = 0;
    int left = 0, right = 0;
    for (int i = 0; i < n;) {
        int j = i + 1;
        while (j < n && flowers[j] >> POSITION_BITS == flowers[i] >> POSITION_BITS)
            j++;
        int lo = flowers[i] & POSITION_MASK, hi = flowers[j - 1] & POSITION_MASK;
        int width = hi - lo;
        long long to_left = std::min(at_left + abs(left - hi), at_right + abs(right - hi)) + width;
        long long to_right = std::min(at_left + abs(left - lo), at_right + abs(right - lo)) + width;
        at_left = to_left;
        at_right = to_right;
        left = lo;
        right = hi;
        i = j;
    }
    printf("%lld\n", std::min(at_left, at_right) + n);
}
