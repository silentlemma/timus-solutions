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
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = read();
    }
    return value;
}

char output[BUFFER_SIZE];
int used;

void write(char c) {
    if (used == BUFFER_SIZE) {
        fwrite(output, 1, used, stdout);
        used = 0;
    }
    output[used++] = c;
}

void write_int(int value) {
    char digits[10];
    int count = 0;
    do {
        digits[count++] = char('0' + value % 10);
        value /= 10;
    } while (value);
    while (count)
        write(digits[--count]);
}

int main() {
    int n = next_int();
    // At most(n+1)*10000<=1000010000 coins: cells and totals fit int32.
    std::vector<int> diff(n + 2);
    for (int i = 0; i <= n; i++) {
        int a = next_int(), b = next_int(), amount = next_int();
        diff[a] += amount;
        diff[b + 1] -= amount;
    }
    int total = 0;
    for (int i = 1; i <= n; i++) {
        total += diff[i];
        write_int(total);
        write(i < n ? ' ' : '\n');
    }
    fwrite(output, 1, used, stdout);
}
