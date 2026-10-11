#include <cstdint>
#include <cstdio>
#include <vector>

const uint32_t BASE = 1000000000; // digits of a big number, lowest first
const int PERCENT = 100;

void multiply(std::vector<uint32_t> &a, uint32_t f) {
    uint64_t carry = 0;
    for (uint32_t &d : a) {
        uint64_t cur = (uint64_t)d * f + carry;
        d = cur % BASE;
        carry = cur / BASE;
    }
    if (carry)
        a.push_back(carry);
}

// whether a > b for numbers without leading zero digits
bool greater(const std::vector<uint32_t> &a, const std::vector<uint32_t> &b) {
    if (a.size() != b.size())
        return a.size() > b.size();
    for (int i = a.size() - 1; i >= 0; i--)
        if (a[i] != b[i])
            return a[i] > b[i];
    return false;
}

std::vector<uint32_t> number(long long v) {
    std::vector<uint32_t> a;
    for (; v > 0; v /= BASE)
        a.push_back(v % BASE);
    return a;
}

int main() {
    long long gold, limit;
    int fee;
    scanf("%lld %lld %d", &gold, &limit, &fee);
    // after k years the gold is gold * ((100 - fee) / 100)^k exactly, so
    // compare gold * (100 - fee)^k with limit * 100^k in whole numbers
    std::vector<uint32_t> left = number(gold), right = number(limit);
    int years = 0;
    while (greater(left, right)) {
        multiply(left, PERCENT - fee);
        multiply(right, PERCENT);
        years++;
    }
    printf("%d\n", years);
}
