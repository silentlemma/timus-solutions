#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>

typedef long long ll;

// "-7 3/4", "-7/11" or "11" as a numerator and denominator
void parse(const std::string &line, ll &num, ll &den) {
    size_t minus = line.find('-');
    ll sign = minus != std::string::npos ? -1 : 1;
    std::istringstream words(minus != std::string::npos ? line.substr(minus + 1) : line);
    ll whole = 0, part = 0;
    den = 1;
    std::string token;
    while (words >> token) {
        size_t slash = token.find('/');
        if (slash != std::string::npos) {
            part = std::stoll(token.substr(0, slash));
            den = std::stoll(token.substr(slash + 1));
        } else {
            whole = std::stoll(token);
        }
    }
    num = sign * (whole * den + part);
}

int main() {
    std::string first, op, second;
    std::getline(std::cin, first);
    std::getline(std::cin, op);
    std::getline(std::cin, second);
    ll an, ad, bn, bd, num, den;
    parse(first, an, ad);
    parse(second, bn, bd);
    char c = '+';
    std::istringstream(op) >> c;
    if (c == '+')
        num = an * bd + bn * ad, den = ad * bd;
    else if (c == '-')
        num = an * bd - bn * ad, den = ad * bd;
    else if (c == '*')
        num = an * bn, den = ad * bd;
    else
        num = an * bd, den = ad * bn;
    if (den < 0)
        num = -num, den = -den;
    const char *sign = num < 0 ? "-" : "";
    num = std::llabs(num);
    ll g = std::gcd(num, den);
    num /= g, den /= g;
    ll whole = num / den, rest = num % den;
    if (rest == 0)
        printf("%s%lld\n", sign, whole);
    else if (whole == 0)
        printf("%s%lld/%lld\n", sign, rest, den);
    else
        printf("%s%lld %lld/%lld\n", sign, whole, rest, den);
}
