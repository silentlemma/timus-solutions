#include <cstdio>
#include <vector>

int main() {
    const int FIRST = 36, OTHER = 55, BASE = 10;
    int k;
    scanf("%d", &k);
    // no position may carry: 36 pairs of leading digits with a sum of at
    // most 9, and 55 pairs of digits from 0 in every other position
    std::vector<int> digits = {FIRST % BASE, FIRST / BASE}; // lowest first
    for (int i = 1; i < k; i++) {
        int carry = 0;
        for (int &d : digits) {
            int v = d * OTHER + carry;
            d = v % BASE;
            carry = v / BASE;
        }
        for (; carry > 0; carry /= BASE) {
            digits.push_back(carry % BASE);
        }
    }
    for (int i = (int)digits.size() - 1; i >= 0; i--) {
        putchar('0' + digits[i]);
    }
    putchar('\n');
}
