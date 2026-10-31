#include <cstdio>

using Wide = unsigned __int128;
const int MAX_DIGITS = 22;

int main() {
    int n;
    scanf("%d", &n);
    // n <= 21: the sum is below 21 * 21! < 10^22, safely within 128 bits.
    Wide total = 0, ways = n;
    for (int k = 2; k <= n; ++k) {
        ways *= n - k + 1;
        total += ways;
    }
    // the bound above leaves space for every digit and a string terminator.
    char digits[MAX_DIGITS + 1];
    int start = MAX_DIGITS;
    digits[start] = '\0';
    do {
        digits[--start] = static_cast<char>('0' + total % 10);
        total /= 10;
    } while (total > 0);
    puts(digits + start);
}
