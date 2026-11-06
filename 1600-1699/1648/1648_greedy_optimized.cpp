#include <algorithm>
#include <cstdio>
#include <vector>

constexpr int BUFFER_SIZE = 4096;

int next_byte() {
    static unsigned char buffer[BUFFER_SIZE];
    static std::size_t position = 0;
    static std::size_t size = 0;
    if (position == size) {
        position = 0;
        size = std::fread(buffer, 1, sizeof buffer, stdin);
        if (size == 0) {
            return EOF;
        }
    }
    return buffer[position++];
}

int number() {
    int c = next_byte();
    while (c != EOF && c <= ' ') {
        c = next_byte();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = 10 * value + c - '0';
        c = next_byte();
    }
    return value;
}

int main() {
    const int months = number();
    const int capacity = number();
    std::vector<int> sales(months);
    int total = 0;
    int limit = 0;
    for (int &sold : sales) {
        limit += capacity;
        const int next = std::min(total + number(), limit);
        sold = next - total;
        total = next;
    }
    int carry = 0;
    long long storage = 0;
    for (auto month = sales.rbegin(); month != sales.rend(); ++month) {
        // Only the accumulated number of yacht-months can exceed 32 bits.
        storage += carry;
        carry = std::max(0, *month + carry - capacity);
    }
    std::printf("%d %lld\n", total, storage);
}
