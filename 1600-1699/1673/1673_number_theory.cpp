#include <algorithm>
#include <cstdio>
#include <map>
#include <utility>
#include <vector>

typedef long long ll;
const ll WITNESSES[] = {2, 3, 5, 7};  // enough for a deterministic test below 3.2 * 10^9

ll power(ll base, ll exp, ll mod) {
    ll result = 1;
    for (base %= mod; exp > 0; exp >>= 1, base = base * base % mod) {
        if (exp & 1) {
            result = result * base % mod;
        }
    }
    return result;
}

// Miller-Rabin with fixed witnesses, exact for these sizes
bool isPrime(ll n) {
    if (n < 2) {
        return false;
    }
    for (ll p : WITNESSES) {
        if (n % p == 0) {
            return n == p;
        }
    }
    ll d = n - 1;
    int s = 0;
    while (d % 2 == 0) {
        d /= 2;
        s++;
    }
    for (ll a : WITNESSES) {
        ll x = power(a, d, n);
        if (x == 1 || x == n - 1) {
            continue;
        }
        bool composite = true;
        for (int i = 1; i < s && composite; i++) {
            x = x * x % n;
            composite = x != n - 1;
        }
        if (composite) {
            return false;
        }
    }
    return true;
}

std::vector<ll> primes;
std::map<std::pair<ll, int>, ll> memo;

// the smallest product of powers of primes[start..] whose totient is rest,
// or 0 if there is none
ll least(ll rest, int start) {
    if (rest == 1) {
        return 1;
    }
    auto key = std::make_pair(rest, start);
    auto it = memo.find(key);
    if (it != memo.end()) {
        return it->second;
    }
    ll best = 0;
    for (int i = start; i < (int)primes.size() && primes[i] - 1 <= rest; i++) {
        ll p = primes[i];
        if (rest % (p - 1) != 0) {
            continue;
        }
        ll part = rest / (p - 1), pw = p;
        while (true) {
            ll sub = least(part, i + 1);
            if (sub && (best == 0 || pw * sub < best)) {
                best = pw * sub;
            }
            if (part % p != 0) {
                break;
            }
            part /= p;
            pw *= p;
        }
    }
    memo[key] = best;
    return best;
}

int main() {
    ll k;
    scanf("%lld", &k);
    // student j is admitted exactly when gcd(j, N) = 1, so K = phi(N); every
    // p - 1 over the primes of N divides K, so the candidates are d + 1, d | K
    std::vector<ll> divs = {1};
    ll rest = k;
    for (ll p = 2; p * p <= rest; p++) {
        if (rest % p == 0) {
            size_t size = divs.size();
            ll pw = 1;
            while (rest % p == 0) {
                rest /= p;
                pw *= p;
                for (size_t i = 0; i < size; i++) {
                    divs.push_back(divs[i] * pw);
                }
            }
        }
    }
    if (rest > 1) {
        size_t size = divs.size();
        for (size_t i = 0; i < size; i++) {
            divs.push_back(divs[i] * rest);
        }
    }
    std::sort(divs.begin(), divs.end());
    for (ll d : divs) {
        if (isPrime(d + 1)) {
            primes.push_back(d + 1);
        }
    }
    printf("%lld\n", least(k, 0));
}
