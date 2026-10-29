#include <cstdio>

// digits seen in the window
const int WINDOW = 10;
const int MAX_DIGITS = 1000;

int main() {
    int n, clicks;
    if (scanf("%d %d", &n, &clicks) != 2)
        return 0;
    // the digits are read as characters and printed with putchar, with no
    // conversion to numbers and no string
    char digits[MAX_DIGITS];
    for (int i = 0; i < n; ++i)
        if (scanf(" %c", &digits[i]) != 1)
            return 0;
    // each click moves the window one digit on, around the wheel
    for (int i = 0; i < WINDOW; ++i)
        putchar(digits[(clicks + i) % n]);
    putchar('\n');
}
