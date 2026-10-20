#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using Integer = long long;
constexpr Integer MIN_SUM_FACTOR = 3;
constexpr Integer QUADRATIC_FACTOR = 4;
constexpr Integer AREA_MULTIPLE = 6;

int main() {
    Integer area;
    std::cin >> area;
    if (area % AREA_MULTIPLE != 0) {
        std::cout << 0 << '\n';
        return 0;
    }
    std::vector<Integer> divisors{1};
    Integer remaining = area;
    for (Integer prime = 2; prime * prime <= remaining; prime += prime == 2 ? 1 : 2) {
        int exponent = 0;
        while (remaining % prime == 0) {
            remaining /= prime;
            exponent += 2;
        }
        const auto size = divisors.size();
        Integer power = 1;
        for (int step = 0; step < exponent; ++step) {
            power *= prime;
            for (std::size_t i = 0; i < size; ++i) {
                divisors.push_back(divisors[i] * power);
            }
        }
    }
    if (remaining > 1) {
        const auto size = divisors.size();
        for (std::size_t i = 0; i < size; ++i) {
            divisors.push_back(divisors[i] * remaining);
            divisors.push_back(divisors[i] * remaining * remaining);
        }
    }
    std::sort(divisors.begin(), divisors.end());
    const Integer square = area * area;
    Integer answer = 0;
    // Heron's variables satisfy x <= y <= z and xyz(x + y + z) = area squared.
    for (std::size_t i = 0; i < divisors.size(); ++i) {
        const Integer x = divisors[i];
        if (x > square / x / x / x / MIN_SUM_FACTOR) {
            break;
        }
        remaining = square / x;
        std::size_t left = i, right = divisors.size();
        while (left < right) {
            const auto middle = (left + right) / 2;
            const Integer y = divisors[middle];
            if (y <= remaining / y / (x + 2 * y)) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        for (std::size_t j = i; j < left; ++j) {
            const Integer y = divisors[j];
            if (remaining % y != 0) {
                continue;
            }
            const Integer total = x + y;
            const Integer discriminant = total * total + QUADRATIC_FACTOR * (remaining / y);
            Integer root = static_cast<Integer>(std::sqrt(static_cast<double>(discriminant)));
            while (root * root > discriminant) {
                --root;
            }
            while ((root + 1) * (root + 1) <= discriminant) {
                ++root;
            }
            if (root * root == discriminant && (root - total) % 2 == 0) {
                ++answer;
            }
        }
    }
    std::cout << answer << '\n';
}
