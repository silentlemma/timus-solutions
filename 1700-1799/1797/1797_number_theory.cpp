#include <iostream>
#include <numeric>
#include <utility>

typedef unsigned long long u64;
typedef unsigned __int128 u128;

// sum of floor((a * i + b) / m) over i = 0 .. n - 1
u128 floorSum(u128 n, u128 m, u128 a, u128 b) {
    u128 total = 0;
    while (true) {
        if (a >= m) {
            total += n * (n - 1) / 2 * (a / m);
            a %= m;
        }
        if (b >= m) {
            total += n * (b / m);
            b %= m;
        }
        u128 top = a * n + b;
        if (top < m) return total;
        n = top / m;
        b = top % m;
        std::swap(m, a);
    }
}

// how many numbers from 1 to limit are a * x + b * y with a, b >= 0
u64 countUpTo(u64 limit, u64 x, u64 y) {
    u64 g = std::gcd(x, y);
    limit /= g;
    x /= g;
    y /= g;
    // with x and y coprime every such number has exactly one form with
    // b < x; for each b the values of a run from 0 to (limit - b*y) / x
    u64 last = limit / y < x - 1 ? limit / y : x - 1;
    u128 forms = floorSum(last + 1, x, y, limit - y * last) + last + 1;
    return (u64)(forms - 1);  // zero is not a volume size
}

int main() {
    int tests;
    if (!(std::cin >> tests)) return 0;
    while (tests--) {
        u64 x, y, l, r;
        if (!(std::cin >> x >> y >> l >> r)) break;
        std::cout << countUpTo(r, x, y) - countUpTo(l - 1, x, y) << "\n";
    }
    return 0;
}
