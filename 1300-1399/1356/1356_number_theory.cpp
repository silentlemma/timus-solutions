#include <cstdio>
#include <vector>

typedef long long ll;

// these bases make Miller-Rabin exact for every n below 3.2 * 10^9
const ll BASES[] = {2, 3, 5, 7};
const ll SMALLEST_SPLIT = 4; // the smallest even number that is a sum of two primes

ll power(ll b, ll e, ll m) {
    ll r = 1;
    b %= m;
    for (; e > 0; e >>= 1) {
        if (e & 1)
            r = r * b % m;
        b = b * b % m;
    }
    return r;
}

bool isPrime(ll n) {
    if (n < 2)
        return false;
    for (ll b : BASES)
        if (n % b == 0)
            return n == b;
    ll d = n - 1;
    int s = 0;
    while (d % 2 == 0) {
        d /= 2;
        s++;
    }
    for (ll b : BASES) {
        ll x = power(b, d, n);
        if (x == 1 || x == n - 1)
            continue;
        bool composite = true;
        for (int i = 1; i < s && composite; i++) {
            x = x * x % n;
            composite = x != n - 1;
        }
        if (composite)
            return false;
    }
    return true;
}

// an even n >= 4 as the smallest prime p and n - p
std::vector<ll> twoPrimes(ll n) {
    ll p = 2;
    while (!(isPrime(p) && isPrime(n - p)))
        p++;
    return {p, n - p};
}

std::vector<ll> split(ll n) {
    if (isPrime(n))
        return {n};
    if (n % 2 == 0)
        return twoPrimes(n);
    if (isPrime(n - 2))
        return {2, n - 2};
    // the largest prime p that leaves an even rest of at least 4
    ll p = n - SMALLEST_SPLIT;
    while (!isPrime(p))
        p -= 2;
    std::vector<ll> parts = twoPrimes(n - p);
    parts.insert(parts.begin(), p);
    return parts;
}

int main() {
    int t = 0;
    if (scanf("%d", &t) != 1)
        return 0;
    for (int i = 0; i < t; i++) {
        ll n = 0;
        if (scanf("%lld", &n) != 1)
            return 0;
        std::vector<ll> parts = split(n);
        for (size_t j = 0; j < parts.size(); j++)
            printf(j ? " %lld" : "%lld", parts[j]);
        printf("\n");
    }
    return 0;
}
