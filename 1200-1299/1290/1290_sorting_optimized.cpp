#include <cstdio>

const int LARGEST = 25000;
const int OUTPUT_LINE_SIZE = 8;

constexpr int INPUT_BUFFER_SIZE = 8192;

// the numbers are parsed by hand from 8 KB blocks, faster than scanf
int readInt() {
    static char buffer[INPUT_BUFFER_SIZE];
    static size_t position = 0;
    static size_t length = 0;
    int value = 0;
    bool started = false;
    for (;;) {
        if (position == length) {
            length = fread(buffer, 1, sizeof(buffer), stdin);
            position = 0;
            if (length == 0)
                return value;
        }
        char c = buffer[position++];
        if (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            started = true;
        } else if (started) {
            return value;
        }
    }
}

int main() {
    int n = readInt();
    // counting each value is a sort in descending order, and printing the
    // conjugate partition twice gives back the sorted array; at most 25 000
    // numbers, so an unsigned short holds every count
    static unsigned short count[LARGEST + 1];
    for (int i = 0; i < n; i++)
        count[readInt()]++;
    char line[OUTPUT_LINE_SIZE];
    for (int value = LARGEST; value >= 1; value--) {
        if (count[value] == 0)
            continue;
        // each value is formatted once and its line written count times
        int length = snprintf(line, sizeof(line), "%d\n", value);
        for (int k = 0; k < count[value]; k++)
            fwrite(line, 1, length, stdout);
    }
}
