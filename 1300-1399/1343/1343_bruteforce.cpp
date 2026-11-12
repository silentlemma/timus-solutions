#include <cstdio>

using u64 = unsigned long long;

const int DIGITS = 12;
const u64 THREE = 3, FIRST_DIVISOR = 5, DIVISOR_STEP = 6;

bool isPrime(u64 number) {
    if (number < 2)
        return false;
    if (number % 2 == 0 || number % THREE == 0)
        return number == 2 || number == THREE;
    // Every prime larger than three is 6k-1 or 6k+1.
    for (u64 divisor = FIRST_DIVISOR; divisor * divisor <= number; divisor += DIVISOR_STEP)
        if (number % divisor == 0 || number % (divisor + 2) == 0)
            return false;
    return true;
}

int main() {
    int count;
    if (scanf("%d", &count) != 1)
        return 0;
    u64 number = 0;
    for (int i = 0; i < count; ++i) {
        char digit;
        scanf(" %c", &digit);
        number = number * 10 + digit - '0';
    }
    for (int i = count; i < DIGITS; ++i)
        number *= 10;
    // A complete prefix is already valid by the input guarantee (including 1).
    if (count < DIGITS) {
        if (number <= 2)
            number = 2;
        else {
            if (number % 2 == 0)
                ++number;
            while (!isPrime(number))
                number += 2;
        }
    }
    printf("%012llu\n", number);
}
