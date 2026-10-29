#include <cstdio>

constexpr int SIDE = 8;

// how many of position - step and position + step stay on the board
int ways(int position, int step) { return (position >= step) + (position + step < SIDE); }

int main() {
    // the input is read with getchar, without iostream
    int n = 0, c = getchar();
    while (c <= ' ' && c != EOF) {
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        n = n * 10 + c - '0';
        c = getchar();
    }
    while (n--) {
        do {
            c = getchar();
        } while (c <= ' ' && c != EOF);
        int x = c - 'a', y = getchar() - '1';
        // a jump moves one coordinate by 1 and the other by 2, each either way,
        // and the choices for the two coordinates are independent
        int count = ways(x, 1) * ways(y, 2) + ways(x, 2) * ways(y, 1);
        // at most 8 squares: a single digit
        putchar('0' + count);
        putchar('\n');
    }
}
