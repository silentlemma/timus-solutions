#include <array>
#include <cstdint>
#include <cstdio>

namespace {
constexpr int FIRST_ODD_PRIME = 3;
constexpr int LIMIT = 1 << 16;
constexpr int MAX_FACTORS = 6;
std::array<std::uint8_t, LIMIT / 2> factors{};
std::array<std::uint16_t, LIMIT / 2> roots{};

std::uint32_t power(std::uint32_t base, int exponent, std::uint32_t modulus) {
    std::uint32_t result = 1;
    for (; exponent; exponent >>= 1) {
        if (exponent & 1) {
            result = result * base % modulus;
        }
        base = base * base % modulus;
    }
    return result;
}

int largest_root(int prime) {
    const int order = prime - 1;
    std::array<int, MAX_FACTORS> exponents{order / 2};
    int count = 1;
    int odd = order >> __builtin_ctz(static_cast<unsigned>(order));
    while (odd > 1) {
        const int stored = factors[odd / 2];
        const int divisor = stored ? stored : odd;
        exponents[count++] = order / divisor;
        do {
            odd /= divisor;
        } while (odd % divisor == 0);
    }
    for (int root = order; root > 1; --root) {
        int i = 0;
        while (i < count && power(root, exponents[i], prime) != 1) {
            ++i;
        }
        if (i == count) {
            return root;
        }
    }
    return 0;
}
} // namespace

int main() {
    int queries;
    if (std::scanf("%d", &queries) != 1) {
        return 0;
    }
    for (int p = FIRST_ODD_PRIME; p * p < LIMIT; p += 2) {
        if (factors[p / 2] == 0) {
            for (int i = p * p / 2; i < LIMIT / 2; i += p) {
                if (factors[i] == 0) {
                    factors[i] = p;
                }
            }
        }
    }
    while (queries-- > 0) {
        int prime;
        if (std::scanf("%d", &prime) != 1) {
            break;
        }
        auto &root = roots[prime / 2];
        if (!root) {
            root = largest_root(prime);
        }
        std::printf("%d\n", static_cast<int>(root));
    }
}
