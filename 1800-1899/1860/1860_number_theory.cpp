#include <cstdio>
#include <vector>

const long long MOD = 1000000007;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    // F_n is the product of k^fib(n - k + 1) over k from 1 to n, with
    // fib(1) = fib(2) = 1; weight[k] = fib(n - k + 1) modulo MOD
    std::vector<long long> fib(n + 2, 0), weight(n + 1);
    fib[1] = 1;
    for (int i = 2; i <= n + 1; i++) fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
    for (int k = 1; k <= n; k++) weight[k] = fib[n - k + 1];
    std::vector<bool> composite(n + 1, false);
    // the exponent of a prime p sums the weights of the multiples of p, of
    // p^2, and so on; the divisors number the product of exponents plus 1
    long long answer = 1;
    for (long long p = 2; p <= n; p++) {
        if (composite[p]) continue;
        for (long long q = p * p; q <= n; q += p) composite[q] = true;
        long long exponent = 0;
        for (long long power = p; power <= n; power *= p) {
            for (long long k = power; k <= n; k += power) exponent += weight[k];
            exponent %= MOD;
        }
        answer = answer * ((exponent + 1) % MOD) % MOD;
    }
    printf("%lld\n", answer);
    return 0;
}
