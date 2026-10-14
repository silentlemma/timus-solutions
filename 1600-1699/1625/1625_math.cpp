#include <cstdint>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

// Non-negative big numbers as base-10^9 digits, lowest first.
typedef vector<uint64_t> Big;
const uint64_t BASE = 1000000000;
const int DIGITS = 9; // decimal digits in a base-10^9 digit

void mulSmall(Big &a, uint64_t s) {
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
}

void divSmall(Big &a, uint64_t s) { // exact division
    uint64_t rem = 0;
    for (size_t i = a.size(); i-- > 0;) {
        uint64_t cur = rem * BASE + a[i];
        a[i] = cur / s;
        rem = cur % s;
    }
    while (a.size() > 1 && a.back() == 0)
        a.pop_back();
}

string show(const Big &a) {
    string s = to_string(a.back());
    for (size_t i = a.size() - 1; i-- > 0;) {
        string part = to_string(a[i]);
        s += string(DIGITS - part.size(), '0') + part;
    }
    return s;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1)
        return 0;
    // The Catalan numbers: every leading square of their Hankel matrix has
    // determinant 1. C(k + 1) = C(k) * 2 (2k + 1) / (k + 2), always exact.
    Big c = {1};
    string out;
    for (int k = 0; k < 2 * n - 1; k++) {
        out += show(c) + "\n";
        mulSmall(c, 2 * (2 * k + 1));
        divSmall(c, k + 2);
    }
    fputs(out.c_str(), stdout);
}
