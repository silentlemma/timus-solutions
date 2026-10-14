#include <cmath>
#include <cstdio>
#include <unordered_map>
using namespace std;

typedef unsigned long long ull;

ull mulmod(ull a, ull b, ull m) { return (unsigned __int128)a * b % m; }

ull power(ull b, ull e, ull m) {
    ull r = 1 % m;
    for (b %= m; e > 0; e >>= 1, b = mulmod(b, b, m))
        if (e & 1)
            r = mulmod(r, b, m);
    return r;
}

// the x in [0, q) with g^x = y modulo p, where g has order q:
// baby steps g^j for j < m, then giant steps y g^(-m i)
ull discreteLog(ull g, ull y, ull p, ull q) {
    ull m = (ull)sqrt((double)q) + 1;
    unordered_map<ull, ull> baby;
    baby.reserve(2 * m);
    ull cur = 1;
    for (ull j = 0; j < m; j++) {
        baby.emplace(cur, j);
        cur = mulmod(cur, g, p);
    }
    ull step = power(g, (q - m % q) % q, p); // g^(-m), since g^q = 1
    cur = y % p;
    for (ull i = 0; i <= m; i++) {
        auto it = baby.find(cur);
        if (it != baby.end())
            return (i * m + it->second) % q;
        cur = mulmod(cur, step, p);
    }
    return 0;
}

int main() {
    ull nBits, lBits, q, p, g, y, h;
    for (ull *field : {&nBits, &lBits, &q, &p, &g, &y, &h})
        if (scanf("%llu", field) != 1)
            return 0;
    // the hash is fixed, so the signature needs the secret key x itself
    ull x = discreteLog(g, y, p, q);
    for (ull k = 1;; k++) {
        ull r = power(g, k, p) % q;
        if (r == 0)
            continue;
        // q is prime, so k^(q-2) is the inverse of k
        ull s = mulmod(power(k, q - 2, q), (h + mulmod(x, r, q)) % q, q);
        if (s != 0) {
            printf("%llu %llu\n", r, s);
            return 0;
        }
    }
}
