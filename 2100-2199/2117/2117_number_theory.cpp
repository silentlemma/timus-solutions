#include <cmath>
#include <cstdio>

typedef unsigned long long u64;

constexpr u64 BOUND = 1000000;  // the cube root of the largest C

u64 isqrt(u64 x) {
    u64 r = (u64)sqrtl((long double)x);
    while (r * r > x) r--;
    while ((r + 1) * (r + 1) <= x) r++;
    return r;
}

int main() {
    u64 c;
    scanf("%llu", &c);
    if (c == 0) {
        puts("1");  // only 0 + 0
        return 0;
    }
    // sqrt A + sqrt B = sqrt C exactly when C = s^2 q with q square-free and
    // A = a^2 q, B = b^2 q, a + b = s; so the answer counts the pairs a <= b
    u64 root = 1;
    for (u64 d = 2; d <= BOUND && d * d <= c; d++) {
        while (c % (d * d) == 0) c /= d * d, root *= d;
        if (c % d == 0) c /= d;
    }
    // what is left has only prime factors above the bound, at most two of them,
    // so it holds a square factor only when it is a square itself
    u64 r = isqrt(c);
    if (c > 1 && r * r == c) root *= r;
    printf("%llu\n", root / 2 + 1);
}
