#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>

constexpr int DIGITS = 10;
constexpr int MAX_HALF_LENGTH = 50;
constexpr int LIMBS = 6;
constexpr int MAX_REDUCED_SUM = MAX_HALF_LENGTH * (DIGITS - 1) / 2;
constexpr std::uint32_t BASE = 1000000000;
using Number = std::array<std::uint32_t, LIMBS>;

void add(Number &value, const Number &other) {
    std::uint32_t carry = 0;
    for (int i = 0; i < LIMBS; ++i) {
        std::uint32_t digit = value[i] + other[i] + carry;
        carry = digit >= BASE;
        value[i] = digit - carry * BASE;
    }
}

void subtract(Number &value, const Number &other) {
    std::uint32_t borrow = 0;
    for (int i = 0; i < LIMBS; ++i) {
        const std::uint32_t subtrahend = other[i] + borrow;
        borrow = value[i] < subtrahend;
        value[i] = value[i] + borrow * BASE - subtrahend;
    }
}

void print_square(const Number &number) {
    std::array<std::uint32_t, 2 * LIMBS> result{};
    for (int i = 0; i < LIMBS; ++i) {
        std::uint64_t carry = 0;
        for (int j = 0; j < LIMBS; ++j) {
            const auto current = result[i + j] + carry + std::uint64_t(number[i]) * number[j];
            result[i + j] = current % BASE;
            carry = current / BASE;
        }
        result[i + LIMBS] = carry;
    }
    int i = static_cast<int>(result.size()) - 1;
    while (i > 0 && result[i] == 0)
        --i;
    std::printf("%u", result[i]);
    while (i > 0)
        std::printf("%09u", result[--i]);
    std::puts("");
}

int main() {
    int length, sum;
    if (std::scanf("%d%d", &length, &sum) != 2)
        return 0;
    const int maximum = length * (DIGITS - 1);
    if (sum % 2 || sum / 2 > maximum) {
        std::puts("0");
        return 0;
    }
    // Complementing every digit exchanges sums t and 9*length-t.
    const int target = std::min(sum / 2, maximum - sum / 2);
    Number storage[2][MAX_REDUCED_SUM + 1]{};
    auto *current = storage[0];
    auto *next = storage[1];
    current[0][0] = 1;
    for (int digit = 0; digit < length; ++digit) {
        Number window{};
        for (int t = 0; t <= target; ++t) {
            add(window, current[t]);
            if (t >= DIGITS)
                subtract(window, current[t - DIGITS]);
            next[t] = window;
        }
        std::swap(current, next);
    }
    print_square(current[target]);
}
