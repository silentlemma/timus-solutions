#include <iostream>
#include <string>

typedef __int128 big;

const int DIGITS = 6; // the input has at most six digits after the point
const long long SCALE = 1000000;

// the number times 10^6 as an exact integer
long long scaled(std::string token) {
    long long sign = token[0] == '-' ? -1 : 1;
    if (token[0] == '-' || token[0] == '+')
        token = token.substr(1);
    size_t dot = token.find('.');
    std::string whole = token.substr(0, dot);
    std::string frac = dot == std::string::npos ? "" : token.substr(dot + 1);
    frac = (frac + std::string(DIGITS, '0')).substr(0, DIGITS);
    return sign * (std::stoll("0" + whole) * SCALE + std::stoll(frac));
}

int main() {
    auto next = [] {
        std::string s;
        std::cin >> s;
        return big(scaled(s));
    };
    big ex = next(), ey = next(), tx = next(), ty = next();
    big ax = next(), ay = next(), bx = next(), by = next();
    // mirror from A along s; the eye and the target relative to A
    big sx = bx - ax, sy = by - ay;
    ex -= ax, ey -= ay, tx -= ax, ty -= ay;
    // heights above the mirror line (times |s|), both on one side
    big he = sx * ey - sy * ex, ht = sx * ty - sy * tx;
    if ((he > 0) != (ht > 0)) {
        std::cout << "INVISIBLE\n";
        return 0;
    }
    // the ray to the target's image meets the line at the projections
    // weighted by the heights: u = (pe * ht + pt * he) / ((he + ht) |s|^2)
    big pe = sx * ex + sy * ey, pt = sx * tx + sy * ty;
    big num = pe * ht + pt * he, den = (he + ht) * (sx * sx + sy * sy);
    if (den < 0)
        num = -num, den = -den;
    std::cout << (num >= 0 && num <= den ? "VISIBLE" : "INVISIBLE") << "\n";
}
