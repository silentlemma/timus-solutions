#include <cmath>
#include <cstdio>
#include <numeric>

long long isqrt(long long v) {
    long long r = (long long)std::sqrt((double)v);
    while (r * r > v) r--;
    while ((r + 1) * (r + 1) <= v) r++;
    return r;
}

int main() {
    long long r1, r2, n, i;
    if (scanf("%lld %lld %lld %lld", &r1, &r2, &n, &i) < 1) return 0;
    long long pos = i - 1;
    if (pos == 0) {
        printf("%lld/1\n", r1);
        return 0;
    }
    if (pos == 1LL << n) {
        printf("%lld/1\n", r2);
        return 0;
    }
    // between touching neighbours 1/sqrt(r) adds up, so circle pos has
    // 1/sqrt(r) = a/sqrt(r1) + b/sqrt(r2), with a and b from Stern's sequence
    // found as alpha f(x) + beta f(x + 1) while x is halved level by level
    long long alpha = 1, beta = 0, x = pos;
    for (int level = 0; level < n; level++) {
        if (x % 2 == 0) {
            alpha += beta;
        } else {
            beta += alpha;
        }
        x /= 2;
    }
    // with both a and b positive the radius is rational exactly when
    // r1 = g p^2 and r2 = g q^2 for g = gcd(r1, r2)
    long long g = std::gcd(r1, r2), p = isqrt(r1 / g), q = isqrt(r2 / g);
    if (p * p * g != r1 || q * q * g != r2) {
        puts("Irrational");
        return 0;
    }
    // r = 1 / ((a q + b p) / (p q sqrt(g)))^2
    long long num = g * p * p * q * q, d = alpha * q + beta * p, den = d * d;
    long long common = std::gcd(num, den);
    printf("%lld/%lld\n", num / common, den / common);
    return 0;
}
