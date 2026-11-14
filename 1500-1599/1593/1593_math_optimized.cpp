#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <set>

using Number = uint64_t;
const Number BASES[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
const int BATCH = 64;
const int MAX_CYCLE = 1 << 16;

Number multiply(Number a, Number b, Number n) { return static_cast<__uint128_t>(a) * b % n; }

Number power(Number a, Number exponent, Number n) {
    Number result = 1;
    for (; exponent; exponent >>= 1, a = multiply(a, a, n))
        if (exponent & 1)
            result = multiply(result, a, n);
    return result;
}

bool prime(Number n) {
    for (Number p : BASES)
        if (n % p == 0)
            return n == p;
    Number odd = n - 1;
    int twos = 0;
    while (!(odd & 1)) {
        odd >>= 1;
        ++twos;
    }
    for (Number a : BASES) {
        Number value = power(a, odd, n);
        if (value == 1)
            continue;
        for (int i = 1; i < twos && value != n - 1; ++i)
            value = multiply(value, value, n);
        if (value != n - 1)
            return false;
    }
    return true;
}

Number distance(Number a, Number b) { return a < b ? b - a : a - b; }

Number divisor(Number n) {
    for (Number c = 1;; ++c) {
        auto step = [n, c](Number a) { return (multiply(a, a, n) + c) % n; };
        Number x = 0, y = 2, saved = 0, factor = 1;
        for (int size = 1; size <= MAX_CYCLE && factor == 1; size *= 2) {
            x = y;
            for (int i = 0; i < size; ++i)
                y = step(y);
            for (int start = 0; start < size && factor == 1; start += BATCH) {
                saved = y;
                Number product = 1;
                for (int i = 0; i < std::min(BATCH, size - start); ++i) {
                    y = step(y);
                    product = multiply(product, distance(x, y), n);
                }
                factor = std::gcd(product, n);
            }
        }
        if (factor == n) {
            do {
                saved = step(saved);
                factor = std::gcd(distance(x, saved), n);
            } while (factor == 1);
        }
        if (factor > 1 && factor < n)
            return factor;
    }
}

bool square(Number n) {
    Number root = std::sqrt(static_cast<double>(n));
    return root * root == n || (root + 1) * (root + 1) == n;
}

constexpr int POWER_OF_FOUR = 4;
constexpr int LEGENDRE_MODULUS = 8;
constexpr int LEGENDRE_RESIDUE = 7;
constexpr int TWO_SQUARE_OBSTRUCTION = 3;
constexpr int THREE_SQUARES = 3;
constexpr int FOUR_SQUARES = 4;

void collect(Number n, std::set<Number> &odd_factors) {
    if (square(n))
        return;
    if (prime(n)) {
        if (n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION && !odd_factors.erase(n))
            odd_factors.insert(n);
        return;
    }
    Number part = divisor(n);
    collect(part, odd_factors);
    collect(n / part, odd_factors);
}

int solve(Number n) {
    if (square(n))
        return 1;
    while (n % POWER_OF_FOUR == 0)
        n /= POWER_OF_FOUR;
    if (n % LEGENDRE_MODULUS == LEGENDRE_RESIDUE)
        return FOUR_SQUARES;
    if (n % 2 == 0)
        n /= 2;
    if (n % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION)
        return THREE_SQUARES;
    for (Number p : BASES) {
        bool odd = false;
        while (n % p == 0) {
            n /= p;
            odd = !odd;
        }
        if (odd && p % POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION)
            return THREE_SQUARES;
    }
    std::set<Number> odd_factors;
    collect(n, odd_factors);
    return odd_factors.empty() ? 2 : THREE_SQUARES;
}

int main() {
    unsigned long long n;
    if (scanf("%llu", &n) == 1)
        printf("%d\n", solve(n));
}
