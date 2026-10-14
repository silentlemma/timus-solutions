#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

const int TOTAL = 1000, MAX_ODD = 100, OUTCOMES = 3;
const int BASE = 1000000000, DIGITS = 9;
using Big = std::vector<int>;

void trim(Big &a) {
    while (a.size() > 1 && a.back() == 0)
        a.pop_back();
}

Big number(std::string text) {
    Big a;
    if (text[0] == '+') text.erase(0, 1);
    for (size_t end = text.size(); end > 0;) {
        size_t start = end > DIGITS ? end - DIGITS : 0;
        a.push_back(std::stoi(text.substr(start, end - start)));
        end = start;
    }
    trim(a);
    return a;
}

Big multiply(const Big &a, const Big &b) {
    Big c(a.size() + b.size(), 0);
    for (size_t i = 0; i < a.size(); i++) {
        long long carry = 0;
        for (size_t j = 0; j < b.size() || carry; j++) {
            long long value = c[i + j] + carry;
            if (j < b.size())
                value += 1LL * a[i] * b[j];
            c[i + j] = value % BASE;
            carry = value / BASE;
        }
    }
    trim(c);
    return c;
}

Big add(const Big &a, const Big &b) {
    Big c;
    int carry = 0;
    for (size_t i = 0; i < std::max(a.size(), b.size()) || carry; i++) {
        int value = carry;
        if (i < a.size()) value += a[i];
        if (i < b.size()) value += b[i];
        c.push_back(value % BASE);
        carry = value / BASE;
    }
    return c;
}

Big shift(Big a, size_t scale) {
    int factor = 1;
    for (size_t i = 0; i < scale % DIGITS; i++) factor *= 10;
    a = multiply(a, number(std::to_string(factor)));
    a.insert(a.begin(), scale / DIGITS, 0);
    return a;
}

bool at_least(const Big &a, const Big &b) {
    if (a.size() != b.size())
        return a.size() > b.size();
    return !std::lexicographical_compare(a.rbegin(), a.rend(), b.rbegin(), b.rend());
}

std::pair<Big, size_t> decimal(std::string token) {
    size_t exponent_at = token.find_first_of("eE");
    long long exponent = 0;
    if (exponent_at != std::string::npos) {
        exponent = std::stoll(token.substr(exponent_at + 1));
        token.resize(exponent_at);
    }
    size_t point = token.find('.');
    long long scale = point == std::string::npos ? 0 : token.size() - point - 1;
    if (point != std::string::npos)
        token.erase(point, 1);
    scale -= exponent;
    Big value = number(token);
    if (scale < 0) {
        value = shift(value, -scale);
        scale = 0;
    }
    return {value, static_cast<size_t>(scale)};
}

int main() {
    Big numerator = number("1"), denominator = number("0");
    for (int i = 0; i < OUTCOMES; i++) {
        std::string token;
        if (!(std::cin >> token))
            return 0;
        auto odd = decimal(token);
        denominator = add(multiply(denominator, odd.first), shift(numerator, odd.second));
        numerator = multiply(numerator, odd.first);
    }
    numerator = multiply(numerator, number(std::to_string(TOTAL)));
    // betting in proportion to 1 / k on every outcome pays the same whatever
    // happens, and any other split pays less on some outcome
    int low = 0, high = TOTAL * MAX_ODD / OUTCOMES + 1;
    while (low + 1 < high) {
        int middle = (low + high) / 2;
        if (at_least(multiply(numerator, number("2")),
                     multiply(denominator, number(std::to_string(2 * middle - 1)))))
            low = middle;
        else
            high = middle;
    }
    std::cout << low << '\n';
}
