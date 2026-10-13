#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

// non-negative integers as 32-bit limbs, the lowest first, without leading zeros
typedef vector<uint32_t> Big;

const int LIMB = 32, BASE = 10, CHUNK_DIGITS = 9;
const uint32_t CHUNK = 1000000000;
const int DIGITS = 128;   // room for numbers up to 10^100
const uint64_t SPEED = 4; // bounces k come at 4 h sin(a) k (k + 1) down the slope

void trim(Big &a) {
    while (!a.empty() && a.back() == 0)
        a.pop_back();
}

Big parse(const char *s) {
    Big a;
    for (; *s; s++) {
        uint64_t carry = *s - '0';
        for (auto &x : a) {
            uint64_t v = (uint64_t)x * BASE + carry;
            x = (uint32_t)v;
            carry = v >> LIMB;
        }
        if (carry)
            a.push_back((uint32_t)carry);
    }
    return a;
}

Big mul(const Big &a, const Big &b) {
    Big r(a.size() + b.size(), 0);
    for (size_t i = 0; i < a.size(); i++) {
        uint64_t carry = 0;
        for (size_t j = 0; j < b.size(); j++) {
            uint64_t v = (uint64_t)a[i] * b[j] + r[i + j] + carry;
            r[i + j] = (uint32_t)v;
            carry = v >> LIMB;
        }
        r[i + b.size()] = (uint32_t)carry;
    }
    trim(r);
    return r;
}

Big add(const Big &a, const Big &b) {
    Big r(max(a.size(), b.size()) + 1, 0);
    uint64_t carry = 0;
    for (size_t i = 0; i + 1 < r.size(); i++) {
        uint64_t v = carry + (i < a.size() ? a[i] : 0) + (i < b.size() ? b[i] : 0);
        r[i] = (uint32_t)v;
        carry = v >> LIMB;
    }
    r.back() = (uint32_t)carry;
    trim(r);
    return r;
}

int compare(const Big &a, const Big &b) {
    if (a.size() != b.size())
        return a.size() < b.size() ? -1 : 1;
    for (size_t i = a.size(); i-- > 0;)
        if (a[i] != b[i])
            return a[i] < b[i] ? -1 : 1;
    return 0;
}

int bits(const Big &a) {
    if (a.empty())
        return 0;
    int top = 0;
    for (uint32_t x = a.back(); x; x >>= 1)
        top++;
    return (int)(a.size() - 1) * LIMB + top;
}

string text(Big a) {
    vector<uint32_t> chunks;
    while (!a.empty()) {
        uint64_t rem = 0;
        for (size_t i = a.size(); i-- > 0;) {
            uint64_t cur = (rem << LIMB) | a[i];
            a[i] = (uint32_t)(cur / CHUNK);
            rem = cur % CHUNK;
        }
        trim(a);
        chunks.push_back((uint32_t)rem);
    }
    string s = chunks.empty() ? "0" : to_string(chunks.back());
    for (size_t i = chunks.size() - 1; i-- > 0;) {
        string part = to_string(chunks[i]);
        s += string(CHUNK_DIGITS - part.size(), '0') + part;
    }
    return s;
}

int main() {
    int t;
    scanf("%d", &t);
    static char hs[DIGITS], ls[DIGITS];
    const Big one = {1};
    while (t--) {
        unsigned drop;
        scanf("%s %s %u", hs, ls, &drop);
        Big height = parse(hs), run = parse(ls);
        // the largest k with SPEED * drop * height * k (k + 1) <= run^2 + height^2,
        // set bit by bit from the highest one k can have
        Big x = add(mul(run, run), mul(height, height));
        Big y = mul(height, Big{(uint32_t)(SPEED * drop)});
        Big k;
        for (int b = max(0, (bits(x) - bits(y)) / 2 + 1); b >= 0; b--) {
            Big c = k;
            c.resize(max(c.size(), (size_t)(b / LIMB + 1)), 0);
            c[b / LIMB] |= 1u << (b % LIMB);
            if (compare(mul(mul(c, add(c, one)), y), x) <= 0)
                k = c;
        }
        printf("%s\n", text(add(k, one)).c_str());
    }
}
