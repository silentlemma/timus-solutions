#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

constexpr int MODULUS = 40961;

int power(int base, int exponent) {
    int result = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = static_cast<std::int64_t>(result) * base % MODULUS;
        }
        base = static_cast<std::int64_t>(base) * base % MODULUS;
        exponent /= 2;
    }
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string bits;
    std::cin >> bits;
    int size = static_cast<int>(bits.size());
    std::vector<int> row(size);
    int ones = 0;
    int factorial = 1;
    for (int index = 0; index < size; ++index) {
        row[index] = bits[index] - '0';
        ones += row[index];
        factorial = static_cast<std::int64_t>(factorial) * (index + 1) % MODULUS;
    }

    std::vector<int> inverse_factorial(size + 1);
    inverse_factorial[size] = power(factorial, MODULUS - 2);
    for (int index = size; index > 0; --index) {
        inverse_factorial[index - 1] =
            static_cast<std::int64_t>(inverse_factorial[index]) * index % MODULUS;
    }

    std::vector<int> answer(size + 1);
    std::int64_t total = 1;
    std::int64_t sum = ones;
    for (int length = size - 1; length > 0; --length) {
        std::int64_t squares = 0;
        // Counts are scaled by the factorial of the number of omitted positions.
        for (int index = 0; index < length; ++index) {
            row[index] = ((length - index) * row[index] + (index + 1) * row[index + 1]) % MODULUS;
            squares += static_cast<std::int64_t>(row[index]) * row[index];
        }
        total = total * (length + 1) % MODULUS;
        sum = sum * length % MODULUS;
        std::int64_t value = (total * sum - squares) % MODULUS;
        if (value < 0) {
            value += MODULUS;
        }
        std::int64_t inverse = inverse_factorial[size - length];
        answer[length] = value * inverse % MODULUS * inverse % MODULUS;
    }

    for (int length = 1; length <= size; ++length) {
        if (length > 1) {
            std::cout << ' ';
        }
        std::cout << answer[length];
    }
    std::cout << '\n';
}
