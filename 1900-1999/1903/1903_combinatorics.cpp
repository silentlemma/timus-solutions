#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int64_t MODULUS = 1000000007;

int64_t power(int64_t base, int64_t exponent) {
    int64_t result = 1;
    while (exponent > 0) {
        if (exponent & 1)
            result = result * base % MODULUS;
        base = base * base % MODULUS;
        exponent /= 2;
    }
    return result;
}

class Binomial {
    std::vector<int64_t> factorial, inverse;

  public:
    explicit Binomial(int maximum) : factorial(maximum + 1, 1), inverse(maximum + 1, 1) {
        for (int i = 1; i <= maximum; ++i)
            factorial[i] = factorial[i - 1] * i % MODULUS;
        inverse[maximum] = power(factorial[maximum], MODULUS - 2);
        for (int i = maximum; i > 0; --i)
            inverse[i - 1] = inverse[i] * i % MODULUS;
    }

    int64_t choose(int total, int take) const {
        if (take < 0 || take > total)
            return 0;
        return factorial[total] * inverse[take] % MODULUS * inverse[total - take] % MODULUS;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, selected;
    std::cin >> n >> selected;
    std::vector<int> classes(n);
    for (int &value : classes)
        std::cin >> value;
    int identified, position;
    std::cin >> identified >> position;
    const int pivot = classes[identified - 1];
    int lower = 0, greater = 0;
    for (int value : classes) {
        lower += value < pivot;
        greater += value > pivot;
    }
    const int others = n - 1;
    const Binomial combinations(others);
    auto bad = [&](int pool, int threshold) {
        int64_t result = 0;
        for (int count = threshold; count <= std::min(pool, selected - 1); ++count) {
            result += combinations.choose(pool, count) *
                      combinations.choose(others - pool, selected - 1 - count) % MODULUS;
            result %= MODULUS;
        }
        return result;
    };
    int64_t answer = combinations.choose(others, selected - 1);
    answer = (answer - bad(lower, position) + MODULUS) % MODULUS;
    answer = (answer - bad(greater, selected - position + 1) + MODULUS) % MODULUS;
    std::cout << answer << '\n';
}
