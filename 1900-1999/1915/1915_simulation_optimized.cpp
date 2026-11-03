#include <algorithm>
#include <cstdio>
#include <vector>

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
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = read();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value * sign;
}

struct Output {
    char data[BUFFER_SIZE];
    int size = 0;

    void flush() {
        fwrite(data, 1, size, stdout);
        size = 0;
    }
    void put(char c) {
        if (size == BUFFER_SIZE)
            flush();
        data[size++] = c;
    }
    void value(int coin) {
        const int DECIMAL_DIGITS = 10;
        char digits[DECIMAL_DIGITS];
        int size = 0;
        do {
            digits[size++] = char('0' + coin % 10);
            coin /= 10;
        } while (coin);
        while (size)
            put(digits[--size]);
        put('\n');
    }
};

void poppedCoins(const std::vector<int> &operations, Output &output) {
    int remaining = int(std::count(operations.begin(), operations.end(), -1));
    if (remaining == 0) {
        return;
    }
    const int capacity = remaining;
    std::vector<int> coins(capacity);
    int bottom = 0;
    int size = 0;
    for (int operation : operations) {
        if (remaining == 0) {
            break;
        }
        if (operation > 0) {
            if (size == remaining) {
                bottom = (bottom + 1) % capacity;
                --size;
            }
            coins[(bottom + size) % capacity] = operation;
            ++size;
        } else if (operation == -1) {
            --remaining;
            --size;
            output.value(coins[(bottom + size) % capacity]);
        } else {
            const int extra = std::min(size, remaining - size);
            const int newBottom = (bottom + capacity - extra) % capacity;
            int source = (bottom + size - extra) % capacity;
            int destination = newBottom;
            for (int index = 0; index < extra; ++index) {
                coins[destination] = coins[source];
                if (++source == capacity) {
                    source = 0;
                }
                if (++destination == capacity) {
                    destination = 0;
                }
            }
            bottom = newBottom;
            size += extra;
        }
    }
    return;
}

int main() {
    int count = next_int();
    std::vector<int> operations(count);
    for (int &operation : operations)
        operation = next_int();
    Output output;
    poppedCoins(operations, output);
    output.flush();
}
