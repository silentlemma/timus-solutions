#include <cstdint>
#include <cstdio>

const int TOP = 40;

int main() {
    int n, a, b;
    if (scanf("%d", &n) != 1 || scanf("%d %d", &a, &b) != 2)
        return 0;
    // Pascal's triangle; the binomials stay below 2^32
    static uint64_t c[TOP][TOP] = {};
    for (int i = 0; i < TOP; i++) {
        c[i][0] = 1;
        for (int j = 1; j <= i; j++)
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
    }
    // up to a identical balls in n boxes: put the unused ones in an extra box,
    // then it is a stars-and-bars count C(a + n, n); the colours are
    // independent, and the product reaches 1.05 * 10^19, past signed 64 bits
    printf("%llu\n", (unsigned long long)(c[a + n][n] * c[b + n][n]));
}
