#include <cstdio>
#include <string>

// n is a product of two odd primes, so trial division starts here
const long long SMALLEST = 3;
// a query is e, n and c
const int FIELDS = 3;

long long power(long long b, long long e, long long n) {
    long long r = 1;
    for (b %= n; e > 0; e /= 2, b = b * b % n)
        if (e % 2)
            r = r * b % n;
    return r;
}

// the inverse of e modulo phi by the extended Euclidean algorithm
long long inverse(long long e, long long phi) {
    long long a = e % phi, b = phi, x = 1, y = 0;
    while (b) {
        long long q = a / b, t = a - q * b;
        a = b;
        b = t;
        t = x - q * y;
        x = y;
        y = t;
    }
    return (x % phi + phi) % phi;
}

int main() {
    int k;
    if (scanf("%d", &k) != 1)
        return 0;
    std::string out;
    while (k--) {
        long long e, n, c;
        if (scanf("%lld %lld %lld", &e, &n, &c) != FIELDS)
            break;
        long long p = SMALLEST;
        while (n % p)
            p += 2;
        long long phi = (p - 1) * (n / p - 1);
        // m^(e d) = m modulo n when e d = 1 modulo phi, so the private
        // exponent d undoes the public one
        out += std::to_string(power(c, inverse(e, phi), n)) + "\n";
    }
    fputs(out.c_str(), stdout);
}
