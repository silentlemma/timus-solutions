#include <cstdio>

// x^exponent mod modulus by repeated squaring
int power(int x, int exponent, int modulus) {
    int result = 1;
    for (; exponent > 0; exponent >>= 1) {
        if (exponent & 1)
            result = result * x % modulus;
        x = x * x % modulus;
    }
    return result;
}

int main() {
    int exponent, modulus, remainder;
    if (scanf("%d %d", &exponent, &modulus) != 2 || scanf("%d", &remainder) != 1)
        return 0;
    // every root is printed as soon as it is found, without a vector of them
    bool found = false;
    // only M candidates; a Y of M or more is never a remainder
    if (remainder < modulus) {
        for (int x = 0; x < modulus; ++x) {
            if (power(x, exponent, modulus) == remainder) {
                if (found)
                    putchar(' ');
                printf("%d", x);
                found = true;
            }
        }
    }
    if (!found)
        printf("-1");
    putchar('\n');
}
