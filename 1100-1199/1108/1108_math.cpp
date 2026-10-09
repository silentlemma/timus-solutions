#include <cstdint>
#include <cstdio>
#include <string>
#include <vector>

// a big number as base 10^9 digits, least significant first
typedef std::vector<uint64_t> Big;
const uint64_t BASE = 1000000000;
const size_t DIGITS = 9;

Big next_term(const Big &a) {
    Big less = a;
    less[0]--; // a is at least 2 and odd from the second term on
    Big res(a.size() * 2 + 1, 0);
    for (size_t i = 0; i < a.size(); i++) {
        uint64_t carry = 0;
        for (size_t j = 0; j < less.size() || carry; j++) {
            uint64_t cur = res[i + j] + carry + (j < less.size() ? a[i] * less[j] : 0);
            res[i + j] = cur % BASE;
            carry = cur / BASE;
        }
    }
    res[0]++; // the product is even, so its lowest digit is below BASE - 1
    while (res.size() > 1 && res.back() == 0)
        res.pop_back();
    return res;
}

std::string text(const Big &a) {
    std::string s = std::to_string(a.back());
    for (size_t i = a.size() - 1; i-- > 0;) {
        std::string digits = std::to_string(a[i]);
        s += std::string(DIGITS - digits.size(), '0') + digits;
    }
    return s;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    Big a = {2};
    std::string out;
    for (int i = 0; i < n; i++) {
        out += text(a) + "\n";
        // after the shares 1/a(1) .. 1/a(k) the remainder is 1/(a(k+1) - 1), and the
        // largest share that still leaves something is 1/a(k+1)
        a = next_term(a);
    }
    fputs(out.c_str(), stdout);
}
