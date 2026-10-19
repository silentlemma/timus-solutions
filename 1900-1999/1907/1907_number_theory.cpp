#include <cstdint>
#include <iostream>
#include <vector>

constexpr int64_t FIRST_ODD_PRIME = 3;

int64_t coprime_count(int64_t bound, size_t index, const std::vector<int64_t> &primes,
                      bool odd_only) {
    if (bound == 0)
        return 0;
    if (index == primes.size())
        return odd_only ? (bound + 1) / 2 : bound;
    return coprime_count(bound, index + 1, primes, odd_only) -
           coprime_count(bound / primes[index], index + 1, primes, odd_only);
}

int64_t count_sizes(int64_t first, int64_t limit) {
    int64_t odd_part = first;
    while (odd_part % 2 == 0)
        odd_part /= 2;
    std::vector<int64_t> primes;
    for (int64_t divisor = FIRST_ODD_PRIME; divisor * divisor <= odd_part; divisor += 2) {
        if (odd_part % divisor == 0) {
            primes.push_back(divisor);
            while (odd_part % divisor == 0)
                odd_part /= divisor;
        }
    }
    if (odd_part > 1)
        primes.push_back(odd_part);
    const bool odd_only = first % 2 == 0;
    const int64_t bad = coprime_count(odd_only ? limit : limit / 2, 0, primes, odd_only);
    return limit - bad;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t first, limit;
    std::cin >> first >> limit;
    std::cout << count_sizes(first, limit) << '\n';
}
