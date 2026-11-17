#include <cstdio>

constexpr int TARGET = 20;
constexpr unsigned long long FIRST_ODD = 3;

bool enough(unsigned long long n, unsigned long long divisor, int needed) {
    // Every remaining prime factor is at least this untested divisor.
    unsigned long long minimum = 1;
    for (int i = 0; i < needed; ++i) {
        if (minimum > n / divisor)
            return false;
        minimum *= divisor;
    }
    return true;
}

int main() {
    unsigned long long n;
    if (scanf("%llu", &n) != 1)
        return 0;
    int count = 0;
    while (n % 2 == 0) {
        n /= 2;
        ++count;
    }
    unsigned long long divisor = FIRST_ODD;
    while (count < TARGET && divisor <= n / divisor) {
        if (TARGET - count > 2 && !enough(n, divisor, TARGET - count))
            break;
        while (n % divisor == 0) {
            n /= divisor;
            ++count;
        }
        divisor += 2;
    }
    // Once the square bound is passed, one residual prime remains.
    if (n > 1 && divisor > n / divisor) {
        ++count;
        n = 1;
    }
    puts(count == TARGET && n == 1 ? "Yes" : "No");
}
