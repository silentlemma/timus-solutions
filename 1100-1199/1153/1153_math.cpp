#include <iostream>
#include <string>
#include <vector>

// 8 S + 1 = (2 N + 1)^2 for S = N (N + 1) / 2
const int EIGHT = 8;
const int BASE = 10;
// the long-hand root takes the digits in pairs; each step multiplies the
// root so far by twice the base
const int PAIR = BASE * BASE, TWICE = 2 * BASE;

typedef std::vector<int> Big; // decimal digits, lowest first, no leading zeros

void trim(Big &a) {
    while (!a.empty() && a.back() == 0)
        a.pop_back();
}

Big mulSmall(const Big &a, int k) {
    Big r;
    int carry = 0;
    for (int d : a) {
        int v = d * k + carry;
        r.push_back(v % BASE);
        carry = v / BASE;
    }
    for (; carry; carry /= BASE)
        r.push_back(carry % BASE);
    trim(r);
    return r;
}

Big addSmall(Big a, int k) {
    for (size_t i = 0; k; i++) {
        if (i == a.size())
            a.push_back(0);
        int v = a[i] + k;
        a[i] = v % BASE;
        k = v / BASE;
    }
    return a;
}

int compare(const Big &a, const Big &b) {
    if (a.size() != b.size())
        return a.size() < b.size() ? -1 : 1;
    for (int i = (int)a.size() - 1; i >= 0; i--)
        if (a[i] != b[i])
            return a[i] < b[i] ? -1 : 1;
    return 0;
}

Big subtract(Big a, const Big &b) {
    int borrow = 0;
    for (size_t i = 0; i < a.size(); i++) {
        int v = a[i] - borrow - (i < b.size() ? b[i] : 0);
        borrow = v < 0;
        a[i] = v < 0 ? v + BASE : v;
    }
    trim(a);
    return a;
}

int main() {
    std::string text;
    if (!(std::cin >> text))
        return 0;
    Big total;
    for (int i = (int)text.size() - 1; i >= 0; i--)
        total.push_back(text[i] - '0');
    trim(total);
    Big d = addSmall(mulSmall(total, EIGHT), 1);
    std::string digits;
    for (int i = (int)d.size() - 1; i >= 0; i--)
        digits += char('0' + d[i]);
    if (digits.size() % 2)
        digits = "0" + digits;
    // the long-hand square root: bring down two digits, then take the largest
    // x with (20 root + x) x not above the remainder
    Big root, rest;
    for (size_t i = 0; i < digits.size(); i += 2) {
        rest = addSmall(mulSmall(rest, PAIR), (digits[i] - '0') * BASE + digits[i + 1] - '0');
        Big twice = mulSmall(root, TWICE), take;
        int x = BASE - 1;
        for (; x > 0; x--) {
            take = mulSmall(addSmall(twice, x), x);
            if (compare(take, rest) <= 0)
                break;
        }
        if (x > 0)
            rest = subtract(rest, take);
        root = addSmall(mulSmall(root, BASE), x);
    }
    // N = (root - 1) / 2, halved digit by digit from the top
    root = subtract(root, Big{1});
    std::string out;
    int carry = 0;
    for (int i = (int)root.size() - 1; i >= 0; i--) {
        int v = carry * BASE + root[i];
        if (!out.empty() || v / 2)
            out += char('0' + v / 2);
        carry = v % 2;
    }
    std::cout << (out.empty() ? "0" : out) << "\n";
}
