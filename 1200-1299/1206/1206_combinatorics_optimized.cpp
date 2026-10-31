#include <cstdio>

const int FIRST = 36, OTHER = 55, MAX_LENGTH = 50;

int main() {
    int k;
    scanf("%d", &k);
    // 36 * 55^(k - 1) < 100^k and k <= 50, so 100 decimal digits suffice.
    int digits[2 * MAX_LENGTH] = {FIRST % 10, FIRST / 10};
    int size = 2;
    for (int i = 1; i < k; ++i) {
        int carry = 0;
        for (int j = 0; j < size; ++j) {
            int value = digits[j] * OTHER + carry;
            digits[j] = value % 10;
            carry = value / 10;
        }
        while (carry > 0) {
            digits[size++] = carry % 10;
            carry /= 10;
        }
    }
    while (size > 0)
        putchar('0' + digits[--size]);
    putchar('\n');
}
