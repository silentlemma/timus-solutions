#include <array>
#include <cstdint>
#include <cstdio>

namespace {
constexpr int FIRST_ODD_PRIME = 3;
constexpr int LIMIT = 1 << 16;
constexpr int MAX_FACTORS = 6;
std::array<std::uint8_t, LIMIT / 2> factors{};
std::array<std::uint16_t, LIMIT / 2> roots{};

struct Modulus {
    static constexpr int WORD_BITS = 32;
    std::uint32_t value;
    std::uint64_t reciprocal;

    explicit Modulus(std::uint32_t prime)
        : value(prime), reciprocal((std::uint64_t{1} << WORD_BITS) / prime) {}

    std::uint32_t multiply(std::uint32_t a, std::uint32_t b) const {
        const std::uint32_t product = a * b;
        const auto quotient = static_cast<std::uint32_t>((product * reciprocal) >> WORD_BITS);
        const std::uint32_t remainder = product - quotient * value;
        // a,b < prime < 2^16: product < 2^32 and the quotient is at most one low.
        return remainder >= value ? remainder - value : remainder;
    }
};

std::uint32_t power(std::uint32_t base, int exponent, const Modulus &modulus) {
    std::uint32_t result = 1;
    for (; exponent; exponent >>= 1) {
        if (exponent & 1) {
            result = modulus.multiply(result, base);
        }
        base = modulus.multiply(base, base);
    }
    return result;
}

int largest_root(int prime) {
    const int order = prime - 1;
    const Modulus modulus(prime);
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
        while (i < count && power(root, exponents[i], modulus) != 1) {
            ++i;
        }
        if (i == count) {
            return root;
        }
    }
    return 0;
}
} // namespace

constexpr int IO_SIZE = 16384;
constexpr int DECIMAL_DIGITS = 20;
class Input {
    char data[IO_SIZE];
    int position = 0, size = 0;

  public:
    int byte() {
        if (position == size) {
            size = std::fread(data, 1, sizeof data, stdin);
            position = 0;
            if (size == 0)
                return EOF;
        }
        return static_cast<unsigned char>(data[position++]);
    }
    int number() {
        int c = byte();
        while (c != EOF && c <= ' ')
            c = byte();
        int sign = 1;
        if (c == '-') {
            sign = -1;
            c = byte();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = byte();
        }
        return value * sign;
    }
};
class Output {
    char data[IO_SIZE];
    int size = 0;

  public:
    void flush() {
        std::fwrite(data, 1, size, stdout);
        size = 0;
    }
    void byte(char c) {
        if (size == IO_SIZE)
            flush();
        data[size++] = c;
    }
    void number(unsigned long long value) {
        char digits[DECIMAL_DIGITS];
        int count = 0;
        do {
            digits[count++] = '0' + value % 10;
            value /= 10;
        } while (value);
        while (count)
            byte(digits[--count]);
    }
};

int main() {
    Input input;
    Output output;
    int queries = input.number();
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
        const int prime = input.number();
        auto &root = roots[prime / 2];
        if (!root) {
            root = largest_root(prime);
        }
        output.number(root);
        output.byte('\n');
    }
    output.flush();
}
