#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>

constexpr int MOD = 1000000007;

int count_sets(std::int64_t amount, std::int64_t base, int length) {
    if (amount < length) {
        return 0;
    }
    std::vector<int> digits;
    std::int64_t digit_sum = 0;
    while (amount > 0) {
        const std::int64_t digit = amount % base;
        digit_sum += digit;
        if (digit_sum > length) {
            return 0;
        }
        digits.push_back(static_cast<int>(digit));
        amount /= base;
    }
    if ((length - digit_sum) % (base - 1) != 0) {
        return 0;
    }
    const int budget = static_cast<int>((length - digit_sum) / (base - 1));
    if (budget == 0) {
        return 1;
    }
    const int radix = static_cast<int>(base);
    std::vector<std::vector<int>> dp(budget + 1);
    for (int used = 0; used <= budget; ++used) {
        dp[used].resize(used + 1);
    }
    dp[0][0] = 1;
    for (int position = static_cast<int>(digits.size()) - 1; position > 0; --position) {
        std::vector<std::vector<int>> next(budget + 1);
        for (int used = 0; used <= budget; ++used) {
            next[used].resize(used + 1);
        }
        for (int used = 0; used <= budget; ++used) {
            const auto &row = dp[used];
            const std::int64_t total = std::accumulate(row.begin(), row.end(), std::int64_t{0});
            if (total == 0) {
                continue;
            }
            int ways = static_cast<int>(total % MOD);
            const int limit = budget - used + 1;
            int stop = std::min(limit, digits[position] + 1);
            for (int split = 0; split < stop; ++split) {
                next[used + split][split] = ways;
            }
            // A split count x needs at least ceil((x - digit) / base) parent splits.
            for (int previous : row) {
                if (stop == limit) {
                    break;
                }
                ways -= previous;
                if (ways < 0) {
                    ways += MOD;
                }
                const int end = std::min(limit, stop + radix);
                for (int split = stop; split < end; ++split) {
                    next[used + split][split] = ways;
                }
                stop = end;
            }
        }
        dp.swap(next);
    }
    // The units cannot be split; their count is fixed by the final carry.
    return static_cast<int>(std::accumulate(dp[budget].begin(), dp[budget].end(), std::int64_t{0}) %
                            MOD);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int tests;
    std::cin >> tests;
    while (tests-- > 0) {
        std::int64_t amount, base;
        int length;
        std::cin >> amount >> base >> length;
        std::cout << count_sets(amount, base, length) << '\n';
    }
}
