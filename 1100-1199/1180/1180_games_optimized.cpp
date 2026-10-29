#include <cstdio>

const int SPLIT = 3;

int main() {
    // the digits are summed as they are read, the number is never stored
    int ch;
    do {
        ch = std::getchar();
    } while (ch != EOF && ch <= ' ');
    int digitSum = 0;
    while (ch >= '0' && ch <= '9') {
        digitSum += ch - '0';
        ch = std::getchar();
    }
    // no power of two is divisible by 3, so from a multiple of 3 every move
    // leaves a non-multiple, and from a non-multiple taking 1 or 2 stones
    // leaves a multiple; the remainder is also the smallest such move
    int remainder = digitSum % SPLIT;
    if (remainder == 0) {
        std::puts("2");
    } else {
        std::puts("1");
        std::putchar('0' + remainder);
        std::putchar('\n');
    }
}
