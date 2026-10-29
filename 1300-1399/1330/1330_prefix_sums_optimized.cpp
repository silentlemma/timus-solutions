#include <cstdio>

constexpr int BUFFER_SIZE = 4096;
constexpr int MAX_SENSORS = 10000;
char input[BUFFER_SIZE], output[BUFFER_SIZE];
int inputSize = 0, inputPosition = 0, outputPosition = 0;
// before[i] is the sum of the first i readings
int before[MAX_SENSORS + 1];

// the numbers are parsed and the answers written by hand through 4 KB
// buffers; the sums stay within 10^8 in absolute value, so int is enough
int readByte() {
    if (inputPosition == inputSize) {
        inputSize = static_cast<int>(fread(input, 1, BUFFER_SIZE, stdin));
        inputPosition = 0;
        if (inputSize == 0)
            return EOF;
    }
    return input[inputPosition++];
}

int nextInt() {
    int c = readByte();
    while (c != EOF && c <= ' ')
        c = readByte();
    bool negative = c == '-';
    if (negative)
        c = readByte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = readByte();
    }
    return negative ? -value : value;
}

void writeByte(char c) {
    if (outputPosition == BUFFER_SIZE) {
        fwrite(output, 1, outputPosition, stdout);
        outputPosition = 0;
    }
    output[outputPosition++] = c;
}

void writeInt(int value) {
    if (value < 0) {
        writeByte('-');
        value = -value;
    }
    constexpr int MAX_DIGITS = 10;
    char digits[MAX_DIGITS];
    int count = 0;
    do {
        digits[count++] = static_cast<char>('0' + value % 10);
        value /= 10;
    } while (value != 0);
    while (count > 0)
        writeByte(digits[--count]);
    writeByte('\n');
}

int main() {
    int n = nextInt();
    for (int i = 1; i <= n; ++i)
        before[i] = before[i - 1] + nextInt();
    for (int q = nextInt(); q > 0; --q) {
        int i = nextInt(), j = nextInt();
        writeInt(before[j] - before[i - 1]);
    }
    fwrite(output, 1, outputPosition, stdout);
}
