#include <cstdio>

const int MOD = 100;
const int BASES = 4;
const int TEN = 10;

int power(int base, int n) {
    int r = 1;
    for (; n > 0; n >>= 1, base = base * base % MOD) {
        if (n & 1)
            r = r * base % MOD;
    }
    return r;
}

int main() {
    int n = 0;
    if (scanf("%d", &n) != 1)
        return 0;
    // from the second power on the sum is even but never divisible by 8,
    // so it ends in at most two zeros and its remainder mod 100 decides
    int s = 0;
    for (int b = 1; b <= BASES; b++)
        s = (s + power(b, n)) % MOD;
    printf("%d\n", s == 0 ? 2 : s % TEN == 0 ? 1 : 0);
    return 0;
}
