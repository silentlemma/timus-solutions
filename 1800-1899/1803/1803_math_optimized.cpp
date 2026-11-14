#include <algorithm>
#include <array>
#include <charconv>
#include <cstdint>
#include <cstdio>
#include <numeric>
#include <vector>

namespace {
constexpr int LIMB_LIMIT = 1000000;
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
            carry = value >= base;
            value -= carry * base;
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
} // namespace

int main() {
    int radix, count;
    if (std::scanf("%d%d", &radix, &count) != 2) {
        return 0;
    }
    std::vector<int> costs(count, 1);
    if ((radix & (radix - 1)) == 0) {
        const int bits = __builtin_ctz(static_cast<unsigned>(radix));
        std::uint64_t mask = 0;
        for (int i = 0; i < LIMB_BITS; i += bits) {
            mask |= std::uint64_t{1} << i;
        }
        const auto sum = [bits, mask](std::uint64_t value) {
            int result = __builtin_popcountll(value & mask);
            if (bits >= 2) {
                result += 2 * __builtin_popcountll((value >> 1) & mask);
            }
            if (bits >= 3) {
                result += 4 * __builtin_popcountll((value >> 2) & mask);
            }
            return result;
        };
        fibonacci_costs(BINARY_BASE, sum, costs);
    } else {
        int base = 1;
        while (base <= LIMB_LIMIT / radix) {
            base *= radix;
        }
        // A limb below one million has at most twenty digits, each at most nine.
        std::vector<std::uint8_t> digit_sum(base);
        for (int i = 1; i < base; ++i) {
            digit_sum[i] = digit_sum[i / radix] + i % radix;
        }
        fibonacci_costs(base, [&](int value) { return digit_sum[value]; }, costs);
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
}
