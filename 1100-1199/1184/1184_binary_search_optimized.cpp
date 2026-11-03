#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

const int BUFFER_SIZE = 4096;
const uint32_t CENTS = 100;
unsigned char input[BUFFER_SIZE];
int position, available;

int read() {
    if (position == available) {
        available = fread(input, 1, BUFFER_SIZE, stdin);
        position = 0;
        if (available == 0)
            return -1;
    }
    return input[position++];
}

uint32_t number() {
    int c = read();
    while (c >= 0 && c <= ' ')
        c = read();
    uint32_t value = 0;
    while (c > ' ') {
        if (c >= '0' && c <= '9')
            value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

int main() {
    int n = number();
    uint32_t k = number(), longest = 0;
    uint64_t total = 0;
    std::vector<uint32_t> cables(n);
    for (uint32_t &length : cables) {
        length = number();
        longest = std::max(longest, length);
        total += length;
    }
    uint32_t low = longest / k, high = std::min<uint64_t>(longest, total / k);
    // A token has exactly two decimal places; ignoring its dot is exact.
    // One cable proves low feasible, conservation of length proves high bound.
    while (low < high) {
        uint32_t mid = (low + high + 1) / 2;
        uint64_t pieces = 0;
        for (uint32_t length : cables) {
            pieces += length / mid;
            if (pieces >= k)
                break;
        }
        if (pieces >= k)
            low = mid;
        else
            high = mid - 1;
    }
    printf("%u.%02u\n", low / CENTS, low % CENTS);
}
