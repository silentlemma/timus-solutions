#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

constexpr int SIEVE_LIMIT = 10000;
constexpr int LOWER_MODULUS = 5000;
constexpr int MODULUS_COUNT = 510;
using Complex = std::pair<std::int64_t, std::int64_t>;

std::vector<std::int64_t> primeModuli() {
    std::vector<bool> prime(SIEVE_LIMIT + 1, true);
    prime[0] = prime[1] = false;
    for (int value = 2; value * value <= SIEVE_LIMIT; ++value) {
        if (prime[value]) {
            for (int multiple = value * value; multiple <= SIEVE_LIMIT; multiple += value)
                prime[multiple] = false;
        }
    }
    std::vector<std::int64_t> result;
    for (int value = LOWER_MODULUS; value <= SIEVE_LIMIT; ++value) {
        if (prime[value])
            result.push_back(value);
        if (result.size() == MODULUS_COUNT)
            break;
    }
    return result;
}

const auto MODULI = primeModuli();

std::int64_t normalize(std::int64_t value, std::int64_t modulus) {
    const auto remainder = value % modulus;
    return remainder < 0 ? remainder + modulus : remainder;
}

Complex multiply(Complex first, Complex second, std::int64_t modulus) {
    return {normalize(first.first * second.first - first.second * second.second, modulus),
            normalize(first.first * second.second + first.second * second.first, modulus)};
}

Complex power(std::int64_t real, std::int64_t imaginary, int exponent, std::int64_t modulus) {
    Complex base{normalize(real, modulus), normalize(imaginary, modulus)}, result{1, 0};
    while (exponent > 0) {
        if (exponent & 1)
            result = multiply(result, base, modulus);
        base = multiply(base, base, modulus);
        exponent >>= 1;
    }
    return result;
}

int countRoots(std::int64_t a, std::int64_t b, int n, std::int64_t c, std::int64_t d, int m) {
    const int common = std::gcd(n, m);
    for (const auto modulus : MODULI) {
        if (power(a, b, m / common, modulus) != power(c, d, n / common, modulus))
            return 0;
    }
    return common;
}

int main() {
    std::int64_t a, b, c, d;
    int n, m;
    std::cin >> a >> b >> n >> c >> d >> m;
    std::cout << countRoots(a, b, n, c, d, m) << '\n';
    return 0;
}
