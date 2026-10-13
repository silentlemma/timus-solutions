#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
const int STEPS = 200; // halvings of the search interval: far below the 1e-6 asked
const int QUARTIC = 4;

ld value(const vector<ld> &poly, ld x) {
    ld s = 0;
    for (ld c : poly)
        s = s * x + c;
    return s;
}

int sign(ld v) { return (v > 0) - (v < 0); }

// points where poly changes sign inside (lo, hi); between neighbouring sign
// changes of the derivative the polynomial is monotone
vector<ld> signRoots(const vector<ld> &poly, ld lo, ld hi) {
    if (poly.size() < 2)
        return {};
    vector<ld> deriv;
    int n = poly.size() - 1;
    for (int i = 0; i < n; i++)
        deriv.push_back(poly[i] * (n - i));
    vector<ld> cuts = {lo};
    for (ld c : signRoots(deriv, lo, hi))
        cuts.push_back(c);
    cuts.push_back(hi);
    vector<ld> found;
    for (size_t k = 0; k + 1 < cuts.size(); k++) {
        ld a = cuts[k], b = cuts[k + 1];
        int sa = sign(value(poly, a)), sb = sign(value(poly, b));
        if (sa == 0 || sb == 0 || sa == sb)
            continue;
        for (int it = 0; it < STEPS; it++) {
            ld mid = (a + b) / 2;
            if (sign(value(poly, mid)) == sa)
                a = mid;
            else
                b = mid;
        }
        found.push_back((a + b) / 2);
    }
    return found;
}

// finds a root p/q of poly
bool rationalRoot(const vector<ll> &poly, ll &p, ll &q) {
    ll lead = llabs(poly[0]), last = llabs(poly.back());
    for (q = 1; q <= lead; q++) {
        if (lead % q != 0)
            continue;
        for (ll pa = 1; pa <= last; pa++) {
            if (last % pa != 0)
                continue;
            for (ll candidate : {pa, -pa}) {
                // q^n f(p/q), exact in integers
                ll s = 0, qp = 1;
                for (ll c : poly) {
                    s = s * candidate + c * qp;
                    qp *= q;
                }
                if (s == 0) {
                    p = candidate;
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<ll> poly(n + 1); // the leading coefficient first
    for (ll &c : poly)
        scanf("%lld", &c);
    vector<ld> roots;
    // rational roots p/q, with p dividing the constant term and q the
    // leading one; dividing by (q x - p) keeps integer coefficients
    while (poly.size() > 1 && poly.back() == 0) {
        roots.push_back(0);
        poly.pop_back();
    }
    ll p, q;
    while (poly.size() > 1 && rationalRoot(poly, p, q)) {
        vector<ll> out = {poly[0] / q};
        for (size_t i = 1; i + 1 < poly.size(); i++)
            out.push_back((poly[i] + p * out.back()) / q);
        poly = out;
        roots.push_back((ld)p / q);
    }
    // what is left has no rational roots; a repeated irrational root would
    // need its quadratic twice, so only a0 (x^2 + b x + d)^2 can repeat
    if ((int)poly.size() == QUARTIC + 1) {
        ll a0 = poly[0], c3 = poly[1], c2 = poly[2], c1 = poly[QUARTIC - 1], c0 = poly[QUARTIC];
        ll u = QUARTIC * a0, e = u * c2 - c3 * c3; // then b = 2 c3 / u, d = 2 e / u^2
        if (2 * c3 * e == c1 * u * u && e * e == c0 * u * u * u) {
            ll w = c3 * c3 - 2 * e; // the roots are (-c3 +- sqrt(w)) / u
            if (w > 0)
                for (ld r : {(-c3 - sqrtl(w)) / u, (-c3 + sqrtl(w)) / u})
                    roots.insert(roots.end(), 2, r);
            poly = {1};
        }
    }
    vector<ld> rest(poly.begin(), poly.end());
    ld bound = 1;
    for (size_t i = 1; i < rest.size(); i++)
        bound = max(bound, 1 + fabsl(rest[i] / rest[0]));
    for (ld r : signRoots(rest, -bound, bound))
        roots.push_back(r);
    sort(roots.begin(), roots.end());
    for (ld r : roots)
        printf("%.10f\n", (double)r); // MinGW printf has no long double
}
