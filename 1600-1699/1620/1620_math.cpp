#include <cstdint>
#include <cstdio>
#include <string>
#include <utility>
#include <vector>
using namespace std;

// Non-negative big numbers as base-10^9 digits, lowest first.
typedef vector<uint64_t> Big;
const uint64_t BASE = 1000000000;
const int DIGITS = 9; // decimal digits in a base-10^9 digit

void mulSmall(Big &a, uint64_t s) { // s <= 10^9
    uint64_t carry = 0;
    for (auto &d : a) {
        uint64_t cur = d * s + carry;
        d = cur % BASE;
        carry = cur / BASE;
    }
    while (carry) {
        a.push_back(carry % BASE);
        carry /= BASE;
    }
    while (a.size() > 1 && a.back() == 0)
        a.pop_back();
}

uint64_t divSmall(Big &a, uint64_t s) { // the quotient replaces a; returns the remainder
    uint64_t rem = 0;
    for (size_t i = a.size(); i-- > 0;) {
        uint64_t cur = rem * BASE + a[i];
        a[i] = cur / s;
        rem = cur % s;
    }
    while (a.size() > 1 && a.back() == 0)
        a.pop_back();
    return rem;
}

void addTo(Big &a, const Big &b) {
    uint64_t carry = 0;
    for (size_t i = 0; i < b.size() || carry; i++) {
        if (i == a.size())
            a.push_back(0);
        uint64_t cur = a[i] + carry + (i < b.size() ? b[i] : 0);
        a[i] = cur % BASE;
        carry = cur / BASE;
    }
}

void subFrom(Big &a, const Big &b) { // a >= b
    int64_t borrow = 0;
    for (size_t i = 0; i < a.size(); i++) {
        int64_t cur = (int64_t)a[i] - borrow - (i < b.size() ? (int64_t)b[i] : 0);
        borrow = cur < 0;
        a[i] = cur + (borrow ? BASE : 0);
    }
    while (a.size() > 1 && a.back() == 0)
        a.pop_back();
}

bool isZero(const Big &a) { return a.size() == 1 && a[0] == 0; }

string show(const Big &a) {
    string s = to_string(a.back());
    for (size_t i = a.size() - 1; i-- > 0;) {
        string part = to_string(a[i]);
        s += string(DIGITS - part.size(), '0') + part;
    }
    return s;
}

int main() {
    long long n, m, k;
    if (scanf("%lld %lld", &n, &m) != 2 || scanf("%lld", &k) != 1)
        return 0;
    // each flip moves the expectation to E (1 - 2/n) + 1, so after k flips
    // E = n/2 + (m - n/2) ((n - 2)/n)^k = (n^(k+1) + (2m - n)(n - 2)^k) / (2 n^k)
    Big num = {1};
    for (long long i = 0; i <= k; i++)
        mulSmall(num, n);
    long long first = 2 * m - n, ratio = n - 2;
    Big tail = {(uint64_t)llabs(first)};
    for (long long i = 0; i < k; i++)
        mulSmall(tail, llabs(ratio));
    bool negative = (first < 0) != (ratio < 0 && k % 2 == 1);
    if (negative)
        subFrom(num, tail); // the expectation is never negative
    else
        addTo(num, tail);
    if (isZero(num)) {
        printf("0/1\n");
        return 0;
    }
    // the denominator 2 n^k as primes and powers; only these can divide num
    vector<pair<uint64_t, long long>> den;
    long long rest = 2 * n;
    for (long long p = 2; p * p <= rest; p++)
        if (rest % p == 0) {
            long long e = 0;
            while (rest % p == 0)
                rest /= p, e++;
            den.push_back({p, e});
        }
    if (rest > 1)
        den.push_back({rest, 1});
    for (auto &[p, e] : den) {
        e = (e - (p == 2)) * k + (p == 2); // the exponent in 2 n^k
        while (e > 0) {
            Big q = num;
            if (divSmall(q, p) != 0)
                break;
            num = q;
            e--;
        }
    }
    Big rest_den = {1};
    for (auto &[p, e] : den)
        for (long long i = 0; i < e; i++)
            mulSmall(rest_den, p);
    printf("%s/%s\n", show(num).c_str(), show(rest_den).c_str());
}
