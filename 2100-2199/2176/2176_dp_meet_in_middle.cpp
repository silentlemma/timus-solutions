#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int TERNARY_BASE = 3;
constexpr int WORD_BITS = 64;
constexpr int MAX_DP_SUM = 50000000;

void collect_beautiful(int value, unsigned pattern, unsigned mask, int limit,
                       std::vector<int> &beautiful) {
    unsigned remaining = value;
    while (remaining >= pattern) {
        if ((remaining & mask) == pattern) {
            beautiful.push_back(value);
            break;
        }
        remaining >>= 1;
    }

    for (int digit = 0; digit < 2; ++digit) {
        std::int64_t child = static_cast<std::int64_t>(value) * TERNARY_BASE + digit;
        if (child <= limit) {
            collect_beautiful(static_cast<int>(child), (pattern << 1) | digit, (mask << 1) | 1,
                              limit, beautiful);
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    std::cin >> count;
    std::vector<int> queries(count);
    int limit = 0;
    for (int &value : queries) {
        std::cin >> value;
        limit = std::max(limit, value);
    }

    std::vector<int> beautiful;
    collect_beautiful(1, 1, 1, limit, beautiful);
    std::sort(beautiful.begin(), beautiful.end());

    int small_total = 0;
    std::size_t split = 0;
    while (split < beautiful.size() && small_total + beautiful[split] <= MAX_DP_SUM) {
        small_total += beautiful[split++];
    }

    std::vector<std::uint64_t> reachable(small_total / WORD_BITS + 1);
    reachable[0] = 1;
    int current_total = 0;
    for (std::size_t index = 0; index < split; ++index) {
        int value = beautiful[index];
        int whole = value / WORD_BITS;
        int part = value % WORD_BITS;
        current_total += value;
        // Descending updates use each beautiful number at most once.
        for (int target = current_total / WORD_BITS; target >= whole; --target) {
            int source = target - whole;
            std::uint64_t shifted = reachable[source] << part;
            if (part != 0 && source > 0) {
                shifted |= reachable[source - 1] >> (WORD_BITS - part);
            }
            reachable[target] |= shifted;
        }
    }

    std::vector<int> high_sums{0};
    for (std::size_t index = split; index < beautiful.size(); ++index) {
        std::size_t previous_size = high_sums.size();
        for (std::size_t subset = 0; subset < previous_size; ++subset) {
            high_sums.push_back(high_sums[subset] + beautiful[index]);
        }
    }
    std::sort(high_sums.begin(), high_sums.end());

    for (int value : queries) {
        bool found = false;
        for (int high_sum : high_sums) {
            int low_sum = value - high_sum;
            if (low_sum < 0) {
                break;
            }
            if (low_sum <= small_total &&
                ((reachable[low_sum / WORD_BITS] >> (low_sum % WORD_BITS)) & 1) != 0) {
                found = true;
                break;
            }
        }
        std::cout << (found ? "YES\n" : "NO\n");
    }
}
