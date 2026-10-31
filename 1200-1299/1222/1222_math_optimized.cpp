#include <cstdio>

const int THREE = 3, FOUR = 4, BASE = 10;

// n <= 3000 gives a product <= 3^1000 < 10^1000, so these digits suffice.
const int MAX_DIGITS = 1000;
int digits[MAX_DIGITS];

int main() {
    int n;
    scanf("%d", &n);
    // threes are best: a 4 or more splits into parts with a larger product, and
    // three 2s lose to two 3s; a leftover 1 joins a 3 to make 2 + 2
    if (n < FOUR) {
        printf("%d\n", n);
        return 0;
    }
    int threes = n / THREE, rest = n % THREE;
    if (rest == 1) {
        threes--;
        rest = FOUR;
    }
    int size = 1;
    digits[0] = rest > 0 ? rest : 1; // lowest first
    for (int i = 0; i < threes; i++) {
        int carry = 0;
        for (int j = 0; j < size; j++) {
            int &d = digits[j];
            int v = d * THREE + carry;
            d = v % BASE;
            carry = v / BASE;
        }
        if (carry > 0) {
            digits[size++] = carry;
        }
    }
    for (int i = size - 1; i >= 0; i--) {
        putchar('0' + digits[i]);
    }
    putchar('\n');
}
