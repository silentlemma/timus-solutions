#include <algorithm>
#include <iostream>
#include <string>

// exponents beyond this either give zero or an answer longer than allowed
const int EXP_LIMIT = 1000;
const char *FAIL = "Not a floating point number";

bool is_digit(char c) { return c >= '0' && c <= '9'; }

std::string run(const std::string &s, size_t &pos) {
    size_t start = pos;
    while (pos < s.size() && is_digit(s[pos]))
        pos++;
    return s.substr(start, pos - start);
}

std::string convert(const std::string &s, int n) {
    size_t pos = 0;
    bool negative = false;
    if (pos < s.size() && (s[pos] == '+' || s[pos] == '-'))
        negative = s[pos++] == '-';
    std::string whole = run(s, pos), frac;
    if (pos < s.size() && s[pos] == '.') {
        frac = run(s, ++pos);
        if (frac.empty())
            return FAIL;
    } else if (whole.empty()) {
        return FAIL;
    }
    int exp = 0;
    if (pos < s.size() && (s[pos] == 'e' || s[pos] == 'E')) {
        int sign = 1;
        if (++pos < s.size() && (s[pos] == '+' || s[pos] == '-'))
            sign = s[pos++] == '-' ? -1 : 1;
        std::string power = run(s, pos);
        if (power.empty())
            return FAIL;
        for (char c : power)
            exp = std::min(exp * 10 + (c - '0'), EXP_LIMIT);
        exp *= sign;
    }
    if (pos != s.size())
        return FAIL;
    // the digits of the number with the decimal point after `point` of them
    std::string mantissa = whole + frac;
    int point = (int)whole.size() + exp;
    if (mantissa.find_first_not_of('0') == std::string::npos)
        point = 0;
    auto digit = [&](int i) { return i >= 0 && i < (int)mantissa.size() ? mantissa[i] : '0'; };
    std::string head, tail;
    for (int i = 0; i < point; i++)
        if (!head.empty() || digit(i) != '0')
            head += digit(i);
    if (head.empty())
        head = "0";
    for (int i = point; i < point + n; i++)
        tail += digit(i);
    std::string out = head + (n > 0 ? "." + tail : "");
    if (negative && (head + tail).find_first_not_of('0') != std::string::npos)
        out = "-" + out;
    return out;
}

int main() {
    std::string s, line;
    std::string out;
    while (std::getline(std::cin, s)) {
        if (!s.empty() && s.back() == '\r')
            s.pop_back();
        if (s == "#" || !std::getline(std::cin, line))
            break;
        out += convert(s, std::stoi(line)) + "\n";
    }
    std::cout << out;
}
