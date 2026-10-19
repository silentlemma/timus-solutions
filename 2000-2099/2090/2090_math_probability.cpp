#include <cstdint>
#include <iostream>
#include <string>

constexpr int DECIMAL_PLACES = 12;
constexpr std::int64_t RADIX = 10;

std::string probability(std::int64_t numerator, std::int64_t denominator) {
    std::int64_t fraction = 0;
    std::int64_t scale = 1;
    for (int digit = 0; digit < DECIMAL_PLACES; ++digit) {
        numerator *= RADIX;
        fraction = fraction * RADIX + numerator / denominator;
        numerator %= denominator;
        scale *= RADIX;
    }
    if (2 * numerator >= denominator) {
        ++fraction;
    }

    std::string result = std::to_string(fraction / scale);
    fraction %= scale;
    if (fraction != 0) {
        std::string digits = std::to_string(fraction);
        digits.insert(0, DECIMAL_PLACES - digits.size(), '0');
        while (digits.back() == '0') {
            digits.pop_back();
        }
        result += "." + digits;
    }
    return result;
}

int main() {
    std::int64_t speed, distance, width_engels, width_marx;
    std::int64_t green_engels, yellow_engels, green_marx, yellow_marx;
    if (!(std::cin >> speed >> distance >> width_engels >> width_marx >> green_engels >>
          yellow_engels >> green_marx >> yellow_marx)) {
        return 0;
    }

    const std::int64_t period = speed * (green_engels + yellow_engels + green_marx + yellow_marx);
    // The other two phases give ties; crossing Marx shifts the winning intervals.
    const std::int64_t crosswalk = speed * (green_engels + yellow_marx) - width_marx;
    std::cout << probability(crosswalk, period) << ' ' << probability(width_marx, period) << '\n';
}
