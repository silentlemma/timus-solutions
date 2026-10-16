#include <cstdint>
#include <cstdio>
#include <vector>

// non-negative big numbers in base 10^9, least significant limb first
using Big = std::vector<uint32_t>;
const uint64_t BASE = 1000000000;

void trim(Big &x) {
    while (!x.empty() && x.back() == 0) x.pop_back();
}

// x += y * s
void addMul(Big &x, const Big &y, uint64_t s) {
    if (x.size() < y.size()) x.resize(y.size(), 0);
    uint64_t carry = 0;
    for (size_t i = 0; i < x.size(); i++) {
        uint64_t cur = x[i] + carry + (i < y.size() ? y[i] * s : 0);
        x[i] = cur % BASE;
        carry = cur / BASE;
    }
    while (carry) {
        x.push_back(carry % BASE);
        carry /= BASE;
    }
}

void mulSmall(Big &x, uint64_t m) {
    uint64_t carry = 0;
    for (auto &limb : x) {
        uint64_t cur = limb * m + carry;
        limb = cur % BASE;
        carry = cur / BASE;
    }
    while (carry) {
        x.push_back(carry % BASE);
        carry /= BASE;
    }
    trim(x);
}

uint64_t modSmall(const Big &x, uint64_t m) {
    uint64_t r = 0;
    for (size_t i = x.size(); i-- > 0;) r = (r * BASE + x[i]) % m;
    return r;
}

// x -= s for s not above x
void subSmall(Big &x, uint64_t s) {
    for (size_t i = 0; s; i++) {
        uint64_t take = s % BASE;
        s /= BASE;
        if (x[i] >= take) {
            x[i] -= take;
        } else {
            x[i] += BASE - take;
            s++;
        }
    }
    trim(x);
}

void divSmall(Big &x, uint64_t m) {
    uint64_t r = 0;
    for (size_t i = x.size(); i-- > 0;) {
        uint64_t cur = r * BASE + x[i];
        x[i] = cur / m;
        r = cur % m;
    }
    trim(x);
}

void print(const Big &x) {
    if (x.empty()) {
        puts("0");
        return;
    }
    printf("%u", x.back());
    for (size_t i = x.size() - 1; i-- > 0;) printf("%09u", x[i]);
    puts("");
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    std::vector<uint64_t> thrown(n);
    for (auto &a : thrown) scanf("%llu", (unsigned long long *)&a);
    // build the catch X digit by digit in base n. Adding s n^j to X keeps
    // the first j fishermen happy and adds s (n - 1)^j to what fisherman
    // j + 1 finds, which is s (-1)^j modulo n: that fixes s
    Big caught, found, powerN{1}, powerM{1};
    for (int j = 0; j < n; j++) {
        uint64_t a = thrown[j];
        uint64_t s = (a + n - modSmall(found, n)) % n;
        if (j % 2) s = (n - s) % n;
        addMul(caught, powerN, s);
        addMul(found, powerM, s);
        trim(caught);
        trim(found);
        // the fisherman throws a fishes away and leaves (n - 1)/n of the rest
        subSmall(found, a);
        divSmall(found, n);
        mulSmall(found, n - 1);
        mulSmall(powerN, n);
        mulSmall(powerM, n - 1);
    }
    // every catch of this residue modulo n^n works; at least one fish
    print(caught.empty() ? powerN : caught);
    return 0;
}
