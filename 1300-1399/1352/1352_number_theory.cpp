#include <cstdio>

// the exponents p of the first 38 Mersenne primes 2^p - 1 (OEIS A000043)
const int EXPONENTS[] = {
    2,      3,      5,      7,       13,      17,      19,      31,      61,     89,
    107,    127,    521,    607,     1279,    2203,    2281,    3217,    4253,   4423,
    9689,   9941,   11213,  19937,   21701,   23209,   44497,   86243,   110503, 132049,
    216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593,
};

int main() {
    int count = 0;
    if (scanf("%d", &count) != 1)
        return 0;
    for (int i = 0; i < count; i++) {
        int n = 0;
        if (scanf("%d", &n) != 1)
            return 0;
        printf("%d\n", EXPONENTS[n - 1]);
    }
    return 0;
}
