#include <cstdio>

constexpr int BASE = 10;
constexpr int LIMIT = BASE * BASE - 1;
// the d-th character is digit d turned upside down, as in the statement, and
// ? marks a digit that reads as nothing
constexpr char TURN[] = "01????9?86";

int main() {
    // n is read with getchar and the digits written with putchar, without iostream
    int count = 0;
    int ch;
    do {
        ch = std::getchar();
    } while (ch != EOF && ch <= ' ');
    while (ch >= '0' && ch <= '9') {
        count = count * BASE + ch - '0';
        ch = std::getchar();
    }
    int run = 0;
    for (int value = 1; value <= LIMIT; ++value) {
        if (TURN[value / BASE] != '?' && TURN[value % BASE] != '?')
            ++run;
        else
            run = 0;
        if (run >= count) {
            for (int target = value; target > value - count; --target) {
                std::putchar(TURN[target % BASE]);
                std::putchar(TURN[target / BASE]);
                std::putchar(target == value - count + 1 ? '\n' : ' ');
            }
            return 0;
        }
    }
    std::puts("Glupenky Pierre");
}
