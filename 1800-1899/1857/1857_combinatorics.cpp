#include <cstdio>
#include <vector>

// a non-negative number in base 10^9, least significant limb first
using Big = std::vector<long long>;
const long long BASE = 1000000000;

static void multiply(Big &x, long long k) {
    long long carry = 0;
    for (auto &limb : x) {
        long long v = limb * k + carry;
        limb = v % BASE;
        carry = v / BASE;
    }
    for (; carry; carry /= BASE) x.push_back(carry % BASE);
}

static void add(Big &x, const Big &y) {
    if (x.size() < y.size()) x.resize(y.size(), 0);
    long long carry = 0;
    for (size_t i = 0; i < x.size(); i++) {
        long long v = x[i] + (i < y.size() ? y[i] : 0) + carry;
        x[i] = v % BASE;
        carry = v / BASE;
    }
    if (carry) x.push_back(carry);
}

// x - y for x >= y
static void subtract(Big &x, const Big &y) {
    long long borrow = 0;
    for (size_t i = 0; i < x.size(); i++) {
        long long v = x[i] - (i < y.size() ? y[i] : 0) - borrow;
        borrow = v < 0;
        x[i] = v + borrow * BASE;
    }
    while (x.size() > 1 && x.back() == 0) x.pop_back();
}

static void divide(Big &x, long long k) {
    long long rest = 0;
    for (size_t i = x.size(); i-- > 0;) {
        long long v = rest * BASE + x[i];
        x[i] = v / k;
        rest = v % k;
    }
    while (x.size() > 1 && x.back() == 0) x.pop_back();
}

int main() {
    int a, n;
    if (scanf("%d %d", &a, &n) != 2) return 0;
    std::vector<int> primes;
    int rest = n;
    for (int p = 2; p * p <= rest; p++) {
        if (rest % p == 0) {
            primes.push_back(p);
            while (rest % p == 0) rest /= p;
        }
    }
    if (rest > 1) primes.push_back(rest);
    // keys up to rotation without a shorter period are Lyndon words: by
    // Moebius inversion n times their number is the sum over square-free
    // divisors d of n of mu(d) a^(n / d)
    Big plus = {0}, minus = {0};
    for (int mask = 0; mask < 1 << primes.size(); mask++) {
        int d = 1;
        bool negative = false;
        for (size_t i = 0; i < primes.size(); i++) {
            if (mask >> i & 1) {
                d *= primes[i];
                negative = !negative;
            }
        }
        Big term = {1};
        for (int k = 0; k < n / d; k++) multiply(term, a);
        add(negative ? minus : plus, term);
    }
    subtract(plus, minus);
    divide(plus, n);
    printf("%lld", plus.back());
    for (size_t i = plus.size() - 1; i-- > 0;) printf("%09lld", plus[i]);
    printf("\n");
    return 0;
}
