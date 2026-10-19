#include <cstdio>
#include <cstdlib>

constexpr long long PERCENT = 100;

int main() {
    long long b, c, d, k, p;
    scanf("%lld %lld %lld %lld %lld", &b, &c, &d, &k, &p);
    // the usual insurance for the next k years; registering the accident costs
    // p percent of it on top, paying cash costs b on top
    long long usual = k * c + d * k * (k + 1) / 2;
    // both sides times 100, so everything stays in integers
    long long gap = usual * p - b * PERCENT;
    puts(gap > 0 ? "Cash" : "Insurance");
    long long cents = llabs(gap);
    printf("%lld.%02lld\n", cents / PERCENT, cents % PERCENT);
}
