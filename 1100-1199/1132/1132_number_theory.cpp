#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

// moduli are below this bound
const int LIMIT = 32768;
// room for two numbers, a space and a newline
const int LINE = 32;

long long power(long long b, long long e, long long p) {
    long long r = 1;
    for (b %= p; e > 0; e /= 2, b = b * b % p)
        if (e % 2)
            r = r * b % p;
    return r;
}

// Tonelli-Shanks for an odd prime p = q * 2^s + 1, a quadratic residue a and a
// non-residue z
long long sqrt_mod(long long a, long long p, long long z) {
    long long q = p - 1, s = 0;
    while (q % 2 == 0) {
        q /= 2;
        s++;
    }
    long long c = power(z, q, p), t = power(a, q, p), r = power(a, (q + 1) / 2, p);
    while (t != 1) {
        // the order of t is 2^i with i < s; b fixes the top bits
        long long i = 0, tt = t;
        while (tt != 1) {
            tt = tt * tt % p;
            i++;
        }
        long long b = power(c, 1LL << (s - i - 1), p);
        s = i;
        c = b * b % p;
        t = t * c % p;
        r = r * b % p;
    }
    return r;
}

int main() {
    int k;
    if (scanf("%d", &k) != 1)
        return 0;
    std::vector<int> non_residue(LIMIT, 0);
    std::string out;
    char buf[LINE];
    while (k--) {
        long long a, p;
        if (scanf("%lld %lld", &a, &p) != 2)
            break;
        a %= p;
        if (p == 2) {
            out += "1\n";
            continue;
        }
        long long half = (p - 1) / 2;
        if (power(a, half, p) != 1) {
            out += "No root\n";
            continue;
        }
        if (!non_residue[p]) {
            int z = 2;
            while (power(z, half, p) != p - 1)
                z++;
            non_residue[p] = z;
        }
        long long r = sqrt_mod(a, p, non_residue[p]);
        snprintf(buf, sizeof buf, "%lld %lld\n", std::min(r, p - r), std::max(r, p - r));
        out += buf;
    }
    fputs(out.c_str(), stdout);
}
