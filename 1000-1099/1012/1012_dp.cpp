#include <cstdint>
#include <cstdio>
#include <vector>

// Big numbers: base 10^9 digits, least significant first.
const uint32_t BASE = 1000000000;
using Big = std::vector<uint32_t>;

Big add(const Big &a, const Big &b) {
    Big r;
    uint64_t carry = 0;
    for (size_t i = 0; i < a.size() || i < b.size() || carry; i++) {
        uint64_t s = carry + (i < a.size() ? a[i] : 0) + (i < b.size() ? b[i] : 0);
        r.push_back(s % BASE);
        carry = s / BASE;
    }
    return r;
}

Big multiply(const Big &a, uint32_t m) {
    Big r;
    uint64_t carry = 0;
    for (size_t i = 0; i < a.size() || carry; i++) {
        uint64_t s = carry + (i < a.size() ? (uint64_t)a[i] * m : 0);
        r.push_back(s % BASE);
        carry = s / BASE;
    }
    return r;
}

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) != 2)
        return 1;
    // numbers of valid prefixes ending with a zero and with another digit,
    // where the first digit is not zero
    Big zero = {0}, other = {(uint32_t)(k - 1)};
    for (int i = 1; i < n; i++) {
        Big next = multiply(add(zero, other), k - 1);
        zero = other;
        other = next;
    }
    Big answer = add(zero, other);
    printf("%u", answer.back());
    for (size_t i = answer.size() - 1; i-- > 0;)
        printf("%09u", answer[i]);
    printf("\n");
}
