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

const long long SCALE = 20000000;

long long exact_floor(long long load, long long stage, long long lower) {
    Big num = {0}, den = {1};
    long long factor = load * (2 * stage - 1);
    for (long long i = 1; i < stage; i++) {
        uint64_t d = 2 * i - 1, r = factor % d;
        if (!r)
            continue;
        Big copy = den;
        uint64_t g = gcd(d, div_small(copy, d));
        Big part = den;
        div_small(part, g);
        mul_small(part, r);
        mul_small(num, d / g);
        add(num, part);
        mul_small(den, d / g);
    }
    // The enclosing interval has width below one, so only one correction exists.
    Big upper = den;
    mul_small(upper, lower + 1);
    return lower + (cmp(num, upper) >= 0);
}

long long line_ceiling(long long distance, long long load, long long stage) {
    long long factor = load * (2 * stage - 1),
              whole = (stage - 1) * load + (2 * stage - 1) * distance, lower = 0;
    for (long long i = 1; i < stage; i++) {
        long long d = 2 * i - 1;
        whole -= factor / d;
        lower += (factor % d) * SCALE / d;
    }
    long long floor = lower / SCALE;
    if (stage > 1 && (lower + stage - 2) / SCALE != floor)
        floor = exact_floor(load, stage, floor);
    return whole - floor;
}

int main() {
    long long distance, load;
    if (scanf("%lld%lld", &distance, &load) != 2)
        return 0;
    long long lower = 0, stage = 1;
    while (lower + load * SCALE / (2 * stage - 1) < distance * SCALE) {
        lower += load * SCALE / (2 * stage - 1);
        stage++;
    }
    // The true active affine line is this stage or its predecessor.
    long long answer = line_ceiling(distance, load, stage);
    if (stage > 1) {
        long long previous = line_ceiling(distance, load, stage - 1);
        if (previous > answer)
            answer = previous;
    }
    printf("%lld\n", answer);
}
