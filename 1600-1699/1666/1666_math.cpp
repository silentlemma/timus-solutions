#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

typedef long long ll;
typedef std::vector<ll> Poly;
const int QUARTIC = 5;  // coefficients of a degree-4 polynomial
const ll DISCRIMINANT = 4;  // t^2 - at + e has discriminant a^2 - 4e

// the positive and negative divisors of v != 0
std::vector<ll> divisors(ll v) {
    v = llabs(v);
    std::vector<ll> out;
    for (ll d = 1; d * d <= v; d++) {
        if (v % d == 0) {
            out.insert(out.end(), {d, -d, v / d, -(v / d)});
        }
    }
    return out;
}

ll value(const Poly& poly, ll x) {
    ll result = 0;
    for (ll c : poly) {
        result = result * x + c;
    }
    return result;
}

// an integer root of a monic polynomial: it divides the constant term
bool root(const Poly& poly, ll& r) {
    if (poly.back() == 0) {
        r = 0;
        return true;
    }
    for (ll d : divisors(poly.back())) {
        if (value(poly, d) == 0) {
            r = d;
            return true;
        }
    }
    return false;
}

ll exactRoot(ll v) {
    ll s = (ll)sqrtl((long double)v);
    while (s * s > v) {
        s--;
    }
    while ((s + 1) * (s + 1) <= v) {
        s++;
    }
    return s;
}

// (x^2 + px + q)(x^2 + rx + s) with qs = d, p + r = a, q + s + pr = b,
// ps + qr = c
bool quadratics(const Poly& poly, Poly& first, Poly& second) {
    ll a = poly[1], b = poly[2], c = poly[QUARTIC - 2], d = poly[QUARTIC - 1];
    for (ll q : divisors(d)) {
        ll s = d / q, p;
        if (q != s) {
            if ((c - a * q) % (s - q) != 0) {
                continue;
            }
            p = (c - a * q) / (s - q);
        } else {
            // then p and r are the roots of t^2 - at + (b - 2q)
            ll disc = a * a - DISCRIMINANT * (b - 2 * q);
            if (disc < 0) {
                continue;
            }
            ll root = exactRoot(disc);
            if (root * root != disc || (a + root) % 2 != 0) {
                continue;
            }
            p = (a + root) / 2;
        }
        ll r = a - p;
        if (q + s + p * r == b && p * s + q * r == c) {
            first = {1, p, q};
            second = {1, r, s};
            return true;
        }
    }
    return false;
}

std::string show(const Poly& poly) {
    int deg = poly.size() - 1;
    std::string out;
    for (int i = 0; i <= deg; i++) {
        ll c = poly[i];
        if (c == 0) {
            continue;
        }
        int power = deg - i;
        out += c < 0 ? "-" : (out.empty() ? "" : "+");
        if (llabs(c) != 1 || power == 0) {
            out += std::to_string(llabs(c));
        }
        if (power > 0) {
            out += "x";
        }
        if (power > 1) {
            out += std::to_string(power);
        }
    }
    return "(" + out + ")";
}

int main() {
    Poly poly(QUARTIC, 1);
    for (int i = 1; i < QUARTIC; i++) {
        scanf("%lld", &poly[i]);
    }
    std::vector<Poly> factors;
    ll r;
    while (poly.size() > 2 && root(poly, r)) {
        factors.push_back({1, -r});
        Poly quotient = {1};
        for (size_t i = 1; i + 1 < poly.size(); i++) {
            quotient.push_back(poly[i] + r * quotient.back());
        }
        poly = quotient;
    }
    if ((int)poly.size() == QUARTIC) {
        Poly first, second;
        if (!quadratics(poly, first, second)) {
            printf("Irreducible\n");
            return 0;
        }
        factors.push_back(first);
        factors.push_back(second);
    } else if (poly.size() > 1) {
        factors.push_back(poly);
    }
    std::string out;
    for (const Poly& f : factors) {
        out += show(f);
    }
    printf("%s\n", out.c_str());
}
