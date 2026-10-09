#include <cmath>
#include <cstdio>

// Lagrange: every number is a sum of four squares, and Legendre: exactly the
// numbers 4^a (8b + 7) need all four
const int MOST = 4;
const int POWER = 4;
const int MODULUS = 8;
const int REST = 7;

bool is_square(int v) {
    int r = (int)std::lround(std::sqrt((double)v));
    return r * r == v;
}

int count(int n) {
    if (is_square(n))
        return 1;
    for (int a = 1; a * a < n; a++)
        if (is_square(n - a * a))
            return 2;
    while (n % POWER == 0)
        n /= POWER;
    return n % MODULUS == REST ? MOST : MOST - 1;
}

int main() {
    int n;
    if (scanf("%d", &n) == 1)
        printf("%d\n", count(n));
}
