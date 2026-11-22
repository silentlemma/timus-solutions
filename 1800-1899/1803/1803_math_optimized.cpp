#include <algorithm>
#include <array>
#include <charconv>
#include <cstdint>
#include <cstdio>
#include <limits>
#include <numeric>
#include <type_traits>
#include <vector>

namespace {
constexpr int BINARY_RADIX = 2, TERNARY_RADIX = 3, QUATERNARY_RADIX = 4;
constexpr int QUINARY_RADIX = 5, SENARY_RADIX = 6, SEPTENARY_RADIX = 7;
constexpr int OCTAL_RADIX = 8, NONARY_RADIX = 9, DECIMAL_RADIX = 10;
constexpr int OCTAL_BITS = 3, HIGH_BIT_WEIGHT = 4;
constexpr int LIMB_LIMIT = 1000000;
constexpr int TABLE_LIMIT = 4096;
constexpr int LIMB_BITS = 60;
constexpr std::uint64_t BINARY_BASE = std::uint64_t{1} << LIMB_BITS;
constexpr int OUTPUT_BUFFER = 8192;
constexpr int INDEX_SPACE = 7;

template <typename Limb, typename DigitSum>
void fibonacci_costs(Limb base, DigitSum digit_sum, std::vector<int> &costs) {
    std::vector<Limb> previous{1}, current{1};
    for (std::size_t i = 2; i < costs.size(); ++i) {
        previous.resize(current.size(), 0);
        int cost = 0;
        Limb carry = 0;
        for (std::size_t j = 0; j < current.size(); ++j) {
            Limb value = previous[j] + current[j] + carry;
            // Both bases are below the unsigned sign bit, and value is less than twice base.
            // The subtraction's high bit therefore identifies a borrow exactly.
            using Unsigned = std::make_unsigned_t<Limb>;
            const Unsigned remainder = static_cast<Unsigned>(value) - static_cast<Unsigned>(base);
            const Unsigned borrow = remainder >> (std::numeric_limits<Unsigned>::digits - 1);
            carry = 1 - borrow;
            value = static_cast<Limb>(remainder + borrow * base);
            previous[j] = value;
            cost += digit_sum(value);
        }
        if (carry != 0) {
            previous.push_back(carry);
            ++cost;
        }
        previous.swap(current);
        costs[i] = cost;
    }
}

template <int Radix> constexpr int radix_power(int limit) {
    int value = 1;
    while (value <= limit / Radix)
        value *= Radix;
    return value;
}

template <int Radix> void ordinary_costs(std::vector<int> &costs) {
    constexpr int base = radix_power<Radix>(LIMB_LIMIT);
    constexpr int block = radix_power<Radix>(TABLE_LIMIT);
    static_assert(block * block >= base, "Two blocks cover every limb");
    std::array<std::uint8_t, block> sums{};
    for (int i = 1; i < block; ++i)
        sums[i] = sums[i / Radix] + i % Radix;
    fibonacci_costs(
        std::uint32_t{base},
        [&](std::uint32_t value) { return sums[value % block] + sums[value / block]; }, costs);
}

template <int Bits> constexpr std::uint64_t digit_mask() {
    std::uint64_t mask = 0;
    for (int i = 0; i < LIMB_BITS; i += Bits)
        mask |= std::uint64_t{1} << i;
    return mask;
}

template <int Bits> struct SoftwareSum {
    int operator()(std::uint64_t value) const {
        constexpr auto mask = digit_mask<Bits>();
        int result = __builtin_popcountll(value & mask);
        if constexpr (Bits >= 2)
            result += 2 * __builtin_popcountll((value >> 1) & mask);
        if constexpr (Bits >= 3)
            result += HIGH_BIT_WEIGHT * __builtin_popcountll((value >> 2) & mask);
        return result;
    }
};

#if defined(__x86_64__) || defined(__i386__)
template <int Bits> struct HardwareSum {
    __attribute__((target("popcnt"))) int operator()(std::uint64_t value) const {
        constexpr auto mask = digit_mask<Bits>();
        int result = __builtin_popcountll(value & mask);
        if constexpr (Bits >= 2)
            result += 2 * __builtin_popcountll((value >> 1) & mask);
        if constexpr (Bits >= 3)
            result += HIGH_BIT_WEIGHT * __builtin_popcountll((value >> 2) & mask);
        return result;
    }
};
#endif

template <int Bits> void binary_costs(std::vector<int> &costs) {
#if defined(__x86_64__) || defined(__i386__)
    if (__builtin_cpu_supports("popcnt")) {
        fibonacci_costs(BINARY_BASE, HardwareSum<Bits>{}, costs);
        return;
    }
#endif
    fibonacci_costs(BINARY_BASE, SoftwareSum<Bits>{}, costs);
}

} // namespace

int main() {
    int radix, count;
    if (std::scanf("%d%d", &radix, &count) != 2) {
        return 0;
    }
    std::vector<int> costs(count, 1);
    switch (radix) {
    case BINARY_RADIX:
        binary_costs<1>(costs);
        break;
    case TERNARY_RADIX:
        ordinary_costs<TERNARY_RADIX>(costs);
        break;
    case QUATERNARY_RADIX:
        binary_costs<2>(costs);
        break;
    case QUINARY_RADIX:
        ordinary_costs<QUINARY_RADIX>(costs);
        break;
    case SENARY_RADIX:
        ordinary_costs<SENARY_RADIX>(costs);
        break;
    case SEPTENARY_RADIX:
        ordinary_costs<SEPTENARY_RADIX>(costs);
        break;
    case OCTAL_RADIX:
        binary_costs<OCTAL_BITS>(costs);
        break;
    case NONARY_RADIX:
        ordinary_costs<NONARY_RADIX>(costs);
        break;
    case DECIMAL_RADIX:
        ordinary_costs<DECIMAL_RADIX>(costs);
        break;
    }
    std::vector<int> order(count);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(),
              [&](int a, int b) { return costs[a] == costs[b] ? a < b : costs[a] < costs[b]; });
    std::array<char, OUTPUT_BUFFER> buffer;
    char *cursor = buffer.data();
    char *const end = cursor + buffer.size();
    for (int i = 0; i < count; ++i) {
        if (end - cursor < INDEX_SPACE) {
            std::fwrite(buffer.data(), 1, cursor - buffer.data(), stdout);
            cursor = buffer.data();
        }
        cursor = std::to_chars(cursor, end, order[i] + 1).ptr;
        *cursor++ = i + 1 == count ? '\n' : ' ';
    }
    std::fwrite(buffer.data(), 1, cursor - buffer.data(), stdout);
    return 0;
}
