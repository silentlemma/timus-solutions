#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <vector>

constexpr std::size_t LIMB_DIGITS = 9;

using Big = std::vector<std::uint32_t>;
const std::uint64_t BASE = 1000000000;

void trim(Big &a) {
    while (a.size() > 1 && a.back() == 0)
        a.pop_back();
}

Big multiply(const Big &a, const Big &b) {
    Big result(a.size() + b.size(), 0);
    for (std::size_t i = 0; i < a.size(); ++i) {
        std::uint64_t carry = 0;
        std::size_t j = 0;
        for (; j < b.size(); ++j) {
            // (BASE-1)^2 + two carries fits in an unsigned 64-bit integer.
            const std::uint64_t value = result[i + j] + carry + std::uint64_t(a[i]) * b[j];
            result[i + j] = static_cast<std::uint32_t>(value % BASE);
            carry = value / BASE;
        }
        while (carry) {
            const std::uint64_t value = result[i + j] + carry;
            result[i + j] = static_cast<std::uint32_t>(value % BASE);
            carry = value / BASE;
            ++j;
        }
    }
    trim(result);
    return result;
}

Big small_product(const Big &a, std::uint32_t factor) {
    Big result;
    result.reserve(a.size() + 1);
    std::uint64_t carry = 0;
    for (std::uint32_t limb : a) {
        const std::uint64_t value = std::uint64_t(limb) * factor + carry;
        result.push_back(static_cast<std::uint32_t>(value % BASE));
        carry = value / BASE;
    }
    if (carry)
        result.push_back(static_cast<std::uint32_t>(carry));
    trim(result);
    return result;
}

Big add(const Big &a, const Big &b) {
    Big result;
    result.reserve(std::max(a.size(), b.size()) + 1);
    std::uint64_t carry = 0;
    for (std::size_t i = 0; i < std::max(a.size(), b.size()); ++i) {
        std::uint64_t value = carry;
        if (i < a.size())
            value += a[i];
        if (i < b.size())
            value += b[i];
        result.push_back(static_cast<std::uint32_t>(value % BASE));
        carry = value / BASE;
    }
    if (carry)
        result.push_back(static_cast<std::uint32_t>(carry));
    return result;
}

Big power_shift(const Big &a, std::size_t digits) {
    if (a.size() == 1 && a[0] == 0)
        return Big{0};
    std::uint32_t factor = 1;
    for (std::size_t i = 0; i < digits % LIMB_DIGITS; ++i)
        factor *= 10;
    Big value = small_product(a, factor);
    Big result(digits / LIMB_DIGITS, 0);
    result.insert(result.end(), value.begin(), value.end());
    return result;
}

bool at_least(const Big &a, const Big &b) {
    if (a.size() != b.size())
        return a.size() > b.size();
    for (std::size_t i = a.size(); i-- > 0;)
        if (a[i] != b[i])
            return a[i] > b[i];
    return true;
}

struct Decimal {
    Big value;
    std::size_t scale;
};

Decimal read_decimal() {
    int c = getchar();
    while (c != EOF && c <= ' ')
        c = getchar();
    if (c == '+')
        c = getchar();
    std::vector<unsigned char> digits;
    bool fraction = false;
    long long places = 0;
    while (c != EOF && c > ' ' && c != 'e' && c != 'E') {
        if (c == '.')
            fraction = true;
        else {
            digits.push_back(static_cast<unsigned char>(c - '0'));
            if (fraction)
                ++places;
        }
        c = getchar();
    }
    long long exponent = 0;
    if (c == 'e' || c == 'E') {
        c = getchar();
        const bool negative = c == '-';
        if (negative || c == '+')
            c = getchar();
        while (c >= '0' && c <= '9') {
            exponent = exponent * 10 + c - '0';
            c = getchar();
        }
        if (negative)
            exponent = -exponent;
    }
    places -= exponent;
    std::size_t first = 0, end = digits.size();
    while (first + 1 < end && digits[first] == 0)
        ++first;
    // Normalize before allocating limbs, including padded scientific notation.
    while (end > first + 1 && digits[end - 1] == 0) {
        --end;
        --places;
    }
    Big value;
    value.reserve((end - first + LIMB_DIGITS - 1) / LIMB_DIGITS);
    while (end > first) {
        const std::size_t start = end - first > LIMB_DIGITS ? end - LIMB_DIGITS : first;
        std::uint32_t limb = 0;
        for (std::size_t i = start; i < end; ++i)
            limb = limb * 10 + digits[i];
        value.push_back(limb);
        end = start;
    }
    trim(value);
    if (places < 0) {
        value = power_shift(value, static_cast<std::size_t>(-places));
        places = 0;
    }
    return {value, static_cast<std::size_t>(places)};
}

int main() {
    const int OUTCOMES = 3, TOTAL = 1000, MAXIMUM_ODD = 100;
    Big numerator{1}, denominator{0};
    for (int i = 0; i < OUTCOMES; ++i) {
        const Decimal odd = read_decimal();
        denominator = add(multiply(denominator, odd.value), power_shift(numerator, odd.scale));
        numerator = multiply(numerator, odd.value);
    }
    const Big twice_payout = small_product(numerator, 2 * TOTAL);
    int low = 0, high = TOTAL * MAXIMUM_ODD / OUTCOMES + 1;
    while (low + 1 < high) {
        const int middle = (low + high) / 2;
        // Exact half-up rounding: P >= middle - 1/2, with no floating point.
        if (at_least(twice_payout, small_product(denominator, 2 * middle - 1)))
            low = middle;
        else
            high = middle;
    }
    printf("%d\n", low);
}
