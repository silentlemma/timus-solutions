#include <cmath>
#include <cstdint>
#include <cstdio>
#include <vector>

// a big number as base 10^9 digits, least significant first
typedef std::vector<uint64_t> Big;
const uint64_t BASE = 1000000000;

void mul_small(Big &a, uint64_t m) {
    uint64_t carry = 0;
    for (auto &d : a) {
        uint64_t cur = d * m + carry;
        d = cur % BASE;
        carry = cur / BASE;
    }
    for (; carry; carry /= BASE)
        a.push_back(carry % BASE);
}

// divides by m and returns the remainder
uint64_t div_small(Big &a, uint64_t m) {
    uint64_t rest = 0;
    for (size_t i = a.size(); i-- > 0;) {
        uint64_t cur = rest * BASE + a[i];
        a[i] = cur / m;
        rest = cur % m;
    }
    while (a.size() > 1 && a.back() == 0)
        a.pop_back();
    return rest;
}

void add(Big &a, const Big &b) {
    if (a.size() < b.size())
        a.resize(b.size(), 0);
    uint64_t carry = 0;
    for (size_t i = 0; i < a.size(); i++) {
        uint64_t cur = a[i] + (i < b.size() ? b[i] : 0) + carry;
        a[i] = cur % BASE;
        carry = cur / BASE;
    }
    if (carry)
        a.push_back(carry);
}

int cmp(const Big &a, const Big &b) {
    if (a.size() != b.size())
        return a.size() < b.size() ? -1 : 1;
    for (size_t i = a.size(); i-- > 0;)
        if (a[i] != b[i])
            return a[i] < b[i] ? -1 : 1;
    return 0;
}

uint64_t gcd(uint64_t a, uint64_t b) { return b ? gcd(b, a % b) : a; }

int main() {
    long long n, m;
    if (scanf("%lld %lld", &n, &m) != 2)
        return 0;
    // from the target backwards: the last m km take one load; before it, a
    // stretch of m / (2k - 1) km is crossed 2k - 1 times to bring k loads
    double stretch = 0;
    long long k = 1;
    while (stretch + (double)m / (2 * k - 1) < n) {
        stretch += (double)m / (2 * k - 1);
        k++;
    }
    // fuel = (k-1) m + (2k-1) n - sum over i < k of m (2k-1) / (2i-1); its
    // fractional sum f = sum r_i / (2i-1) is kept exactly as num / den
    long long whole = (k - 1) * m + (2 * k - 1) * n;
    Big num = {0}, den = {1};
    double approx = 0;
    for (long long i = 1; i < k; i++) {
        uint64_t d = 2 * i - 1, r = m * (2 * k - 1) % d;
        whole -= m * (2 * k - 1) / d;
        if (r == 0)
            continue;
        approx += (double)r / d;
        Big copy = den;
        uint64_t g = gcd(d, div_small(copy, d));
        // num/den + r/d over the denominator den * (d / g)
        Big part = den;
        div_small(part, g);
        mul_small(part, r);
        mul_small(num, d / g);
        add(num, part);
        mul_small(den, d / g);
    }
    // floor(f) from its approximation, then corrected exactly
    long long t = (long long)std::floor(approx);
    auto times = [&](long long v) {
        Big b = den;
        mul_small(b, v);
        return b;
    };
    while (t > 0 && cmp(times(t), num) > 0)
        t--;
    while (cmp(times(t + 1), num) <= 0)
        t++;
    printf("%lld\n", whole - t);
}
