#include <cstdio>

constexpr int INPUT_SIZE = 8192;
char input[INPUT_SIZE];
int position = 0, length = 0;

int next_byte() {
    if (position == length) {
        length = fread(input, 1, INPUT_SIZE, stdin);
        position = 0;
        if (length == 0)
            return -1;
    }
    return input[position++];
}

int number() {
    int c = next_byte();
    while (c >= 0 && c <= ' ')
        c = next_byte();
    int value = 0;
    while (c >= '0' && c <= '9') {
        value = value * 10 + c - '0';
        c = next_byte();
    }
    return value;
}

int main() {
    int divisor = number() + 1, sets = number();
    number();
    puts("YES");
    for (int set = 0; set < sets; ++set) {
        int count = number(), sum = 0;
        for (int item = 0; item < count; ++item)
            sum += number();
        // Similar multisets change the sum by a nonzero value smaller than divisor.
        printf("%d\n", sum % divisor + 1);
    }
}
