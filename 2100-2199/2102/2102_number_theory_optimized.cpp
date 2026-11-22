#include <cstdio>

constexpr int TARGET = 20;
constexpr unsigned long long FIRST_ODD = 3, FIRST_WHEEL = 5, WHEEL = 6;

bool enough(unsigned long long n, unsigned long long divisor, int needed) {
    // Every remaining prime factor is at least this untested divisor.
    unsigned __int128 minimum = 1;
    for (int i = 0; i < needed; ++i) {
        minimum *= divisor;
        if (minimum > n)
            return false;
    }
    return true;
}

int main() {
    unsigned long long n;
    if (scanf("%llu", &n) != 1)
        return 0;

    int count = __builtin_ctzll(n);
    n >>= count;
    while (n % FIRST_ODD == 0) {
        n /= FIRST_ODD;
        ++count;
    }
    unsigned long long divisor = FIRST_WHEEL, step = 2;
    while (count < TARGET && divisor * divisor <= n) {
        if (TARGET - count > 2 && !enough(n, divisor, TARGET - count))
            break;
        while (n % divisor == 0) {
            n /= divisor;
            ++count;
        }
        divisor += step;
        step = WHEEL - step;
    }
    // Once the square bound is passed, one residual prime remains.
    if (n > 1 && divisor * divisor > n) {
        ++count;
        n = 1;
    }
    puts(count == TARGET && n == 1 ? "Yes" : "No");
}
