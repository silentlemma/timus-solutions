#include <cstdio>

constexpr std::size_t INPUT_SIZE = 16384;
unsigned char input_buffer[INPUT_SIZE + 1];
unsigned char *input_position = input_buffer, *input_end = input_buffer;

bool refill() {
    const std::size_t size = std::fread(input_buffer, 1, INPUT_SIZE, stdin);
    input_position = input_buffer;
    input_end = input_buffer + size;
    *input_end = 0;
    return size != 0;
}

bool read_integer(int &answer) {
    // The extra byte is a sentinel; only a token boundary needs a refill test.
    while (*input_position <= ' ') {
        if (input_position == input_end) {
            if (!refill())
                return false;
        } else {
            ++input_position;
        }
    }
    const bool negative = *input_position == '-';
    if (negative)
        ++input_position;
    int value = 0;
    for (;;) {
        while (*input_position >= '0' && *input_position <= '9') {
            value = value * 10 + *input_position - '0';
            ++input_position;
        }
        if (input_position == input_end) {
            if (refill())
                continue;
        } else {
            ++input_position;
        }
        answer = negative ? -value : value;
        return true;
    }
}

int number() {
    int answer = 0;
    read_integer(answer);
    return answer;
}

constexpr int OUTPUT_SIZE = 128, INTEGER_DIGITS = 20, DECIMAL = 10;
char output[OUTPUT_SIZE];
int output_size = 0;

void output_number(long long value) {
    char digits[INTEGER_DIGITS];
    int length = 0;
    do {
        digits[length++] = static_cast<char>('0' + value % DECIMAL);
        value /= DECIMAL;
    } while (value != 0);
    while (length != 0)
        output[output_size++] = digits[--length];
}

int main() {
    const int start = number();
    const int end = number();
    int previous = number(), direction = 0, pieces = 1;
    for (int index = start; index < end; ++index) {
        const int current = number();
        const int step = (current > previous) - (current < previous);
        if (step && direction && step != direction) {
            // The step crossing the boundary sets no direction in the new piece.
            ++pieces;
            direction = 0;
        } else if (!direction) {
            direction = step;
        }
        previous = current;
    }
    output_number(pieces);
    output[output_size++] = '\n';
    std::fwrite(output, 1, output_size, stdout);
    return 0;
}
