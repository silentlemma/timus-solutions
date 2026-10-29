#include <cstdio>

const int DWARFS = 7;

int main() {
    // the number has up to 51 digits, so take it modulo 7 digit by digit
    int rest = 0;
    // the digits are folded as getchar reads them; the number is never stored
    for (int ch; (ch = getchar()) != EOF;) {
        if (ch >= '0' && ch <= '9')
            rest = (rest * 10 + ch - '0') % DWARFS;
    }
    putchar('0' + rest);
    putchar('\n');
}
