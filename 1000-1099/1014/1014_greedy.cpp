#include <cstdio>
#include <string>

const int BASE = 10;

int main() {
    long long n;
    if (scanf("%lld", &n) != 1)
        return 1;
    // a zero digit makes the product zero: 10 is the smallest such number
    if (n == 0) {
        printf("%d\n", BASE);
        return 0;
    }
    if (n == 1) {
        printf("1\n");
        return 0;
    }
    // the largest digits first give the fewest digits; then sort them up
    std::string digits;
    for (int d = BASE - 1; d >= 2; d--)
        while (n % d == 0) {
            digits.insert(digits.begin(), char('0' + d));
            n /= d;
        }
    printf("%s\n", n == 1 ? digits.c_str() : "-1");
}
