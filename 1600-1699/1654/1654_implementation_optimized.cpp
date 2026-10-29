#include <cstdio>

int main() {
    constexpr int MAX_LENGTH = 200000;
    constexpr int INPUT_BUFFER_SIZE = 4096;
    // the letters go straight from 4 KB input blocks onto a fixed stack
    static char stack[MAX_LENGTH];
    char buffer[INPUT_BUFFER_SIZE];
    int size = 0;
    std::size_t length;
    while ((length = std::fread(buffer, 1, sizeof(buffer), stdin)) != 0) {
        for (std::size_t i = 0; i < length; ++i) {
            char ch = buffer[i];
            if (ch < 'a' || ch > 'z')
                continue;
            // a letter equal to the one before it cancels that one: removing the
            // inserted pairs in any order leaves the same text
            if (size > 0 && stack[size - 1] == ch)
                --size;
            else
                stack[size++] = ch;
        }
    }
    std::fwrite(stack, 1, size, stdout);
    std::putchar('\n');
}
