#include <cstdio>

const long long FIRST_ODD = 3;  // the smallest divisor worth trying

// whether n is a product of an odd number of factors, each 2 or an odd
// number above 1: n = 2^twos * rest with rest odd
bool paid(long long n) {
    int twos = 0;
    while (n % 2 == 0) {
        n /= 2;
        twos++;
    }
    if (n == 1) {
        return twos % 2 == 1;
    }
    if (twos % 2 == 0) {
        return true;  // rest as a single factor
    }
    // an odd count needs rest split into two factors, so not a prime
    for (long long d = FIRST_ODD; d * d <= n; d += 2) {
        if (n % d == 0) {
            return true;
        }
    }
    return false;
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        long long n;
        scanf("%lld", &n);
        puts(paid(n) ? "YES" : "NO");
    }
}
