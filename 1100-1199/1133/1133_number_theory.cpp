#include <cstdio>
#include <utility>

typedef unsigned long long u64;

// a prime above the 4e9 + 1 possible answers and below 2^32, so products fit
// in 64 bits; no Fibonacci number with index up to 2000 is divisible by it
const u64 P = 4294967291ULL;
// the input is i, F(i), j, F(j) and n
const int FIELDS = 5;

u64 reduce(long long v) { return (u64)((v % (long long)P + (long long)P) % (long long)P); }

u64 power(u64 b, u64 e) {
    u64 r = 1;
    for (; e > 0; e /= 2, b = b * b % P)
        if (e % 2)
            r = r * b % P;
    return r;
}

int main() {
    long long i, fi, j, fj, n;
    if (scanf("%lld %lld %lld %lld %lld", &i, &fi, &j, &fj, &n) != FIELDS)
        return 0;
    if (i > j) {
        std::swap(i, j);
        std::swap(fi, fj);
    }
    // F(j) = A F(i) + B F(i + 1), with A and B found by stepping coefficients
    u64 a = 1, b = 0, na = 0, nb = 1;
    for (long long k = i; k < j; k++) {
        u64 sa = (a + na) % P, sb = (b + nb) % P;
        a = na;
        b = nb;
        na = sa;
        nb = sb;
    }
    u64 cur = reduce(fi);
    u64 next = (reduce(fj) + P - a * cur % P) % P * power(b, P - 2) % P;
    for (long long k = i; k < n; k++) {
        u64 s = (cur + next) % P;
        cur = next;
        next = s;
    }
    for (long long k = i; k > n; k--) {
        u64 prev = (next + P - cur) % P;
        next = cur;
        cur = prev;
    }
    long long answer = cur > P / 2 ? (long long)cur - (long long)P : (long long)cur;
    printf("%lld\n", answer);
}
