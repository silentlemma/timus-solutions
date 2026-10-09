#include <cstdint>
#include <cstdio>
#include <vector>

// a non-negative number as base-10^9 limbs, the lowest limb first
typedef std::vector<uint32_t> Big;

const int DIGITS = 10;
const uint64_t BASE = 1000000000;

void add_to(Big &a, const Big &b) {
    if (a.size() < b.size())
        a.resize(b.size(), 0);
    uint64_t carry = 0;
    for (size_t i = 0; i < a.size(); i++) {
        uint64_t s = a[i] + carry + (i < b.size() ? b[i] : 0);
        a[i] = s % BASE;
        carry = s / BASE;
    }
    if (carry)
        a.push_back(carry);
}

Big multiply(const Big &a, const Big &b) {
    std::vector<uint64_t> acc(a.size() + b.size() + 1, 0);
    for (size_t i = 0; i < a.size(); i++)
        for (size_t j = 0; j < b.size(); j++) {
            acc[i + j] += (uint64_t)a[i] * b[j];
            acc[i + j + 1] += acc[i + j] / BASE;
            acc[i + j] %= BASE;
        }
    for (size_t i = 0; i + 1 < acc.size(); i++) {
        acc[i + 1] += acc[i] / BASE;
        acc[i] %= BASE;
    }
    Big r(acc.begin(), acc.end());
    while (r.size() > 1 && r.back() == 0)
        r.pop_back();
    return r;
}

void print(const Big &a) {
    printf("%u", a.back());
    for (size_t i = a.size() - 1; i-- > 0;)
        printf("%09u", a[i]);
    printf("\n");
}

int main() {
    int n, s;
    if (scanf("%d %d", &n, &s) != 2)
        return 0;
    int half = s / 2;
    if (s % 2 != 0 || half > (DIGITS - 1) * n) {
        printf("0\n");
        return 0;
    }
    // ways[t]: the number of strings of the digits seen so far with digit sum t
    std::vector<Big> ways(half + 1, Big{0});
    ways[0] = Big{1};
    for (int k = 0; k < n; k++) {
        std::vector<Big> next(half + 1, Big{0});
        for (int t = 0; t <= half; t++)
            for (int d = 0; d < DIGITS && d <= t; d++)
                add_to(next[t], ways[t - d]);
        ways.swap(next);
    }
    // the two halves are chosen independently
    print(multiply(ways[half], ways[half]));
}
