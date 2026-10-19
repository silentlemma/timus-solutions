#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

constexpr int PERSISTENT_COUNT = 3;

std::string solve(const std::vector<int> &values) {
    int maximum = *std::max_element(values.begin(), values.end());
    int limit = 0;
    while ((limit + 1) * (limit + 1) <= maximum)
        ++limit;
    std::vector<bool> sieve(limit + 1, true);
    std::vector<int> primes;
    for (int prime = 2; prime <= limit; ++prime) {
        if (!sieve[prime])
            continue;
        primes.push_back(prime);
        for (int multiple = prime * prime; multiple <= limit; multiple += prime)
            sieve[multiple] = false;
    }
    std::unordered_map<int, int> counts;
    int best = 0;
    for (int value : values) {
        for (int prime : primes) {
            if (prime * prime > value)
                break;
            if (value % prime != 0)
                continue;
            int count = ++counts[prime];
            if (count == PERSISTENT_COUNT)
                return "infinity";
            best = std::max(best, count);
            while (value % prime == 0)
                value /= prime;
        }
        if (value > 1) {
            int count = ++counts[value];
            if (count == PERSISTENT_COUNT)
                return "infinity";
            best = std::max(best, count);
        }
    }
    return std::to_string(best);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int size;
    std::cin >> size;
    std::vector<int> values(size);
    for (int &value : values)
        std::cin >> value;
    std::cout << solve(values) << '\n';
}
