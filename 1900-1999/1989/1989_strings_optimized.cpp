#include <cstdio>
#include <cstring>

constexpr int MAX_LENGTH = 100000;
constexpr int BUFFER_SIZE = 16384;
constexpr int DECIMAL = 10;
static char word[MAX_LENGTH], reversed[MAX_LENGTH];
static unsigned char buffer[BUFFER_SIZE];
static int position, available;

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(buffer, 1, sizeof buffer, stdin));
        position = 0;
        if (available == 0)
            return EOF;
    }
    return buffer[position++];
}

int start_token() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    return ch;
}

int next_int() {
    int value = 0;
    for (int ch = start_token(); ch >= '0' && ch <= '9'; ch = next_byte())
        value = value * DECIMAL + ch - '0';
    return value;
}

int main() {
    int size = 0;
    for (int ch = start_token(); ch > ' '; ch = next_byte())
        word[size++] = static_cast<char>(ch);
    int changes = 0;
    for (int i = 0; i < size; ++i) {
        reversed[size - 1 - i] = word[i];
        if (i > 0)
            changes += word[i - 1] != word[i];
    }
    for (int count = next_int(); count > 0; --count) {
        const bool update = start_token() == 'c';
        for (int ch = next_byte(); ch > ' '; ch = next_byte()) {
        }
        const int left = next_int() - 1;
        if (update) {
            const char value = static_cast<char>(start_token());
            if (left > 0)
                changes += (word[left - 1] != value) - (word[left - 1] != word[left]);
            if (left + 1 < size)
                changes += (word[left + 1] != value) - (word[left + 1] != word[left]);
            word[left] = reversed[size - 1 - left] = value;
        } else {
            const int end = next_int();
            const int half = (end - left) / 2;
            const bool palindrome =
                changes == 0 || std::memcmp(word + left, reversed + size - end, half) == 0;
            std::puts(palindrome ? "Yes" : "No");
        }
    }
}
