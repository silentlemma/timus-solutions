#include <cstdio>
#include <numeric>
#include <vector>

using namespace std;

vector<long long> primesOf(long long n) {
    vector<long long> found;
    for (long long p = 2; p * p <= n; p++)
        if (n % p == 0) {
            found.push_back(p);
            while (n % p == 0)
                n /= p;
        }
    if (n > 1)
        found.push_back(n);
    return found;
}

long long power(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    for (; exp > 0; exp >>= 1) {
        if (exp & 1)
            result = result * base % mod;
        base = base * base % mod;
    }
    return result;
}

int main() {
    long long a, n;
    scanf("%lld %lld", &a, &n);
    if (gcd(a, n) != 1) { // the remainders keep a common factor with N and never reach 1
        puts("0");
        return 0;
    }
    // the order divides phi(N): strip prime factors while a power stays 1
    long long phi = n;
    for (long long p : primesOf(n))
        phi = phi / p * (p - 1);
    long long order = phi;
    for (long long p : primesOf(phi))
        while (order % p == 0 && power(a, order / p, n) == 1)
            order /= p;
    printf("%lld\n", order);
}
