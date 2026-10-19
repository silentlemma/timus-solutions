#include <array>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

constexpr int kFactorLimit = 100;
constexpr int kLowFps = 10;
constexpr int kHighFps = 60;
using Counts = std::array<int, kFactorLimit + 1>;

struct FactorTable {
    std::vector<int> primes;
    std::array<std::vector<std::pair<int, int>>, kFactorLimit + 1> factors;
    FactorTable() {
        for (int value = 2; value <= kFactorLimit; ++value) {
            int remaining = value;
            for (int prime : primes) {
                int exponent = 0;
                while (remaining % prime == 0) {
                    remaining /= prime;
                    ++exponent;
                }
                if (exponent != 0)
                    factors[value].emplace_back(prime, exponent);
            }
            if (remaining > 1) {
                factors[value].emplace_back(remaining, 1);
                if (remaining == value)
                    primes.push_back(value);
            }
        }
    }
};

std::string classify(int width, int height, int power, const Counts &counts,
                     const std::vector<int> &primes) {
    int area = width * height, limit = power / (kLowFps * area);
    if (limit == 0)
        return "Slideshow";
    int product = 1;
    for (int prime : primes)
        for (int step = 0; step < counts[prime]; ++step) {
            if (product > limit / prime)
                return "Slideshow";
            product *= prime;
        }
    return product <= power / (kHighFps * area) ? "Perfect" : "So-so";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    FactorTable table;
    Counts counts{};
    std::unordered_map<std::string, int> options;
    int n;
    std::cin >> n;
    options.reserve(n);
    for (int i = 0; i < n; ++i) {
        std::string name;
        int value;
        std::cin >> name >> value;
        options.emplace(name, value);
        for (auto [prime, exponent] : table.factors[value])
            counts[prime] += exponent;
    }
    int width, height, power, changes;
    std::cin >> width >> height >> power >> changes;
    std::cout << classify(width, height, power, counts, table.primes) << '\n';
    for (int i = 0; i < changes; ++i) {
        std::string command;
        std::cin >> command;
        if (command == "Resolution") {
            std::cin >> width >> height;
        } else {
            std::string name;
            std::cin >> name;
            int change = command == "On" ? 1 : -1;
            for (auto [prime, exponent] : table.factors[options.at(name)])
                counts[prime] += change * exponent;
        }
        std::cout << classify(width, height, power, counts, table.primes) << '\n';
    }
}
