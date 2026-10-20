#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

constexpr int FIRST_ODD_PRIME = 3;

std::vector<std::uint16_t> smallest_factors(int limit) {
    std::vector<std::uint16_t> factors((limit + 1) / 2);
    for (int prime = FIRST_ODD_PRIME; prime <= limit / prime; prime += 2) {
        if (factors[prime / 2] != 0) {
            continue;
        }
        for (int value = prime * prime; value <= limit; value += 2 * prime) {
            if (factors[value / 2] == 0) {
                factors[value / 2] = static_cast<std::uint16_t>(prime);
            }
        }
    }
    return factors;
}

int largest_factor(int value, const std::vector<std::uint16_t> &factors) {
    if (value % 2 == 0) {
        value /= value & -value;
        if (value == 1) {
            return 2;
        }
    }
    while (factors[value / 2] != 0) {
        value /= factors[value / 2];
    }
    return value;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count;
    std::cin >> count;
    std::vector<std::pair<int, int>> queries(count);
    int limit = 1;
    for (auto &[a, b] : queries) {
        std::cin >> a >> b;
        limit = std::max({limit, a, b});
    }
    const auto factors = smallest_factors(limit);
    for (const auto &[a, b] : queries) {
        int common = std::gcd(a, b);
        if (common != 1 && a != b) {
            // Shared factors survive exactly when they are at least this threshold.
            const int threshold =
                std::max(largest_factor(a / common, factors), largest_factor(b / common, factors));
            if (threshold > 2) {
                common /= common & -common;
            }
            while (common > 1) {
                int prime = common % 2 == 0 ? 2 : factors[common / 2];
                if (prime == 0) {
                    prime = common;
                }
                if (prime >= threshold) {
                    break;
                }
                common /= prime;
            }
        }
        std::cout << common << '\n';
    }
}
