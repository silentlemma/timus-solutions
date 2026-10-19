#include <cstdio>

constexpr int TARGET = 20;
constexpr long long BOUND = 2000000;  // trial divisors; beyond them at most two primes remain

int main() {
    long long n;
    scanf("%lld", &n);
    int count = 0;
    long long d = 2;
    for (; d <= BOUND && d * d <= n; d++)
        while (n % d == 0) n /= d, count++;
    if (n > 1) {
        if (d * d > n)
            count++;  // what is left is prime
        else
            // n >= BOUND^2 here, so the divided part is at most 10^18 / BOUND^2,
            // fewer than 18 factors, and the rest adds at most two
            count = -1;
    }
    puts(count == TARGET ? "Yes" : "No");
}
