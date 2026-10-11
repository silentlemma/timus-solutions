#include <cstdio>
#include <vector>

const int THREE = 3, FOUR = 4, BASE = 10;

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
    std::vector<int> digits = {rest > 0 ? rest : 1}; // lowest first
    for (int i = 0; i < threes; i++) {
        int carry = 0;
        for (int &d : digits) {
            int v = d * THREE + carry;
            d = v % BASE;
            carry = v / BASE;
        }
        if (carry > 0) {
            digits.push_back(carry);
        }
    }
    for (int i = (int)digits.size() - 1; i >= 0; i--) {
        putchar('0' + digits[i]);
    }
    putchar('\n');
}
