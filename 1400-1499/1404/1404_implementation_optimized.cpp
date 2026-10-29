#include <cstdio>

// added to the first letter
const int SHIFT = 5;
const int LETTERS = 26;

int main() {
    // each code is the previous code plus the letter, modulo 26: take differences
    int previous = SHIFT;
    int ch;
    while ((ch = std::getchar()) != EOF && ch <= ' ') {
    }
    // each letter is decoded and printed as soon as it is read
    while (ch >= 'a' && ch <= 'z') {
        int code = ch - 'a';
        std::putchar('a' + (code - previous + LETTERS) % LETTERS);
        previous = code;
        ch = std::getchar();
    }
    std::putchar('\n');
}
