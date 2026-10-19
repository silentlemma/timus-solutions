#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <utility>
#include <vector>

using namespace std;
typedef long long i64;
typedef pair<i64, i64> Elem;  // a t + b in F_p[t] / (t^2 - t - 1)

constexpr i64 SMALL = 50;  // small primes: walk the whole sequence
constexpr i64 FIVE = 5;
constexpr i64 QUAD = 4;  // the discriminant of a y^2 + b y + c is b^2 - 4 a c

i64 p;

i64 power(i64 b, i64 e) {
    i64 r = 1;
    for (b %= p; e; e >>= 1, b = b * b % p)
        if (e & 1) r = r * b % p;
    return r;
}

// a square root of a modulo the odd prime p, or -1 (Tonelli-Shanks)
i64 sqrtMod(i64 a) {
    a %= p;
    if (a == 0) return 0;
    if (power(a, (p - 1) / 2) != 1) return -1;
    i64 q = p - 1, s = 0;
    while (q % 2 == 0) q /= 2, s++;
    i64 z = 2;
    while (power(z, (p - 1) / 2) != p - 1) z++;
    i64 m = s, c = power(z, q), t = power(a, q), r = power(a, (q + 1) / 2);
    while (t != 1) {
        i64 i = 0, t2 = t;
        while (t2 != 1) t2 = t2 * t2 % p, i++;
        i64 b = power(c, 1LL << (m - i - 1));
        m = i, c = b * b % p, t = t * c % p, r = r * b % p;
    }
    return r;
}

// (a t + b)(c t + d) with t^2 = t + 1
Elem mul(Elem u, Elem v) {
    i64 ac = u.first * v.first % p;
    i64 cross = (u.first * v.second + u.second * v.first) % p;
    return {(ac + cross) % p, (ac + u.second * v.second) % p};
}

int main() {
    i64 x;
    scanf("%lld %lld", &p, &x);
    set<i64> found;
    if (p <= SMALL) {
        // the pairs (F(k), F(k + 1)) repeat with a period of at most 4p + 4
        i64 a = 0, b = 1;
        do {
            if (a == x) found.insert(b);
            i64 c = (a + b) % p;
            a = b, b = c;
        } while (a != 0 || b != 1);
    } else {
        // t^k = F(k) t + F(k - 1), and Cassini's identity
        // F(k + 1)^2 - F(k + 1) F(k) - F(k)^2 = (-1)^k limits y = F(k + 1)
        // to the roots of y^2 - x y - x^2 - s = 0, s = 1 or -1
        set<i64> candidates;
        i64 half = (p + 1) / 2;
        for (i64 s : {1, -1}) {
            i64 root = sqrtMod(((x * x + QUAD * (x * x + s)) % p + p) % p);
            if (root < 0) continue;
            candidates.insert((x + root) % p * half % p);
            candidates.insert((x - root + p) % p * half % p);
        }
        // a pair is a power of t when the discrete logarithm exists: baby steps
        // t^j, giant steps by t^-m; the period divides p - 1 or 2 (p + 1)
        i64 bound = p % FIVE == 1 || p % FIVE == FIVE - 1 ? p - 1 : 2 * (p + 1);
        i64 m = (i64)sqrt((double)bound) + 1;
        vector<Elem> baby;
        Elem e = {0, 1};
        for (i64 j = 0; j < m; j++) baby.push_back(e), e = mul(e, {1, 0});
        sort(baby.begin(), baby.end());
        Elem back = {0, 1}, inverse = {1, p - 1};  // t^-m = (t - 1)^m
        for (i64 k = m; k; k >>= 1, inverse = mul(inverse, inverse))
            if (k & 1) back = mul(back, inverse);
        for (i64 y : candidates) {
            e = {x, (y - x + p) % p};
            for (i64 i = 0; i <= m; i++, e = mul(e, back))
                if (binary_search(baby.begin(), baby.end(), e)) {
                    found.insert(y);
                    break;
                }
        }
    }
    printf("%d\n", (int)found.size());
    if (!found.empty()) {
        bool first = true;
        for (i64 y : found) printf(first ? "%lld" : " %lld", y), first = false;
        printf("\n");
    }
}
