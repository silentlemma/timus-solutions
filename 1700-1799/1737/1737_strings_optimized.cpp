#include <cstdio>

constexpr std::size_t INPUT_SIZE = 256;
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

#include <cstring>

constexpr int LIMIT = 100000, PERIOD = 3, WORDS = PERIOD * (PERIOD - 1);
const char LETTERS[] = "abc";
char output[LIMIT + WORDS];

int main() {
    int n;
    if (!read_integer(n))
        return 0;
    if (n == 1) {
        int used = 0;
        for (char letter : LETTERS) {
            if (letter != 0) {
                output[used++] = letter;
                output[used++] = '\n';
            }
        }
        std::fwrite(output, 1, used, stdout);
        return 0;
    }
    if (WORDS * n > LIMIT) {
        const char message[] = "TOO LONG\n";
        std::fwrite(message, 1, sizeof message - 1, stdout);
        return 0;
    }
    int used = 0;
    for (int first = 0; first < PERIOD; first++)
        for (int second = 0; second < PERIOD; second++)
            if (first != second) {
                const int third = PERIOD - first - second;
                const char pattern[] = {LETTERS[first], LETTERS[second], LETTERS[third]};
                char *word = output + used;
                int filled = n < PERIOD ? n : PERIOD;
                std::memcpy(word, pattern, filled);
                // Every complete copied prefix has length divisible by three.
                while (filled < n) {
                    const int take = filled < n - filled ? filled : n - filled;
                    std::memcpy(word + filled, word, take);
                    filled += take;
                }
                used += n;
                output[used++] = '\n';
            }
    std::fwrite(output, 1, used, stdout);
    return 0;
}
