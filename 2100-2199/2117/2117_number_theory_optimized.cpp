#include <cmath>
#include <cstdint>
#include <cstdio>

using u64 = uint64_t;
const u64 FIRST_ODD_PRIME = 3;
const u64 FIRST_WHEEL_DIVISOR = 5;
const u64 WHEEL_PERIOD = 6;

u64 isqrt(u64 value) {
    u64 root = static_cast<u64>(sqrtl(static_cast<long double>(value)));
    while (root * root > value)
        --root;
    while ((root + 1) * (root + 1) <= value)
        ++root;
    return root;
}

void remove(u64 &value, u64 divisor, u64 &root) {
    u64 square = divisor * divisor;
    while (value % square == 0) {
        value /= square;
        root *= divisor;
    }
    if (value % divisor == 0)
        value /= divisor;
}

int main() {
    unsigned long long input;
    if (scanf("%llu", &input) != 1)
        return 0;
    u64 value = input;
    u64 root = isqrt(value);
    if (root * root == value) {
        printf("%llu\n", static_cast<unsigned long long>(root / 2 + 1));
        return 0;
    }
    root = 1;
    remove(value, 2, root);
    remove(value, FIRST_ODD_PRIME, root);
    // Past this cube bound the residual has at most two prime factors.
    for (u64 divisor = FIRST_WHEEL_DIVISOR, step = 2; divisor * divisor * divisor <= value;
         divisor += step, step = WHEEL_PERIOD - step)
        remove(value, divisor, root);
    u64 tail = isqrt(value);
    if (tail * tail == value)
        root *= tail;
    printf("%llu\n", static_cast<unsigned long long>(root / 2 + 1));
}
