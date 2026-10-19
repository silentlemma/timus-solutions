#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

constexpr int LIMB_BITS = 32;  // magnitudes are kept in 32-bit limbs
constexpr int64_t BASE = 1LL << LIMB_BITS;
constexpr int SCALE = 4;  // N is the distance of Q from the vertex times 4 |A|^3

// a small signed big integer: values here reach about 10^164
struct Big {
    bool negative = false;
    vector<uint32_t> limbs;  // least significant first, no leading zeros

    Big() {}
    Big(int64_t v) {
        negative = v < 0;
        uint64_t m = negative ? -(uint64_t)v : v;
        for (; m; m >>= LIMB_BITS) limbs.push_back((uint32_t)m);
    }
    bool zero() const { return limbs.empty(); }
    void trim() {
        while (!limbs.empty() && limbs.back() == 0) limbs.pop_back();
        if (zero()) negative = false;
    }
};

int compareMagnitude(const Big& a, const Big& b) {
    if (a.limbs.size() != b.limbs.size()) return a.limbs.size() < b.limbs.size() ? -1 : 1;
    for (int i = (int)a.limbs.size() - 1; i >= 0; i--)
        if (a.limbs[i] != b.limbs[i]) return a.limbs[i] < b.limbs[i] ? -1 : 1;
    return 0;
}

Big addMagnitude(const Big& a, const Big& b) {
    Big r;
    uint64_t carry = 0;
    for (size_t i = 0; i < max(a.limbs.size(), b.limbs.size()) || carry; i++) {
        uint64_t s = carry;
        if (i < a.limbs.size()) s += a.limbs[i];
        if (i < b.limbs.size()) s += b.limbs[i];
        r.limbs.push_back((uint32_t)s);
        carry = s >> LIMB_BITS;
    }
    r.trim();
    return r;
}

Big subMagnitude(const Big& a, const Big& b) {  // |a| >= |b|
    Big r;
    int64_t borrow = 0;
    for (size_t i = 0; i < a.limbs.size(); i++) {
        int64_t s = (int64_t)a.limbs[i] - borrow - (i < b.limbs.size() ? b.limbs[i] : 0);
        borrow = s < 0;
        r.limbs.push_back((uint32_t)(s + borrow * BASE));
    }
    r.trim();
    return r;
}

Big operator-(Big a) {
    if (!a.zero()) a.negative = !a.negative;
    return a;
}

Big operator+(const Big& a, const Big& b) {
    if (a.negative == b.negative) {
        Big r = addMagnitude(a, b);
        r.negative = a.negative && !r.zero();
        return r;
    }
    bool aLarger = compareMagnitude(a, b) >= 0;
    Big r = aLarger ? subMagnitude(a, b) : subMagnitude(b, a);
    r.negative = (aLarger ? a.negative : b.negative) && !r.zero();
    return r;
}

Big operator-(const Big& a, const Big& b) { return a + (-b); }

Big operator*(const Big& a, const Big& b) {
    Big r;
    r.limbs.assign(a.limbs.size() + b.limbs.size(), 0);
    for (size_t i = 0; i < a.limbs.size(); i++) {
        uint64_t carry = 0;
        for (size_t j = 0; j < b.limbs.size() || carry; j++) {
            uint64_t cur = r.limbs[i + j] + carry;
            if (j < b.limbs.size()) cur += (uint64_t)a.limbs[i] * b.limbs[j];
            r.limbs[i + j] = (uint32_t)cur;
            carry = cur >> LIMB_BITS;
        }
    }
    r.negative = a.negative != b.negative;
    r.trim();
    return r;
}

bool operator<=(const Big& a, const Big& b) {
    if (a.negative != b.negative) return a.negative;
    int c = compareMagnitude(a, b);
    return a.negative ? c >= 0 : c <= 0;
}

Big parse(const string& s) {
    Big r;
    size_t i = s[0] == '-' ? 1 : 0;
    for (; i < s.size(); i++) r = r * Big(10) + Big(s[i] - '0');
    if (s[0] == '-') r = -r;
    return r;
}

Big cross(const Big& ux, const Big& uy, const Big& vx, const Big& vy) {
    return ux * vy - uy * vx;
}

string answer(const Big& a, const Big& b, const Big& c, const Big& d, const Big& e, const Big& f,
              const Big& px, const Big& py, const Big& r) {
    // the curve is C + B t + A t^2 with A = (a, d), B = (b, e), C = (c, f)
    Big wx = px - c, wy = py - f;  // P relative to C
    Big r2 = r * r;
    if (a.zero() && d.zero()) {
        if (b.zero() && e.zero())
            // a single point: every line through it is an axis, and Q runs over the
            // circle with diameter CP, from C itself to P
            return wx * wx + wy * wy <= r2 ? "YES" : "MAYBE";
        // a line: the line itself is an axis (Q lies on it), and so is every
        // perpendicular, with Q at the distance of P from the line
        Big dist = cross(wx, wy, b, e);
        return dist * dist <= r2 * (b * b + e * e) ? "YES" : "MAYBE";
    }
    // one axis along A; along it, P lies at N / (4 |A|^3) from the vertex
    Big a2 = a * a + d * d;
    Big ab = a * b + d * e;
    Big n = Big(SCALE) * a2 * (wx * a + wy * d) + ab * ab;
    Big k = cross(a, d, b, e);
    Big k2 = k * k;  // zero for a ray, otherwise the parabola width
    Big a6 = a2 * a2 * a2;
    bool inside;
    if (n <= Big(2) * k2)
        // the nearest point of the curve is its vertex (the end of a ray)
        inside = n * n <= Big(SCALE * SCALE) * r2 * a6;
    else
        // Q far enough inside: squared distance k2 (N - k2) / (4 |A|^6), zero on a ray
        inside = k2 * (n - k2) <= Big(SCALE) * r2 * a6;
    return inside ? "YES" : "NO";
}

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    string out;
    auto read = [] {
        string s;
        cin >> s;
        return parse(s);
    };
    while (t--) {
        // declarators are read in order
        Big a = read(), b = read(), c = read(), d = read(), e = read(), f = read();
        Big px = read(), py = read(), r = read();
        out += answer(a, b, c, d, e, f, px, py, r) + "\n";
    }
    cout << out;
}
