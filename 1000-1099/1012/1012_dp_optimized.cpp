#include <cstdio>
#include <utility>
const int MAX_SUM = 1800, LIMB_DIGITS = 9;
// big numbers: base 10^9 digits, least significant first.
const long long BASE = 1000000000;
// the answer is below 10^n, with n < 1800: these base-10^9 arrays always suffice.
const int LIMBS = MAX_SUM / LIMB_DIGITS + 1;
long long zero[LIMBS], other[LIMBS];
int main() {
    int n, k;
    if (scanf("%d%d", &n, &k) != 2)
        return 0;
    // numbers of valid prefixes ending with a zero and with another digit,
    // where the first digit is not zero.
    int used = 1;
    other[0] = k - 1;
    for (int i = 1; i < n; i++) {
        long long carry = 0;
        for (int j = 0; j < used; j++) {
            // k <= 10 makes the intermediate smaller than 18 * base, within int64.
            long long next = (zero[j] + other[j]) * (k - 1) + carry;
            zero[j] = other[j];
            other[j] = next % BASE;
            carry = next / BASE;
        }
        if (carry)
            other[used++] = carry;
    }
    long long carry = 0;
    for (int j = 0; j < used; j++) {
        long long next = zero[j] + other[j] + carry;
        other[j] = next % BASE;
        carry = next / BASE;
    }
    if (carry)
        other[used++] = carry;
    printf("%lld", other[used - 1]);
    for (int j = used - 2; j >= 0; j--)
        printf("%09lld", other[j]);
    putchar('\n');
}
