#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    // Euler's totient: the turns 2*pi*m/n with gcd(m, n) = 1
    int phi = n, rest = n;
    for (int p = 2; p * p <= rest; p++) {
        if (rest % p == 0) {
            while (rest % p == 0)
                rest /= p;
            phi -= phi / p;
        }
    }
    if (rest > 1)
        phi -= phi / rest;
    printf("%d\n", phi / 2);
}
