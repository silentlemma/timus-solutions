#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

const int DIGITS = 19;
// a digit of any input sits at a power of ten from -SHIFT up to TOP - SHIFT
const int SHIFT = 300, TOP = 450;
const int BASE = 10, HALF = 5;

// adds the decimal number in text, digit by digit, to the signed sums
void add(const std::string &text, std::vector<long long> &sum) {
    size_t e = text.find_first_of("eE");
    std::string mantissa = text.substr(0, e);
    int exp = e == std::string::npos ? 0 : std::stoi(text.substr(e + 1));
    int sign = 1;
    if (mantissa[0] == '-' || mantissa[0] == '+') {
        if (mantissa[0] == '-')
            sign = -1;
        mantissa = mantissa.substr(1);
    }
    size_t dot = mantissa.find('.');
    int whole = dot == std::string::npos ? mantissa.size() : dot;
    int place = whole - 1 + exp;
    for (char c : mantissa)
        if (c != '.')
            sum[SHIFT + place--] += sign * (c - '0');
}

// turns the sums into digits 0..9 and returns the carry out of the top
long long settle(std::vector<long long> &sum) {
    long long carry = 0;
    for (long long &d : sum) {
        carry += d;
        d = ((carry % BASE) + BASE) % BASE;
        carry = (carry - d) / BASE;
    }
    return carry;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> sum(TOP, 0);
    for (int i = 0; i < n; i++) {
        std::string word;
        std::cin >> word;
        add(word, sum);
    }
    std::string sign;
    if (settle(sum) < 0) {
        // a negative total: settle its opposite instead
        for (long long &d : sum)
            d = -d;
        sign = "-";
        settle(sum);
    }
    int top = TOP - 1;
    while (top >= 0 && sum[top] == 0)
        top--;
    if (top < 0) {
        printf("0.%se0\n", std::string(DIGITS - 1, '0').c_str());
        return 0;
    }
    // keep 19 significant digits, rounding half up on the next one
    std::vector<int> kept(DIGITS + 1, 0);
    for (int k = 0; k < DIGITS; k++)
        kept[k + 1] = top - k >= 0 ? sum[top - k] : 0;
    if (top - DIGITS >= 0 && sum[top - DIGITS] >= HALF) {
        int k = DIGITS;
        while (++kept[k] == BASE)
            kept[k--] = 0;
    }
    int exponent = top - SHIFT, first = 1;
    if (kept[0] == 1)
        exponent++, first = 0;
    std::string text;
    for (int k = first; k < first + DIGITS; k++)
        text += char('0' + kept[k]);
    printf("%s%c.%se%d\n", sign.c_str(), text[0], text.substr(1).c_str(), exponent);
}
