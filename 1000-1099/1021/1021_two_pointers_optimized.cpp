#include <cstdint>
#include <cstdio>
#include <vector>

// refilling makes this buffer independent of total input size and whitespace.
constexpr int BUFFER_SIZE = 4096;
char input[BUFFER_SIZE];
int position = 0, length = 0;
int readByte() {
    if (position == length) {
        length = static_cast<int>(fread(input, 1, BUFFER_SIZE, stdin));
        position = 0;
        if (length == 0)
            return EOF;
    }
    return input[position++];
}
int nextInt() {
    int c;
    do {
        c = readByte();
    } while (c != EOF && c <= ' ');
    int sign = 1;
    if (c == '-') {
        sign = -1;
        c = readByte();
    }
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return value * sign;
}

constexpr int TARGET = 10000;
int main() {
    int n = nextInt();
    // statement values fit signed 16 bits; promote before adding.
    std::vector<int16_t> up(n);
    for (auto &x : up)
        x = static_cast<int16_t>(nextInt());
    int m = nextInt(), at = 0;
    bool found = false;
    for (int j = 0; j < m; ++j) {
        int value = nextInt();
        while (at < n && up[at] + value < TARGET)
            ++at;
        if (at < n && up[at] + value == TARGET)
            found = true;
    }
    puts(found ? "YES" : "NO");
}
