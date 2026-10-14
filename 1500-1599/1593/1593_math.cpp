#include <cmath>
#include <cstdio>

const long long FOUR = 4, SEVEN = 7, EIGHT = 8;
const long long RESIDUE = 3;   // the primes 4k + 3
const long long FIRST_ODD = 3; // the first odd divisor to try
const int THREE_SQUARES = 3, FOUR_SQUARES = 4;

bool isSquare(long long n) {
    long long r = (long long)sqrtl((long double)n);
    while (r * r > n)
        r--;
    while ((r + 1) * (r + 1) <= n)
        r++;
    return r * r == n;
}

// Fermat: every prime 4k + 3 must appear an even number of times
bool twoSquares(long long n) {
    while (n % 2 == 0)
        n /= 2;
    for (long long d = FIRST_ODD; d * d <= n; d += 2) {
        int count = 0;
        while (n % d == 0) {
            n /= d;
            count++;
        }
        if (d % FOUR == RESIDUE && count % 2 == 1)
            return false;
    }
    // what is left is 1 or a prime
    return n % FOUR != RESIDUE;
}

int main() {
    long long n;
    if (scanf("%lld", &n) != 1)
        return 0;
    long long m = n;
    while (m % FOUR == 0)
        m /= FOUR;
    if (isSquare(n))
        printf("1\n");
    else if (twoSquares(n))
        printf("2\n");
    else if (m % EIGHT == SEVEN)
        printf("%d\n", FOUR_SQUARES); // Legendre: exactly the numbers 4^a (8b + 7) need four
    else
        printf("%d\n", THREE_SQUARES);
}
