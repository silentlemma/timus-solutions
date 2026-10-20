#include <cstdint>
#include <iostream>
#include <vector>

constexpr std::int64_t kMod = 1'000'000'007;

struct Entry {
    int value;
    int size;
};

std::int64_t modularPower(std::int64_t base, std::int64_t exponent) {
    std::int64_t result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = result * base % kMod;
        }
        base = base * base % kMod;
        exponent /= 2;
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    if (!(std::cin >> n)) {
        return 0;
    }
    std::vector<Entry> stack;
    stack.reserve(n);
    std::int64_t factorial = 1;
    std::int64_t denominator = 1;

    for (int i = 1; i <= n; ++i) {
        int value;
        std::cin >> value;
        int size = 0;
        // Popped nodes now have complete Cartesian subtrees.
        while (!stack.empty() && stack.back().value > value) {
            size += stack.back().size;
            stack.pop_back();
            denominator = denominator * size % kMod;
        }
        stack.push_back({value, size + 1});
        factorial = factorial * i % kMod;
    }

    int size = 0;
    while (!stack.empty()) {
        size += stack.back().size;
        stack.pop_back();
        denominator = denominator * size % kMod;
    }

    // The tree hook-length formula counts the equivalent permutations.
    std::cout << factorial * modularPower(denominator, kMod - 2) % kMod << '\n';
    return 0;
}
