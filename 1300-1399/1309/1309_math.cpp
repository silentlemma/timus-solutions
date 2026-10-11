#include <cstdio>

const long long MOD = 9973;
const long long COEF_X = 3, COEF_Y = 7;

// g(x, y) = y (x^5 - x + 7) + (x^3 + 3x - x^5) is the map y -> a y + b
// modulo 9973, and it depends only on x mod 9973
void step(long long x, long long &a, long long &b) {
    long long x3 = x * x % MOD * x % MOD, x5 = x3 * x % MOD * x % MOD;
    a = ((x5 - x + COEF_Y) % MOD + MOD) % MOD;
    b = ((x3 + COEF_X * x - x5) % MOD + MOD) % MOD;
}

int main() {
    long long n = 0;
    if (scanf("%lld", &n) != 1)
        return 0;
    long long whole = n / MOD, rest = n % MOD;
    // x = 1 .. 9973 compose into one map, the same for every full period
    long long bigA = 1, bigB = 0, a = 0, b = 0;
    for (long long x = 1; x <= MOD; x++) {
        step(x, a, b);
        bigB = (a * bigB + b) % MOD;
        bigA = a * bigA % MOD;
    }
    long long y = 0;
    for (long long k = 0; k < whole; k++)
        y = (bigA * y + bigB) % MOD;
    for (long long x = 1; x <= rest; x++) {
        step(x, a, b);
        y = (a * y + b) % MOD;
    }
    printf("%lld\n", y);
    return 0;
}
