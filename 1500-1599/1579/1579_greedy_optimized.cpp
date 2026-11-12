#include <cstdio>
#include <vector>

const int OUTPUT_SIZE = 8192;
const int NUMBER_RESERVE = 16;

struct Output {
    char bytes[OUTPUT_SIZE];
    int used = 0;
    bool first = true;

    void flush() {
        fwrite(bytes, 1, used, stdout);
        used = 0;
    }

    void number(int value) {
        if (used + NUMBER_RESERVE >= OUTPUT_SIZE)
            flush();
        if (!first)
            bytes[used++] = ' ';
        first = false;
        char digits[NUMBER_RESERVE];
        int count = 0;
        do {
            digits[count++] = char('0' + value % 10);
            value /= 10;
        } while (value);
        while (count)
            bytes[used++] = digits[--count];
    }

    void line() {
        bytes[used++] = '\n';
        first = true;
    }
};

const int INPUT_SIZE = 4096;

struct Input {
    unsigned char bytes[INPUT_SIZE];
    int position = 0, length = 0;

    int next() {
        if (position == length) {
            length = int(fread(bytes, 1, sizeof(bytes), stdin));
            position = 0;
            if (!length)
                return 0;
        }
        return bytes[position++];
    }

    int number() {
        int c = next(), value = 0;
        while (c && c <= ' ')
            c = next();
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = next();
        }
        return value;
    }
};

int main() {
    Input input;
    int n = input.number(), r = input.number();
    std::vector<int> sizes(n);
    for (int &value : sizes)
        value = input.number();
    int trips = 0, left = 0;
    for (int right = 0; right < n; ++right) {
        while (sizes[right] - sizes[left] > r)
            ++left;
        if (right - left + 1 > trips)
            trips = right - left + 1;
    }
    Output output;
    output.number(trips);
    output.line();
    // Every next coat in a trip is trips positions later, outside any width-r window.
    for (int trip = 0; trip < trips; ++trip) {
        output.number((n - trip + trips - 1) / trips);
        for (int coat = trip + 1; coat <= n; coat += trips)
            output.number(coat);
        output.line();
    }
    output.flush();
}
