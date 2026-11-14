#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>

constexpr int dimensions = 3;
constexpr int decimal_base = 10;
constexpr int limb_digits = 9;
constexpr std::uint32_t limb_base = 1000000000;
constexpr std::size_t ratio_limbs = 3;
constexpr int output_precision = 3;

struct Integer {
    std::vector<std::uint32_t> digits;
    int sign = 0;

    void normalize(int direction) {
        while (!digits.empty() && digits.back() == 0) {
            digits.pop_back();
        }
        sign = digits.empty() ? 0 : direction;
    }
};

int compare_magnitudes(const Integer &a, const Integer &b) {
    if (a.digits.size() != b.digits.size()) {
        return a.digits.size() < b.digits.size() ? -1 : 1;
    }
    for (std::size_t i = a.digits.size(); i-- > 0;) {
        if (a.digits[i] != b.digits[i]) {
            return a.digits[i] < b.digits[i] ? -1 : 1;
        }
    }
    return 0;
}

Integer operator+(const Integer &a, const Integer &b) {
    if (a.sign == 0 || b.sign == 0) {
        return a.sign == 0 ? b : a;
    }
    Integer result;
    if (a.sign == b.sign) {
        const std::size_t length = std::max(a.digits.size(), b.digits.size());
        result.digits.resize(length + 1);
        std::uint32_t carry = 0;
        for (std::size_t i = 0; i < length; ++i) {
            const std::uint32_t left = i < a.digits.size() ? a.digits[i] : 0;
            const std::uint32_t right = i < b.digits.size() ? b.digits[i] : 0;
            const std::uint32_t sum = left + right + carry;
            result.digits[i] = sum % limb_base;
            carry = sum / limb_base;
        }
        result.digits[length] = carry;
        result.normalize(a.sign);
        return result;
    }
    const bool left_larger = compare_magnitudes(a, b) >= 0;
    const auto &high = left_larger ? a : b;
    const auto &low = left_larger ? b : a;
    result.digits.resize(high.digits.size());
    std::int64_t borrow = 0;
    for (std::size_t i = 0; i < high.digits.size(); ++i) {
        const std::int64_t right = i < low.digits.size() ? low.digits[i] : 0;
        const std::int64_t difference = std::int64_t(high.digits[i]) - right - borrow;
        borrow = difference < 0;
        result.digits[i] = difference + borrow * limb_base;
    }
    result.normalize(high.sign);
    return result;
}

Integer operator-(const Integer &a, Integer b) {
    b.sign = -b.sign;
    return a + b;
}

Integer operator*(const Integer &a, const Integer &b) {
    if (a.sign == 0 || b.sign == 0) {
        return {};
    }
    Integer result;
    result.digits.resize(a.digits.size() + b.digits.size());
    for (std::size_t i = 0; i < a.digits.size(); ++i) {
        std::uint64_t carry = 0;
        for (std::size_t j = 0; j < b.digits.size(); ++j) {
            const std::uint64_t sum =
                std::uint64_t(a.digits[i]) * b.digits[j] + result.digits[i + j] + carry;
            result.digits[i + j] = sum % limb_base;
            carry = sum / limb_base;
        }
        result.digits[i + b.digits.size()] = carry;
    }
    result.normalize(a.sign * b.sign);
    return result;
}

struct Decimal {
    std::string digits;
    int exponent;
    int sign;
};

Decimal parse(const std::string &token) {
    const int sign = token.front() == '-' ? -1 : 1;
    const std::size_t start = token.front() == '-' || token.front() == '+' ? 1 : 0;
    const std::size_t marker = token.find_first_of("eE");
    const std::size_t end = std::min(marker, token.size());
    int exponent = marker == std::string::npos ? 0 : std::stoi(token.substr(marker + 1));
    std::string digits;
    bool fractional = false;
    for (std::size_t i = start; i < end; ++i) {
        if (token[i] == '.') {
            fractional = true;
        } else {
            digits.push_back(token[i]);
            exponent -= fractional;
        }
    }
    const auto first = digits.find_first_not_of('0');
    if (first == std::string::npos) {
        return {{}, 0, 0};
    }
    const auto last = digits.find_last_not_of('0');
    exponent += static_cast<int>(digits.size() - last - 1);
    return {digits.substr(first, last - first + 1), exponent, sign};
}

Integer scale(Decimal number, int exponent) {
    if (number.sign == 0) {
        return {};
    }
    number.digits.append(number.exponent - exponent, '0');
    Integer result;
    for (std::size_t end = number.digits.size(); end > 0;) {
        const std::size_t first = end > limb_digits ? end - limb_digits : 0;
        std::uint32_t digit = 0;
        for (std::size_t i = first; i < end; ++i) {
            digit = decimal_base * digit + (number.digits[i] - '0');
        }
        result.digits.push_back(digit);
        end = first;
    }
    result.sign = number.sign;
    return result;
}

// Take the leading limbs of positive operands. The exact sign tests use all limbs.
long double ratio(const Integer &a, const Integer &b) {
    if (a.sign == 0) {
        return 0;
    }
    const auto leading = [](const Integer &value) {
        long double sum = 0;
        const std::size_t end = value.digits.size();
        const std::size_t first = end - std::min(end, ratio_limbs);
        for (std::size_t i = end; i-- > first;) {
            sum = sum * limb_base + value.digits[i];
        }
        return std::pair{sum, static_cast<long double>(first)};
    };
    const auto [left, left_power] = leading(a);
    const auto [right, right_power] = leading(b);
    return left / right * std::pow(static_cast<long double>(limb_base), left_power - right_power);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    std::string token;
    if (!(std::cin >> count >> token)) {
        return 0;
    }
    const Decimal distance = parse(token);
    int exponent = distance.exponent;
    std::vector<std::array<Decimal, 2 * dimensions>> input(count);
    for (auto &object : input) {
        for (auto &value : object) {
            std::cin >> token;
            value = parse(token);
            if (value.sign != 0) {
                exponent = std::min(exponent, value.exponent);
            }
        }
    }
    std::vector<std::array<Integer, 2 * dimensions>> objects(count);
    for (int i = 0; i < count; ++i) {
        for (int k = 0; k < 2 * dimensions; ++k) {
            objects[i][k] = scale(input[i][k], exponent);
        }
    }
    const Integer radius = scale(distance, exponent);
    const Integer limit = radius * radius;
    long double best = std::numeric_limits<long double>::infinity();
    int first = 0, second = 0;
    for (int i = 0; i < count; ++i) {
        for (int j = i + 1; j < count; ++j) {
            Integer gap = Integer{} - limit, projection, speed;
            for (int k = 0; k < dimensions; ++k) {
                const Integer p = objects[j][k] - objects[i][k];
                const Integer v = objects[j][k + dimensions] - objects[i][k + dimensions];
                gap = gap + p * p;
                projection = projection + p * v;
                speed = speed + v * v;
            }
            if (projection.sign >= 0) {
                continue;
            }
            const Integer projection_squared = projection * projection;
            const Integer discriminant = projection_squared - speed * gap;
            if (discriminant.sign >= 0) {
                const long double time = ratio(gap, projection) /
                                         (1 + std::sqrt(ratio(discriminant, projection_squared)));
                if (time < best) {
                    best = time;
                    first = i + 1;
                    second = j + 1;
                }
            }
        }
    }
    if (first == 0) {
        std::cout << "OK\n";
    } else {
        std::cout << "ALARM!\n"
                  << std::fixed << std::setprecision(output_precision) << best << ' ' << first
                  << ' ' << second << '\n';
    }
}
